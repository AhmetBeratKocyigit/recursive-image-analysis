
import os
from PIL import Image

IMAGE_DIR = "images"
RESULT_DIR = "results"
GRAPH_DIR = "graphs"

os.makedirs(RESULT_DIR, exist_ok=True)
os.makedirs(GRAPH_DIR, exist_ok=True)

def load_images():
    files = sorted(f for f in os.listdir(IMAGE_DIR) if f.endswith(".png"))
    return [Image.open(os.path.join(IMAGE_DIR, f)).convert("RGB") for f in files]
