
from flask import Flask, render_template,request
import uuid
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'user_uploads'
ALLOWED_EXTENSIONS = { 'pdf', 'png', 'jpg', 'jpeg'}
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods = ["GET","POST"])
def create():
    myid = uuid.uuid1()
    if request.method == "POST":
        # Handle file upload and reel creation logic here
        print(request.files.keys())
        res_id = request.form.get("uuid")
        des = request.form.get("text")
        Input_files = []
        for key,value in request.files.items():
            print(key,value)
            # upload the file
            file = request.files[key]
            if file:
                filename = secure_filename(file.filename)
                if (not(os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'],res_id)))) :
                        os.mkdir (os.path.join(app.config['UPLOAD_FOLDER'],res_id))
                        file.save(os.path.join(app.config['UPLOAD_FOLDER'],res_id, filename))
                        Input_files.append(file.filename) 
                        with open(os.path.join(app.config['UPLOAD_FOLDER'],res_id,"des.txt"),"w") as f:
                            f.write(des)
        for fl in Input_files:
          with open(os.path.join(app.config['UPLOAD_FOLDER'],res_id,"input.txt"),"a") as f:
              f.write(f"file '{fl}'\n duration 10\n")
    return render_template("create.html",myid=myid)

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

app.run(debug=True)