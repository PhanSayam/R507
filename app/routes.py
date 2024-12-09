from app import app

@app.route("/")
def home():
    return "Hello, CI/CD with Canary Deployment!"
