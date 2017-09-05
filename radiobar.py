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
    def __init__(self):
        super(RadioBar, self).__init__('RadioBar', icon='radio-icon.png', template=True, quit_button=None)
        self.station_list_url = u'http://somafm.com/channels.json'
        self.station_url_pattern = u'http://ice%d.somafm.com/%s-128-mp3'
        self.stations = []
        self.get_stations()
        self.player = vlc.MediaPlayer()

    def build_menu(self):
        self.menu.clear()

        if len(self.stations) < 1:
            print('no stations loaded.')
            return

        new_menu = []

        for station in self.stations:
            item = rumps.MenuItem(station, callback=self.play)
            item.state = 0
            new_menu.append(item)

        new_menu.append(rumps.separator)
        new_menu.append(rumps.MenuItem('Quit RadioBar', callback=self.on_quit))

        self.menu = new_menu

    def get_stations(self):
        if len(self.stations) > 0:
            return

        r = requests.get(self.station_list_url)
        j = r.json()
        for c in j['channels']:
            self.stations.append(c['id'])

        self.build_menu()

    def play_radio(self, station):
        self.player.set_mrl(station)
        self.player.play()

    def reset_menu_states(self):
        for station in self.stations:
            self.menu[station].state = 0

    def play(self, sender):
        if self.menu[sender.title].state == 1:
            return

        self.reset_menu_states()

        station_url = self.station_url_pattern % (1, sender.title)
        self.play_radio(station_url)
        print(u'playing %s' % station_url)
        sender.state = not sender.state

    def on_quit(self, _):
        rumps.quit_application()

if __name__ == "__main__":
    RadioBar().run()
