#!/bin/bash
source ./venv/bin/activate
export FLASK_APP=app.py
flask run --port=6780 --host=0.0.0.0