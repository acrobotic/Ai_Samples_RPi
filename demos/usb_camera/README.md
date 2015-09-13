Raspberry Pi 2 USB Camera
=========================

## Driver

The Raspberry Pi supports USB cameras that are compliant with the USB Video Class (UVC) specification using the `uvcvideo` driver. Supported cameras will be accessible via the device nodes `/dev/video0`, `/dev/video1`, etc...

## Program

### Simple Catpure

Install `streamer`.

    sudo apt-get install streamer

Take a JPEG picture.

    streamer -c /dev/video0 -o outfile.jpeg

Record a short 10 second video.

    streamer -q -c /dev/video0 -f rgb24 -r 3 -t 00:00:10 -o outfile.avi

### Advanced Capture

Using Python and OpenCV you can control when frames are captured and perform some image processing to further control what is done.

    sudo apt-get install python-opencv python-numpy
    ./python.py

## Additional Resources

1. [OpenCV](http://www.opencv.org/)
1. [Python](https://www.python.org/)
1. [OpenCV Python Tutorials](http://docs.opencv.org/trunk/doc/py_tutorials/py_tutorials.html)

