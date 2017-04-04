# the legendary script that took my whole 273Mb of 
# chicks collection which i crawled them from some weird website
# this thing renamed it and even put it in a safe zone 
import os,io,sys
import time
from google.cloud import vision

client = vision.Client()

path = '/Path/to/your/chicks/folder/'

saved={}

for (dirpath,dirname,filename) in os.walk(path):
    for f in filename:

        print u'\U0001F914'+"    filtering ",f

        with io.open(path+f,'rb') as q:
            content = q.read()
            img = client.image(content=content)


        if img.detect_web(limit=1).web_entities:
            name = img.detect_web(limit=1).web_entities[0].description

            safe = img.detect_safe_search()
            if str(safe.adult) == "Likelihood.VERY_LIKELY":
                name = "."+name # see that's how i keep it safe from kids 

            if name not in saved:
                saved[name]=0
            else:
                saved[name]+=1
                name = name+" "+str(saved[name]+1)

            print f+" "+u'\U0001F449'+"   "+name+"  "+u'\U0001F483'

            os.rename(path+f,path+name+"."+f.split('.')[1])

            for k in range(100):
                if k!=0:
                    print u'\U0001F634',
                    sys.stdout.flush()
                if k%10 ==0 and k!=0:
                    print " ",k
                time.sleep(1)

            # what? why all these waiting?
            # if you are using the cloud platform freely then 
            # google panics if you send request within 100 secs 
            # saying something very similar to RESOURCE_EXHAUSTED

        print ""
