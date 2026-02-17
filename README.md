# Bin Picking — Vision + Igus Robot 

This repo shows a simple bin-picking workflow: a camera-based vision script detects parts, classifies shapes (square vs circle), computes their center and orientation, converts pixel coordinates to robot-base coordinates, and a robot program performs a pick-and-place into different bins.

## What’s in this repository
- `finalallinone.py` — Python/OpenCV vision script that captures video, thresholds, finds contours, detects rectangular objects, computes center and rotation, and converts pixel coordinates to robot coordinates (`rob_coord`).
- `final_testing.st` — Robot station program (robot language) with predefined points and a pick-and-place sequence (home, pickup hover, pickup, place, etc.).


## Overview (Beginner-friendly)
1. The camera captures a live image.
2. The script thresholds the image and finds contours.
3. Each contour is analyzed. If a contour approximates to 4 points, it is treated as a rectangle (square/box) and sent to one bin; if it looks circular, it should be sent to another bin.
4. The script computes the pixel center and rotation angle of the object, converts the pixel coordinates into the robot's base coordinates (using a simple linear mapping), and prints the coordinates.
5. Those coordinates can be used to update the robot waypoints in `final_testing.st` or sent directly to the robot controller using a communication link you add (serial, TCP, etc.).

## Requirements
- Python 3.8+ (Windows recommended in this repo)
- OpenCV for Python

Install dependencies with pip:

```bash
python -m pip install --upgrade pip
pip install opencv-python
```

## Run the vision script
1. Connect a webcam to your computer.
2. Run:

```bash
python finalallinone.py
```

3. The script opens two windows: the live `frame` and the `Threshold Frame`.
4. Press `q` to quit. When you quit, the script will print the last detected object's pixel center, rotation angle, and the converted robot coordinates.

Example output printed on exit:

```
The center of the first contour is at pixel coordinates (cx, cy)
The Orientation of the detected rectangular piece is : <angle>
The Co-Ordinates of detected point in robot base frame are : (X_rob, Y_rob)
```

