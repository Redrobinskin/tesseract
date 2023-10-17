from flask import Flask, render_template
import views

app = Flask(__name__)
app.register_blueprint(views.dashboard_blueprint)

@app.route('/')
def home():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run(debug=True)