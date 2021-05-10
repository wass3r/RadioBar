## RadioBar

Basic macOS menubar app to play SomaFM radio stations with help from [rumps](https://github.com/jaredks/rumps) and VLC.

## Development

### Prerequisites

* Python 3.9.x
* VLC 3.x (`brew cask install vlc`)
* Install dependencies (`pip3 install -r requirements.txt`)

#### Run

1. `python3 radiobar.py`

#### Build macOS app

1. `rm -rf ./dist/ ./build/`
1. `python3 setup.py py2app`

## License
MIT