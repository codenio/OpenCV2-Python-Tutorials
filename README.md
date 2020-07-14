# OpenCV2-Python-Tutorials
OpenCV2 Python Tutorials For Beginners

### Requirements
- numpy==1.19.0
- opencv-python==4.2.0.34

### Getting Started

- Install [python 3](https://www.python.org/downloads/) from official website
- Install virtualenv to crate a isolated work environment
    ```bash
    $ pip3 install virtualenv
    ```
- Install virtualenvwrapper to control virtual work enviroments
    ```bash
    $ pip3 install virtualenvwrapper
    ```
- Create openvc virtual env 
    ```bash
    $ mkvirtualenv openvc
    ``` 
- Clone this repository and enter into the OpenCV2-Python-Tutorials directory
    ```bash
    $ git clone git@github.com:codenio/OpenCV2-Python-Tutorials.git
    ....
    $ cd OpenCV2-Python-Tutorials    
    ```
- Install the requirement using requirements.txt
    ```bash
    $ pip3 install -r requirements.txt
    ```
- Move to the required directory and execute python file to view the results
    ```
    $ cd basics/images
    $ python3 images.py
    ```
  
### Index
- [basics](basics)
    - [images](basics/images)
        - [image.py](basics/images/image.py)
    - [shapes](basics/shapes)
        - [shapes.py](basics/shapes/shapes.py)
    - [webcam](basics/webcam)
        - [webcam.py](basics/webcam/webcam.py)
        - [canny-webcam.py](basics/webcam/canny-webcam.py)

- [trackbar](trackbar)
    - [threshold-trackbar.py](trackbar/threshold-trackbar.py)
    - [hsv-trackbar.py](trackbar/hsv-trackbar.py)