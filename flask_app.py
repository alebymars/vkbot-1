#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, json
from settings import *
import messageHandler

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello from Flask!'


@app.route('/', methods=['POST'])
def processing():
    data = json.loads(request.data)
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        messageHandler.create_answer(data['object'], token)
        return 'ok'


if __name__ == "__main__":
    app.run("0.0.0.0")
