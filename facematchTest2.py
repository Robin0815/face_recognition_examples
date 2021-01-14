import face_recognition
from PIL import Image
import numpy as np
# from PIL.ExifTags import TAGS
import os


def display(im):
    im.show()


image_of_balmer = face_recognition.load_image_file('/home/nutzer/Documents/TestData2/Steve_Ballmer_2014.jpeg')
balmer_face_encoding = face_recognition.face_encodings(image_of_balmer)[0]

unknown_image = face_recognition.load_image_file(
    '/home/nutzer/Documents/TestData2/index.jpeg')
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

image_of_balmer = Image.fromarray(image_of_balmer)
unknown_image = Image.fromarray(unknown_image)
# Compare faces
results = face_recognition.compare_faces(
    [balmer_face_encoding], unknown_face_encoding)

if results[0]:
    print('This is Steve Balmer')
else:
    print('This is NOT Steve Balmer')

width1, height1 = image_of_balmer.size
width2, height2 = unknown_image.size

width, height = max(width1, width2), max(height1, height2)

image_of_balmer = image_of_balmer.resize((width, height))
unknown_image = unknown_image.resize((width, height))

Image.fromarray(np.hstack((np.array(image_of_balmer), np.array(unknown_image)))).show()

if results[0]:
    a=0
    stream = os.popen('exiftool -Subject=SteveBalmer /home/nutzer/Documents/TestData2/index.jpeg')
