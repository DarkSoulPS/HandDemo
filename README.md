# Machine Gesture Control

![PyPI - Python Version](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.8-blue)

Python library for gesture control of a machine's user interface using a webcam.

## Getting Started

[`Python 3.8`](https://www.python.org/downloads/release/python-3810/
) is required to run this library - other versions are untested.

### Installation

The package dependencies can be installed as follows:

```commandline
pip install --requirement requirements.txt
```

The library can then be initialised:

```commandline
python controller.py
```

This will launch a video feed popup displaying points, with overlays of boundary boxes, points and vertices as picked up by the hand detection model.

## Usage

The library supports four gesture controls:

- Single hand track for mouse control
- Close and rapidly open palm to 'click'
- Close palm and hold to drag
- 'Pistol' hands (each hand making a pistol shape) moved in and out - like framing a picture - for zoom control
