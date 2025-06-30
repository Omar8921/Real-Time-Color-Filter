# Real-Time HSV Color Filter

This project implements a real-time color detection system using OpenCV. The program captures video from the webcam, converts each frame to HSV color space, and filters specific color ranges based on user input. It demonstrates how to isolate red, blue, or green regions in live video using color masks.

## Features

- Live webcam feed
- HSV color space filtering
- Predefined color filters for red, blue, and green
- Keyboard input to switch filters instantly
- Gaussian blur applied to smooth the binary mask
- ESC key to exit, Enter key to reset filters

## How It Works

1. Each frame from the webcam is flipped and converted from BGR to HSV.
2. Based on the selected color filter, a specific HSV range is used to generate a binary mask.
3. The mask is applied to the original frame using `cv2.bitwise_and` to extract only the selected color.
4. The output is displayed in a single window.

## Controls

| Key      | Action             |
|----------|--------------------|
| R or r   | Apply red filter   |
| B or b   | Apply blue filter  |
| G or g   | Apply green filter |
| S or s    | Take a screenshot |
| Enter    | Reset (remove filter) |
| ESC      | Exit the program   |

## Requirements

- Python 3.6+
- OpenCV (`opencv-python`)
- NumPy

Install requirements:
```bash
pip install opencv-python numpy
