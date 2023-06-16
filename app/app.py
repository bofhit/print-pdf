import dotenv
import os

from flask import Flask

app = Flask(__name__)

# Load variables from .env
dotenv.load_dotenv()

FLASK_PORT = os.environ['FLASK_PORT']

@app.route('/')
def hello():
    return "Hello World!"
  
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=FLASK_PORT)
    
