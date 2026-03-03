import os
import json
from transformers import ViTImageProcessor, ViTForImageClassification
from PIL import Image

from app.core.config import settings

# Initialize model lazily if needed, but for now we put placeholders
processor = None
model = None

def init_vision_model():
    global processor, model
    if processor is None or model is None:
        try:
            print(f"Loading Vision Model: {settings.VISION_MODEL_ID}...")
            processor = ViTImageProcessor.from_pretrained(settings.VISION_MODEL_ID)
            model = ViTForImageClassification.from_pretrained(settings.VISION_MODEL_ID)
            print("Vision Model Loaded.")
        except Exception as e:
            print(f"Failed to load Vision Model: {e}")

def classify_screenshot(image_path: str) -> str:
    """Classifies an image using ViT and returns JSON string of labels."""
    init_vision_model()
    if model is None:
        return json.dumps([{"label": "model_not_loaded", "score": 0.0}])
        
    if not os.path.exists(image_path):
        return json.dumps([{"error": "file_not_found"}])

    try:
        image = Image.open(image_path).convert("RGB")
        inputs = processor(images=image, return_tensors="pt")
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class_idx = logits.argmax(-1).item()
        label = model.config.id2label[predicted_class_idx]
        
        # In a real CAASM, we would map generic labels to "cisco router", "login page", etc.
        return json.dumps([{"label": label, "score": float(logits.max().item())}])
    except Exception as e:
        return json.dumps([{"error": str(e)}])
