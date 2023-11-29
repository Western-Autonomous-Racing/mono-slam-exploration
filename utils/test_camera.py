import cv2

# GStreamer pipeline for Arducam B0179
# grayscale
# pipeline = (
#     "nvarguscamerasrc ! video/x-raw(memory:NVMM),width=1920,height=1080,format=(string)NV12,framerate=(fraction)30/1 ! "
#     "nvvidconv ! videoconvert ! videoflip method=rotate-180 ! appsink"
# )

# RGB
pipeline = (
    "nvarguscamerasrc ! video/x-raw(memory:NVMM),width=1920,height=1080,format=(string)NV12,framerate=(fraction)30/1 ! "
    "nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert ! videoflip method=rotate-180  ! appsink"
)

# Create a VideoCapture object with the GStreamer pipeline
cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Failed to open camera")
    exit()

# Read and display frames from the camera
while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to read frame from camera")
        break
    
    cv2.imshow("Camera Stream", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()