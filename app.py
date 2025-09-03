"""
Main initialization file for StudyPlan AI
"""
from app.main import app
import os

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    print(f"🚀 Starting StudyPlan AI on port {port}...")
    print(f"📍 Access: http://localhost:{port}")
    app.run(host="0.0.0.0", port=port, debug=True)
