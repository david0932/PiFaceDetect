rm -f *.jpg
raspistill -w 640 -h 480 -t 500 -n -o image.jpg
python face_test.py image.jpg haarcascade_frontalface_default.xml
sudo fbi -T 1 -1 -t 2 image.jpg detect.jpg face*.jpg
