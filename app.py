
from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import numpy as np
import os
from keras.utils import to_categorical
from werkzeug.utils import secure_filename
from keras.models import Sequential, load_model
from tensorflow.keras.models import model_from_json
import h5py
import urllib.request
import librosa


app = Flask(__name__)


@app.route('/')
def index():
	return render_template('upload.html')

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    port = int(os.environ.get('PORT', 5000))
    app.run(threaded=True, port=port)
