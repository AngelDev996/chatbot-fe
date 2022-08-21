from flask import Flask, render_template, request, jsonify
from chat import get_response
import os

IMG_FOLDER = os.path.join('static', 'images')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMG_FOLDER

@app.get("/")
def index_get():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'banhn.png')
    full_filename2 = os.path.join(app.config['UPLOAD_FOLDER'],  'robot.jpg')
    return render_template("index.html", user_image=full_filename, user_image2=full_filename2)


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)
