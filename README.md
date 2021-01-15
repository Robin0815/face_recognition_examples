# face_recognition_examples
Examples for Python Face Recognition library

## How to use
These code examples use the face-recognition python library
[https://pypi.org/project/face-recognition/]
[https://github.com/ageitgey/face_recognition]

for a more detailed description I highly recommend to use these ressources

The code this project is based on:
[https://github.com/bradtraversy/face_recognition_examples]

## Installing
It is fairly easy to setup a development environment in Linux and I would recommend doing so, Mac and Windows should work but is not worth the hassle in my opinion.
For Windows users it is easier to just setup a Virtual Machine with Linux, recommended Ubunu 20.04 LTS.
In Ubuntu install your favorite Python Env, I used Anaconda 2020.11.
```
sudo apt-get install -y --fix-missing     build-essential     cmake     gfortran     git     wget     curl     graphicsmagick     libgraphicsmagick1-dev     libatlas-base-dev     libavcodec-dev     libavformat-dev     libgtk2.0-dev     libjpeg-dev     liblapack-dev     libswscale-dev     pkg-config     python3-dev     python3-numpy     software-properties-common     zip     && apt-get clean && rm -rf /tmp/* /var/tmp/*
```

```
cd ~ &&     mkdir -p dlib &&     git clone -b 'v19.9' --single-branch https://github.com/davisking/dlib.git dlib/ &&     cd  dlib/ &&     python3 setup.py install --yes USE_AVX_INSTRUCTIONS
```

```
pip install face-recognition
```

afterwards you should be able to use the library

For a good understanding of face recognition algorithms I recommend the OpenCV dcumentation:
Face detection [https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html]
Face recognition [https://docs.opencv.org/3.4/da/d60/tutorial_face_main.html]
