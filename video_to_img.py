import cv2
vidcap = cv2.VideoCapture('72.mp4')
success,image = vidcap.read()
count = 0
while success:
    success,image = vidcap.read()

    if count % 25 == 0:
        cv2.imwrite("gambar1/72_frame%d.png" % count, image)     # save frame as JPEG file      
        print('Read a new frame: ', success)
    count += 1