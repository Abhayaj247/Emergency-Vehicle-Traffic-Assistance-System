import cv2
import cv2
import numpy as np
import os

cap = cv2.VideoCapture('emergencyv.mp4')
while True:
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.4)
        cv2.imshow('Video', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

import subprocess

# Set the path to the ampy executable
ampy_path = "C:\\Users\\qwert\\anaconda3\\envs\\env\\Scripts\\ampy.exe"

# Set the port for the ESP32
port = "COM5"

# Set the path to the ESP32 code
esp32_code_path = "blink.py"

# Construct the command to run the code on the ESP32
cmd = [ampy_path, "--port", port, "run", esp32_code_path]
# Run the command in the shell
subprocess.run(cmd)

cap.release()
cv2.destroyAllWindows()
