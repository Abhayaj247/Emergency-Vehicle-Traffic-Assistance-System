import cv2
import numpy as np
# Load YOLO pre-trained model and labels
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Set minimum confidence threshold and non-maximum suppression threshold
confThreshold = 0.5
nmsThreshold = 0.4

# Define colors for different classes
colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0)]

# Initialize video capture from camera or video file
cap = cv2.VideoCapture(0)

while True:
    # Read frame from video stream
    ret, frame = cap.read()

    # Convert frame to blob and feed it to the YOLO network
    blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    outputs = net.forward(net.getUnconnectedOutLayersNames())

    # Loop over the detections and draw bounding boxes around emergency vehicles
    classIDs = []
    confidences = []
    boxes = []
    for output in outputs:
        for detection in output:
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]
            if confidence > confThreshold and classID in [0, 1, 18]:
                center_x = int(detection[0] * frame.shape[1])
                center_y = int(detection[1] * frame.shape[0])
                width = int(detection[2] * frame.shape[1])
                height = int(detection[3] * frame.shape[0])
                left = int(center_x - width/2)
                top = int(center_y - height/2)
                classIDs.append(classID)
                confidences.append(float(confidence))
                boxes.append([left, top, width, height])

    # Apply non-maximum suppression to remove redundant bounding boxes
    indices = cv2.dnn.NMSBoxes(boxes, confidences, confThreshold, nmsThreshold)
    for i in indices:
        i = i[0]
        box = boxes[i]
        left, top, width, height = box
        color = colors[classIDs[i]]
        cv2.rectangle(frame, (left, top), (left+width, top+height), color, 2)
        label = f"{classes[classIDs[i]]}: {confidences[i]:.2f}"
        cv2.putText(frame, label, (left, top-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Display the output frame
    cv2.imshow("Emergency Vehicle Detection", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) == ord('q'):
        break

# Release video capture and close all windows
cap.release()
cv2.destroyAllWindows()
