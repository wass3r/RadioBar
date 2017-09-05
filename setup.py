from setuptools import setup

APP = ['radiobar.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,
    },
    'packages': ['rumps'],
    'iconfile': 'radio-icon.png',
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
