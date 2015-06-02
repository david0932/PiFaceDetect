import cv2
import sys
import urllib2
import time
import os
from glob import glob

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

#print "Found {0} faces!".format(len(faces))

#send to web server
#ts = int(time.time())
#retUrl = 'http://192.168.101.222/tv/face_detect.php?face='+format(len(faces))+'&timestamp='+str(ts)
#print retUrl
#response = urllib2.urlopen(retUrl)

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

