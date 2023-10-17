# Flask App

This is a Flask application that utilizes code from a GitHub repository and incorporates it into a proper Flask app structure using Jinja2.

## Installation

1. Clone the repository
2. Install the dependencies:

```
pip install -r requirements.txt
```

## Running the App

To run the app, execute the following command:

```
python run.py
```

## Structure

The application has the following structure:

```
.
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── templates
│   │   ├── index.html
│   │   └── layout.html
│   ├── static
│   │   ├── css
│   │   │   └── main.css
│   │   └── js
│   │       └── main.js
│   ├── models.py
│   └── forms.py
├── config.py
├── run.py
├── tests
│   ├── test_basic.py
│   ├── test_models.py
│   └── test_forms.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Testing

To run the tests, execute the following command:

```
python -m unittest discover tests
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)