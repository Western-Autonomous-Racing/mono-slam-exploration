import math

# Define intrinsic parameters of camera
# image plane dimensions in mm
canvas_width = 750
canvas_height = 300
distance = 100  # in mm to image plane

# Calculate size of image plane
hfov = math.degrees(2 * math.atan((canvas_width/2) / (distance)))
vfov = math.degrees(2 * math.atan((canvas_height/2) / (distance)))

print("Vertical FOV: ", vfov)
print("Horizontal FOV: ", hfov)

# calculate pixel density
