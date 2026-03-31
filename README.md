📌 Overview
This project implements an automated Instance Segmentation system using the YOLOv8 (You Only Look Once) architecture. While traditional object detection identifies items within a rectangular bounding box, this implementation performs pixel-level segmentation, allowing for a finer and more accurate representation of object boundaries.

📂 Project Structure
Plaintext
image-segmentation-yolo/
├── data/               # Input media (e.g., test.webp) for testing
├── models/             # Directory for pre-trained YOLO weights (.pt)
├── runs/               # Auto-generated directory for inference results
├── src/                # Source code directory
│   ├── __init__.py
│   └── predict.py      # Main CLI execution script
├── requirements.txt    # List of Python dependencies
└── README.md           # Project documentation and setup guide
⚙️ Implementation Pipeline
The project follows a structured engineering pipeline to move from raw data to segmented output:


Input Ingestion: The system utilizes an argparse interface to accept various media formats (images/videos) from the data/ directory.


Preprocessing: Input frames are normalized and resized to the model’s required input dimensions (e.g., 640x640) using the Ultralytics framework.


Feature Extraction: The CSPDarknet53 backbone processes the image to identify complex spatial features and semantic patterns.


Segmentation Head: Instead of a standard detection head, the model utilizes a specialized segmentation branch that computes a binary mask for every identified object.


Post-Processing: The system applies a confidence threshold (default 0.5) and Non-Maximum Suppression (NMS) to filter out weak detections and overlapping masks.


Result Persistence: Final masks, labels, and confidence scores are rendered onto the image and saved to the runs/segment/predict/ directory for verification.

🛠️ Setup Instructions
1. Clone the Repository
Bash
git clone https://github.com/manasvi-maheshwari/Image_Segmentation_YOLO.git
cd Image_Segmentation_YOLO
2. Install Dependencies
Ensure you have Python 3.8+ installed, then run:

Bash
pip install -r requirements.txt
3. Execution
To run the segmentation on your local device, use the following terminal command:

Bash
python src/predict.py --source data/test.webp

📊 Results
Upon execution, the model processes the image and saves the output (containing masks and confidence scores) to:
runs/segment/predict/


Example Results: During testing, the model successfully identified objects (e.g., cats) with high confidence scores, such as 0.87 and 0.84.

💻 Tech Stack

Language: Python 


Framework: Ultralytics - YOLOv8 

Libraries:


OpenCV: For image handling and visualization.


NumPy: For high-performance array manipulations.


Argparse: For robust command-line interface management.
