import os,io
import time
from google.cloud import vision

client = vision.Client()

with io.open("/Path/to/your/image/file",'rb') as q:
    content = q.read()
    img = client.image(content=content)

safe = img.detect_safe_search()

if str(safe.adult) == "Likelihood.VERY_LIKELY":
    print "you perv!!"


