FROM blang/latex
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY app /
WORKDIR /
RUN pip install -r requirements.txt
EXPORT FLASK_APP=app.py
CMD flask run --port=6780 --host=0.0.0.0