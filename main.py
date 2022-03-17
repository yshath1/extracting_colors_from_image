import os
import extcolors
from flask import Flask, render_template, redirect, url_for, flash, abort, request
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage


UPLOAD_FOLDER = 'static/Uploaded/'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route('/',methods=['GET', 'POST'])
def upload_files():
    return render_template("up.html")


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        img_name=secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
        colors,pixel_count=extcolors.extract_from_path(f"static/Uploaded/{img_name}")
        rgb_colors=[]
        for x in colors:
            print(x[0])
            rgb_colors.append(x[0])

        print(len(rgb_colors))
        return render_template("display.html",colors=rgb_colors)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
