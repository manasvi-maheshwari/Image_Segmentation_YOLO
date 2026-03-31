import argparse
import os
from ultralytics import YOLO

def run_segmentation(source_path):
    # This downloads the 'brain' (weights) automatically if not found
    model = YOLO('models/yolov8n-seg.pt') 
    
    # Run the segmentation
    print(f"Processing: {source_path}")
    results = model.predict(source=source_path, save=True, conf=0.5)
    
    print("\n" + "="*30)
    print(f"SUCCESS! Check the 'runs/segment' folder for your output.")
    print("="*30)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=str, required=True, help="Path to image file")
    args = parser.parse_args()
    
    if os.path.exists(args.source):
        run_segmentation(args.source)
    else:
        print(f"Error: File {args.source} not found!")