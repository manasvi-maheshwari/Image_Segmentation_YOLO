# Image Segmentation using YOLOv8

## Overview
This project is an implementation of an automated Instance Segmentation system using the YOLOv8 algorithm. In the traditional object detection approach, the object is detected within the box; instead, the object is segmented.

## Project Structure

image-segmentation-yolo/
├── data/               # Input images (e.g., test.webp)
├── models/             # Pre-trained YOLO weights (.pt)
├── src/                # Source code
│   ├── __init__.py
│   └── predict.py      # Main execution script
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation

## Setup Instructions

### Clone the Repository

Bash
git clone [https://github.com/manasvi-maheshwari/Image_Segmentation_YOLO.git](https://github.com/manasvi-maheshwari/Image_Segmentation_YOLO.git)
cd Image_Segmentation_YOLO

### Install Dependencies

Make sure you have Python 3.8+ installed, then run:

Bash
pip install -r requirements.txt

### Execution

To run the segmentation on your local device, use the following command in your terminal:

Bash
python src/predict.py --source data/test.webp

### Results

Upon execution, the model processes the image and saves the output with the masks and confidence score to:

runs/segment/predict/

## Tech Stack

### Language

 Python

### Framework

 Ultralytics - YOLOv8

### Libraries

 OpenCV
 NumPy