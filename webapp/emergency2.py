import cv2

# Load the image
img = cv2.imread('media/img/ambulance.jpeg')

# Display the image
cv2.imshow('Image', img)

# Wait for a key press to close the window


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

cv2.waitKey(0)
# Clean up
cv2.destroyAllWindows()
