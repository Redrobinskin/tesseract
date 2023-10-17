from flask import render_template

def dashboard_view():
    try:
        return render_template('dashboard.html')
    except Exception as e:
        print(f"An error occurred: {e}")
        return render_template('error.html', error=e)