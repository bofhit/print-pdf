import dotenv
import os

from flask import Flask, redirect, render_template, request

app = Flask(__name__)

# Load variables from .env
dotenv.load_dotenv()

FLASK_PORT = os.environ['FLASK_PORT']

@app.route('/name-tag', methods=['GET', 'POST'])
def print_name_tag():
    """Print a name tag."""

    if request.method == 'GET':
        return render_template('template.html')

    if request.method == 'POST':
        return redirect('/name-tag')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=FLASK_PORT)
    
