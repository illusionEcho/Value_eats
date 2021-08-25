#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@Date :2021/08/25 00:32:32
@Author :AaronRen
@version :1.0
'''

import os
from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app

# Initialize Flask app
app = Flask(__name__)





port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)