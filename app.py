from flask import Flask, render_template
from base_bp.routes import base_bp

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

@app.route('/')
def home():
    return render_template('index.html')

app.register_blueprint(base_bp)

if __name__ == '__main__':
    app.run(debug=True)
