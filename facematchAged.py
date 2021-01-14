import face_recognition
from PIL import Image
import numpy as np
# from PIL.ExifTags import TAGS
import os


def display(im):
    im.show()


image_of_keanu = face_recognition.load_image_file('/home/nutzer/Documents/keanu-reeves-2000.jpg')
keanu_face_encoding = face_recognition.face_encodings(image_of_keanu)[0]

unknown_image = face_recognition.load_image_file(
    '/home/nutzer/Documents/keanu-reeves-9454211-1-402.jpg')
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

image_of_keanu = Image.fromarray(image_of_keanu)
unknown_image = Image.fromarray(unknown_image)
# Compare faces
results = face_recognition.compare_faces(
    [keanu_face_encoding], unknown_face_encoding)

if results[0]:
    print('This is Keanu')
else:
    print('This is NOT Keanu')

width1, height1 = image_of_keanu.size
width2, height2 = unknown_image.size

width, height = max(width1, width2), max(height1, height2)

image_of_keanu = image_of_keanu.resize((width, height))
unknown_image = unknown_image.resize((width, height))

Image.fromarray(np.hstack((np.array(image_of_keanu), np.array(unknown_image)))).show()

if results[0]:
    stream = os.popen('exiftool -Subject=KeanuReeves /home/nutzer/Documents/keanu-reeves-9454211-1-402.jpg')

