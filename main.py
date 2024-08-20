from Flask import Flask, render_template # type: ignore
import utils.spotify_client as spotify_client

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8888)