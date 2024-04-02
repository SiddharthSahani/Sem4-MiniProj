# create flask server
import flask as f

app = f.Flask(__name__)


@app.route('/')
def hello():
    return f.render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

