import face_recognition
from PIL import Image
import numpy as np
# from PIL.ExifTags import TAGS
import os


def display(im):
    im.show()


image_of_ballmer = face_recognition.load_image_file('./img/Steve_Ballmer_2014.jpeg')
ballmer_face_encoding = face_recognition.face_encodings(image_of_ballmer)[0]

unknown_image = face_recognition.load_image_file(
    './img/UnknownBalmer.jpeg')
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

image_of_ballmer = Image.fromarray(image_of_ballmer)
unknown_image = Image.fromarray(unknown_image)
# Compare faces
results = face_recognition.compare_faces(
    [ballmer_face_encoding], unknown_face_encoding)

if results[0]:
    print('This is Steve Ballmer')
else:
    print('This is NOT Steve Ballmer')

width1, height1 = image_of_ballmer.size
width2, height2 = unknown_image.size

width, height = max(width1, width2), max(height1, height2)

image_of_ballmer = image_of_ballmer.resize((width, height))
unknown_image = unknown_image.resize((width, height))

Image.fromarray(np.hstack((np.array(image_of_ballmer), np.array(unknown_image)))).show()

"""

#Change to add "Subject" to the picture metadata
if results[0]:
    stream = os.popen('exiftool -Subject=SteveBallmer /home/robin/PycharmProjects/face_recognition_examples/img/UnknownBalmer.jpeg')

"""