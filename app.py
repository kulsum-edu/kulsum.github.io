from flask import Flask, render_template, request
from color_suggester import get_outfit_colors

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    skin = request.form['skin_tone']
    event = request.form['event_type']
    colors = get_outfit_colors(skin, event)
    return render_template('index.html', result=colors)

if __name__ == '__main__':
    app.run(debug=True)
