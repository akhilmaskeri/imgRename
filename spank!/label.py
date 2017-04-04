import os,io
import sys
from google.cloud import vision

client = vision.Client()

if len(sys.argv) <= 1:
    print "please specify the path of the file "
    exit(0)

if not os.path.isfile(sys.argv[1]):
    print "please specify the path of the file "
    exit(0)

with io.open(sys.argv[1],'rb') as f:
    content = f.read()
    img = client.image(content=content)

labels = img.detect_labels()

print "-"*50
print("labels :")
for label in labels:
    print(label.description)

faces = img.detect_faces(limit=50)
face = faces[0]

print "-"*50

print "joy : ",face.joy
print "anger: ",face.anger
print "sorrow :",face.sorrow
print "surprise :",face.surprise
print "headwear :",face.headwear


