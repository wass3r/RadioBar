## RadioBar

Basic macOS menubar app to play SomaFM radio stations with help from [rumps](https://github.com/jaredks/rumps) and VLC.

## Development

Make sure you have VLC installed, ie. `brew cask install vlc`.

Tested in Python 2.7.x and 3.x. To run, try:
1. `pip install -r requirements.txt`
2. `python radiobar.py`

To re-build the macOS app, run:
1. `rm -rf ./dist/ ./build/`
2. `python setup.py py2app`

## License
MIT