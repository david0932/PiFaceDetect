import cv2
import sys
import urllib2
import time
# file
import os
from glob import glob
# post to web server
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2


# Get user supplied values
imagePath = sys.argv[1]
cascPath = sys.argv[2]

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

print "Found {0} faces!".format(len(faces))

#send to web server
ts = int(time.time())
retUrl = 'http://192.168.101.222/tv/face_detect.php?face='+format(len(faces))+'&timestamp='+str(ts)
print retUrl
response = urllib2.urlopen(retUrl)

i = 0
# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    face_img = image[y: y + h, x: x + w]
    filename = "face%d.jpg" % (i)
    i = i + 1
    cv2.imwrite(filename,face_img)
cv2.imwrite("detect.jpg",image)
#cv2.imshow("Faces found", image)
#cv2.waitKey(0)

# send detect face image to web server
face_cnt = len(faces)
#print "face_cnt = %d" % face_cnt
if face_cnt > 0 :
   # Register the streaming http handlers with urllib2
   register_openers()

   #upload file loop
   i = 0  
   for i in range (face_cnt) :
      filename = "face%d.jpg" % (i)
      i = i + 1
      # headers contains the necessary Content-Type and Content-Length
      # datagen is a generator object that yields the encoded parameters
      datagen, headers = multipart_encode({"file": open(filename, "rb")})
      # Create the Request object
      request = urllib2.Request("http://192.168.101.222/tv/upload_file.php", datagen, headers)
      # Actually do the request, and get the response
      print urllib2.urlopen(request).read()
     
   # send detect image to web server
   datagen, headers = multipart_encode({"file": open("detect.jpg", "rb")})
   request = urllib2.Request("http://192.168.101.222/tv/upload_file.php", datagen, headers)
   print urllib2.urlopen(request).read()

   # send capture image to web server
   #datagen, headers = multipart_encode({"file": open("image.jpg", "rb")})
   #request = urllib2.Request("http://192.168.101.222/tv/upload_file.php", datagen, headers)
   #print urllib2.urlopen(request).read()
