#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rumps
import vlc
import os
import platform
import requests

# rumps.debug_mode(True)

if 'VLC_PLUGIN_PATH' not in os.environ:
    print('VLC_PLUGIN_PATH not set. Setting now...')
    os.environ['VLC_PLUGIN_PATH'] = '$VLC_PLUGIN_PATH:/Applications/VLC.app/Contents/MacOS/plugins'


class RadioBar(rumps.App):
    station_list_url = u'http://somafm.com/channels.json'
    station_url_pattern = u'http://ice%d.somafm.com/%s-128-mp3'

    def __init__(self):
        super(RadioBar, self).__init__('RadioBar',
                                       icon='radio-icon.png', template=True, quit_button=None)
        self.active_station = None
        self.player = vlc.MediaPlayer()
        self.stations = []
        self.get_stations()

    def build_menu(self):
        self.menu.clear()

        if len(self.stations) < 1:
            rumps.alert('No stations loaded.')

        new_menu = []

        new_menu.append(rumps.MenuItem(
            'Pause', callback=self.toggle_playback))
        new_menu.append(rumps.MenuItem(
            'Stop', callback=self.stop_playback))
        new_menu.append(rumps.separator)

        for station in self.stations:
            item = rumps.MenuItem(station, callback=self.play)
            new_menu.append(item)

        new_menu.append(rumps.separator)
        new_menu.append(rumps.MenuItem('Quit RadioBar',
                                       callback=rumps.quit_application))

        self.menu = new_menu

    def get_stations(self):
        if len(self.stations) > 0:
            return

        try:
            r = requests.get(self.station_list_url)
            r.raise_for_status()
            j = r.json()
            for c in j['channels']:
                self.stations.append(c['id'])
        except requests.exceptions.RequestException as e:
            rumps.alert(e)

        self.build_menu()

    def play_radio(self):
        # reset Pause
        self.menu['Pause'].state = 0
        self.menu['Pause'].title = 'Pause'

        # craft station url
        station_url = self.station_url_pattern % (1, self.active_station)
        print(u'playing %s' % station_url)

        # feed url to player
        self.player.set_mrl(station_url)
        self.player.play()

    def reset_menu_state(self):
        if self.active_station is None:
            return
        self.menu[self.active_station].state = 0
        self.menu[self.active_station].set_callback(self.play)
        self.active_station = None
        self.menu['Stop'].state = 0
        self.menu['Pause'].state = 0
        self.menu['Pause'].title = 'Pause'

    def play(self, sender):
        # is there already a station playing or a paused station?
        if self.active_station is not None and self.menu[self.active_station].state is not 0:
            self.reset_menu_state()

        self.active_station = sender.title
        sender.state = 1
        sender.set_callback(None)
        self.play_radio()

    def stop_playback(self, sender):
        sender.state = 1
        self.reset_menu_state()
        self.player.stop()

    def toggle_playback(self, sender):
        if self.active_station is not None:
            active_menu = self.menu[self.active_station]
            if active_menu.state == 1:
                active_menu.state = -1
                sender.title = 'Resume'
                sender.state = 1
                self.player.pause()
            else:
                active_menu.state = 1
                sender.title = 'Pause'
                sender.state = 0
                self.player.play()


if __name__ == "__main__":
    RadioBar().run()
