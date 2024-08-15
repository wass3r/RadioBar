## RadioBar

Basic macOS menubar app to play SomaFM radio stations with help from [rumps](https://github.com/jaredks/rumps), VLC, and Briefcase.

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
1. check `build/radiobar/macos/app` folder for application to launch

#### Create macOS installer

1. clean dist folder: `rm -rf ./dist`
1. `poetry run briefcase package`
1. check `dist/` folder for `.dmg` installer

## License

MIT
