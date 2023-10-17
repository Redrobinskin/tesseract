```python
from PIL import Image
import pytesseract

def extract_text(image):
    """
    Extract text from the preprocessed image using Tesseract.
    """
    # Convert the image to grayscale
    image = image.convert('L')

    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(image)

    return text
```