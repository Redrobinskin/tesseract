```python
import os
from PIL import Image

def load_images(directory_path):
    """
    Load all images from the specified directory.
    """
    images = []
    for filename in os.listdir(directory_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img = Image.open(os.path.join(directory_path, filename))
            if img is not None:
                images.append(img)
    return images
```