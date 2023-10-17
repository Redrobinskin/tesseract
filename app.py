```python
from flask import Flask, render_template, request, jsonify
import load_images
import preprocess_image
import further_preprocessing
import extract_text
import output_to_json
import init_db
import store_output
import retrieve_data

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/load_images', methods=['POST'])
def load():
    directory_path = request.json['directory_path']
    images = load_images.load_images(directory_path)
    return jsonify({'message': 'Images loaded successfully'}), 200

@app.route('/preprocess_image', methods=['POST'])
def preprocess():
    image = request.json['image']
    preprocessed_image = preprocess_image.preprocess_image(image)
    return jsonify({'message': 'Image preprocessed successfully'}), 200

@app.route('/further_preprocessing', methods=['POST'])
def further_preprocess():
    image = request.json['image']
    segments = further_preprocessing.further_preprocessing(image)
    return jsonify({'message': 'Image further preprocessed successfully'}), 200

@app.route('/extract_text', methods=['POST'])
def extract():
    image = request.json['image']
    text = extract_text.extract_text(image)
    return jsonify({'message': 'Text extracted successfully', 'text': text}), 200

@app.route('/output_to_json', methods=['POST'])
def output():
    text = request.json['text']
    json_output = output_to_json.output_to_json(text)
    return jsonify({'message': 'Text outputted to JSON successfully', 'json_output': json_output}), 200

@app.route('/init_db', methods=['GET'])
def init():
    init_db.init_db()
    return jsonify({'message': 'Database initialized successfully'}), 200

@app.route('/store_output', methods=['POST'])
def store():
    json_output = request.json['json_output']
    store_output.store_output(json_output)
    return jsonify({'message': 'Output stored successfully'}), 200

@app.route('/retrieve_data', methods=['GET'])
def retrieve():
    id = request.args.get('id')
    data = retrieve_data.retrieve_data(id)
    return jsonify({'message': 'Data retrieved successfully', 'data': data}), 200

if __name__ == '__main__':
    app.run(debug=True)
```