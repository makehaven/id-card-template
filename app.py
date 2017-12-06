import os
import tempfile
from flask import Flask, render_template, request, make_response, send_file, after_this_request
app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('tmp')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload():
    print(request.files, request.form)
    file = request.files['image']
    first = request.form['first'].upper()
    last = request.form['last'].upper()
    
    tmp = tempfile.mkdtemp()
    print(tmp)

    @after_this_request
    def cleanup(response):
        os.system('rm -rf {}'.format(tmp))
        return response

    filename = os.path.join(tmp, 'photo.jpg')
    file.save(filename)

    with open(os.path.join(tmp, 'front.tex'), 'w') as of:
    	tex = open('front.tex', 'r').read()
    	tex = tex.replace('FIRSTNAME', first)
    	tex = tex.replace('LASTNAME', last)
    	of.write(tex)

    os.system('cp idcard_back.pdf {}'.format(tmp))
    os.system('cp idcard.tex {}'.format(tmp))
    os.system('./generate.sh {}'.format(tmp))

    return send_file(os.path.join(tmp, 'idcard.pdf'))