import cv2 # pip install opencv-python
import numpy as np # pip install numpy

video = cv2.VideoCapture('final.mp4')
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
threshold = 20.

writer = cv2.VideoWriter('final2.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height))
ret, frame1 = video.read()
prev_frame = frame1

a = 0
b = 0
c = 0

protopath = 'MobileNetSSD_deploy.prototxt'
modelpath = 'MobileNetSSD_deploy.caffemodel'

detector = cv2.dnn.readNetFromCaffe(prototxt=protopath, caffeModel=modelpath)

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]

while True:
    ret, frame = video.read()
    (H, W) = frame.shape[:2]

    blob = cv2.dnn.blobFromImage(frame, 0.007843, (W, H), 127.5)

    detector.setInput(blob)
    person_detections = detector.forward()

    for i in np.arange(0, person_detections.shape[2]):
        confidence = person_detections[0, 0, i, 2]
        if confidence > 0.5:
            idx = int(person_detections[0, 0, i, 1])

            if CLASSES[idx] != "person":
                continue

            person_box = person_detections[0, 0, i, 3:7] * np.array([W, H, W, H])
            (startX, startY, endX, endY) = person_box.astype("int")

            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 0, 255), 2)

            if (((np.sum(np.absolute(frame - prev_frame)) / np.size(frame)) > threshold)):
                writer.write(frame)
                prev_frame = frame
                a += 1
            else:
                prev_frame = frame
                b += 1

    cv2.imshow("Application", frame)
    c += 1

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

print("Total frames: ", c)
print("Unique frames: ", a)
print("Common frames: ", b)
video.release()
writer.release()
cv2.destroyAllWindows()