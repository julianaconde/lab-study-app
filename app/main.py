"""
Main StudyPlan AI application - Simplified version with Flask only
"""
import os
from pathlib import Path
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# Importing application components
from app.api.api import api_bp

# Load environment variables
root_env = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=root_env if root_env.exists() else None)

# Configuring Flask application
app = Flask(__name__, 
           template_folder=str(Path(__file__).parent / "templates"),
           static_folder=str(Path(__file__).parent / "static"))

# Registering the API blueprint
app.register_blueprint(api_bp, url_prefix='/api')

@app.route("/")
def index():
    return render_template("index.html")

# Configuring CORS to allow requests from any origin
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    print(f"🚀 Starting StudyPlan AI on port {port}...")
    print(f"📍 Access: http://localhost:{port}")
    app.run(host="0.0.0.0", port=port, debug=True)
