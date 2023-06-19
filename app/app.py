import dotenv
import os

from flask import Flask, redirect, render_template, request

from make_pdf import make_pdf

app = Flask(__name__)

# Load variables from .env
dotenv.load_dotenv()

FLASK_PORT = os.environ['FLASK_PORT']
PDF_OUTPATH = os.environ['PDF_OUTPATH']

@app.route('/name-tag', methods=['GET', 'POST'])
def print_name_tag():
    """Print a name tag."""

    if request.method == 'GET':
        return render_template('template.html')

    if request.method == 'POST':
        name = request.form.get('name-tag-name')
        print(name)
        make_pdf('my_pdf.pdf', name=name)
        return redirect('/name-tag')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=FLASK_PORT)
    
