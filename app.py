from flask import flask,render_template,request
from text_summary import summarizer

app = flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
