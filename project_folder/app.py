from flask import Flask, render_template
import views

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('dashboard.html')

@app.route('/analyse', methods=['POST'])
def analyse():
    codebase = request.form['codebase']
    improvements = views.analyse_codebase(codebase)
    return render_template('dashboard.html', improvements=improvements)

if __name__ == "__main__":
    app.run(debug=True)