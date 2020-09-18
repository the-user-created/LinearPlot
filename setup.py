"""
This is a setup.py script generated by py2applet

Usage:
    python3 setup.py py2app --matplotlib-backends TkAgg
    Results in 131.9 MB app w/o "import requests, webbrowser, os"
    Results in 135.7 MB app w/ "import requests, webbrowser, os"

    python3 setup.py py2app
    Results in 207.9 MB app

    without PIL:
        CRASH
    with from PIL import Image:
        CRASH
    with python3 setup.py py2app --matplotlib-backends TkAgg --includes PIL.Image:
        CRASH
"""

from setuptools import setup

APP = ['LinearPlot.py']
DATA_FILES = ["update_boot_tracker.txt"]
OPTIONS = {"packages": ["PIL"], "iconfile": "LinearPlotIcon.icns", "plist": "Info.plist"}

setup(
    name="Linear Plot",
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
