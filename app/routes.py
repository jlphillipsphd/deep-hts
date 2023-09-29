from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/model_interface')
def model_interface():
    return render_template('model_interface.html')

@app.route('/documentation')
def documentation():
    return render_template('documentation.html')

@app.route('/faqs')
def faqs():
    return render_template('faqs.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')
