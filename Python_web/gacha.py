
from flask import Flask, render_template
import os

print(os.getcwd())
print(os.listdir(os.path.join(os.getcwd(), 'templates')))

app = Flask(__name__)

@app.route('/')
def about():
    return render_template('about.html')
@app.home('/')
def HSR():
    return render_template('home.html')

@app.route('/button-click', methods=['Post'])
def handle_button_click():
    # In this function I will add use URL
    print("Button clicked!")
    return "Button clicked"

if __name__ == '__main__':
    app.run()