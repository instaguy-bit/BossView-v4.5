# Flask app entry point
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home(): return 'BossView 4.5 Running'