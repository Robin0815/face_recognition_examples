import face_recognition
from PIL import Image
import numpy as np


def display(im):
    im.show()


image_of_donald = face_recognition.load_image_file('./img/known/Donald Trump.jpg')
bill_face_encoding = face_recognition.face_encodings(image_of_donald)[0]

unknown_image = face_recognition.load_image_file(
    './img/unknown/d-trump.jpg')
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

image_of_donald = Image.fromarray(image_of_donald)
unknown_image = Image.fromarray(unknown_image)
# Compare faces
results = face_recognition.compare_faces(
    [bill_face_encoding], unknown_face_encoding)

if results[0]:
    print('This is Donald Trump')
else:
    print('This is NOT Donald Trump')

width1, height1 = image_of_donald.size
width2, height2 = unknown_image.size

width, height = max(width1, width2), max(height1, height2)

image_of_donald= image_of_donald.resize((width, height))
unknown_image= unknown_image.resize((width, height))

Image.fromarray(np.hstack((np.array(image_of_donald), np.array(unknown_image)))).show()
