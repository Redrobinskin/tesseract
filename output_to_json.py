```python
import json

def output_to_json(text):
    """
    Output the extracted text in JSON format.
    """
    json_output = json.dumps(text)
    return json_output
```