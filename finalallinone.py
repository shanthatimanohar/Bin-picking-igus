import cv2
import math
def rob_coord(val1, val2):
    kx = 0.425
    ky = 0.406
    X_off = 155
    Y_off = 210
    X_rob = X_off+(kx*val1)
    Y_rob = Y_off-(ky*val2)-6
    X_rob = math.ceil(X_rob)
    Y_rob = math.ceil(Y_rob)
    print('The Co-Ordinates of detected point in robot base frame are :', (X_rob, Y_rob))
# Start the camera
cap = cv2.VideoCapture(0)

# Set the frame width to 640*480
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Declare the center variable and angle variable before the loop
center = None
rot_angle = None

while True:
    # Capture the frame
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply a threshold of 180,255
    _, thresh = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)

    # Find the contours based on the area min and max
    contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = [c for c in contours if cv2.contourArea(c) > 700 and cv2.contourArea(c) < 15000]

    # Number the contours in order
    contours = sorted(contours, key=lambda x: cv2.contourArea(x))
    for i, c in enumerate(contours):
        cv2.putText(frame, str(i), (int(cv2.minEnclosingCircle(c)[0][0]), int(cv2.minEnclosingCircle(c)[0][1])), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Find the center point of the first contour only in pixel coordinates
    if len(contours) > 0:
        M = cv2.moments(contours[0])
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        center = (cx, cy)  # Update the center variable
        cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)
        cv2.putText(frame, f"({cx}, {cy})", (cx+20, cy-20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        # Iterate through contours and find rectangles with area between 700 and 15000
    for cnt in contours:
        # Calculate area of contour
        area = cv2.contourArea(cnt)

        if area > 700 and area < 15000:
            # Approximate contour to polygon
            approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)

            # If polygon has 4 sides, it's a rectangle
            if len(approx) == 4:
                # Draw rectangle on original frame
                cv2.drawContours(frame, [approx], 0, (0, 255, 0), 2)

                # Find rotation angle of rectangle with respect to image frame origin
                rect = cv2.minAreaRect(cnt)
                angle = rect[2]

                # Display angle circle on frame
                center = tuple(map(int, rect[0]))
                radius = 5
                cv2.circle(frame, center, radius, (255, 0, 0), 2)
                rot_angle = angle

                # Print rotation angle
                #print("Rotation angle:", angle)
       

    # Show the frame
    cv2.imshow('frame', frame)
    cv2.imshow('Threshold Frame', thresh)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()

# Use the center variable outside the loop
if center is not None:
    print(f"The center of the first contour is at pixel coordinates ({center[0]}, {center[1]})")
    print("The Orinetation of the detected rectangular piece is :", rot_angle)
    a, b = center
    a = int(a)
    b = int(b)
    rob_coord(a,b)
else:
    print("No contours were found in the video stream") 