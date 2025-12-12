# radiobar

Basic macOS menubar app to play SomaFM radio stations with help from [rumps](https://github.com/jaredks/rumps), VLC, and Briefcase.

## Why?

Initially just an idea to try `rumps`, but in daily use since. A simple, lite, and unobtrusive way to play internet radio.

No affiliation with SomaFM. They just had an easy station feed and good selection of genres, so you can station-hop depending on mood. Go support them @ https://somafm.com/support/.

## Roadmap

Mostly just regular maintenance to keep it working and maybe small-ish improvements.

The only thing I might explore further as a feature is the ability to pull stations from a local, custom config.

## Development/Running

### Prerequisites

- [poetry](https://python-poetry.org/)
- VLC 3.x (`brew cask install vlc`)

#### Run

1. `poetry install`
1. `poetry run briefcase dev`

#### Build macOS app

1. clean build folder: `rm -rf ./build`
1. `poetry run briefcase create`
1. `poetry run briefcase build`
1. check `./build/radiobar/macos/app` folder for application to launch

#### Create macOS installer

1. clean dist folder: `rm -rf ./dist`
1. `poetry run briefcase package`
1. check `./dist/` folder for `.dmg` installer

## License

MIT
