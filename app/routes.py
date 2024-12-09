from flask import render_template, request
from app import app  # Import the `app` instance from __init__.py
from app.bottleneck import analyze_code

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        code = request.form['code']
        result = analyze_code(code)
        return render_template('results.html', code=code, result=result)
    return render_template('index.html')
