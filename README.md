# Chehro

Chehro is a face detection library for python with a _[mediapipe](https://google.github.io/mediapipe)_ backend. It is faster and more accurate comparing to the old _HAARCASCADE Classifier_ way of face detection in python/OpenCV. 

![Tested on a picture of Elon Musk](https://github.com/prp-e/chehro/raw/master/result.jpg)

## Installation guide

### From source

First of all, you have to clone this repository to your local machine:

```
git clone https://github.com/prp-e/chehro
```

Then, you move to the source directory and run:

```
pip3 install -e .
```

_NOTE_: In some systems(specially Linux based ones) _pip3_ might be just _pip_, since most of moderl Linux distributions just left Python2 behind. 

### From PyPi

In case you want this package to be installed using _pip_ then just run this command:

```
pip3 install chehro
```

_NOTE_: In some systems(specially Linux based ones) _pip3_ might be just _pip_, since most of moderl Linux distributions just left Python2 behind. 

## How to use

First, create a new python environment or project. Then you easily can do this:

```python
import cv2
from chehro import Chehro

image = cv2.imread('faces.jpg')
detector = Chehro(image)

result, bboxes = detector.detect()

# In case you might need no bounding box drawn around faces, just run it like this
result, bboxes = detector.detect(draw=False)
```

_NOTE_ : `detect()` method returns a tuple made of an image (or the result) and a list of bounding boxed. All bounding boxes are normalized and you don't need to normalize it manually.
