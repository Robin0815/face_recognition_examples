import face_recognition
from PIL import Image
import numpy as np

image_of_bill = face_recognition.load_image_file('./img/known/Bill Gates.jpg')
bill_face_encoding = face_recognition.face_encodings(image_of_bill)[0]

unknown_image = face_recognition.load_image_file(
    './img/unknown/d-trump.jpg')
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

image_of_bill = Image.fromarray(image_of_bill)
unknown_image = Image.fromarray(unknown_image)

# Compare faces
results = face_recognition.compare_faces(
    [bill_face_encoding], unknown_face_encoding)

if results[0]:
    print('This is Billy')
else:
    print('This is NOT Billy')

width1, height1 = image_of_bill.size
width2, height2 = unknown_image.size

width, height = max(width1, width2), max(height1, height2)

image_of_bill= image_of_bill.resize((width, height))
unknown_image= unknown_image.resize((width, height))

Image.fromarray(np.hstack((np.array(image_of_bill), np.array(unknown_image)))).show()
