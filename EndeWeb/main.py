from flask import Flask, render_template, request
import subprocess
import os
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/encode')
def encode():
    data = request.args.get('data')
    encoding_type = request.args.get('encode')
    type = encoding_type
    if not data:
        return render_template('input.html', type=type, encoding_result=None, action='encode')
    else:
        script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Ende.sh'))
        try:
            encoding_result = subprocess.run([script_path, '-e', type, data], capture_output=True, text=True, check=True)
            output = encoding_result.stdout
        except subprocess.CalledProcessError as e:
            output = f"Error: {e.stderr}"
        except FileNotFoundError:
            output = f"Error: {script_path} not found"
        return render_template('encode.html', encoding_type=encoding_type, encoding_result=output, data=data)

@app.route('/decode')
def decode():
    data = request.args.get('data')
    decoding_type = request.args.get('decode')
    type = decoding_type
    if not data:
        return render_template('input.html', type=type, action='decode')
    else:
        script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Ende.sh'))
        try:
            decoding_result = subprocess.run([script_path, '-d', decoding_type, data], capture_output=True, text=True, check=True)
            output = decoding_result.stdout
        except subprocess.CalledProcessError as e:
            output = f"Error: {e.stderr}"
        except FileNotFoundError:
            output = f"Error: {script_path} not found"
        return render_template('decode.html', decoding_type=decoding_type, decoding_result=output, data=data)

if __name__ == '__main__':
    app.run(debug=True)