
from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()
    return f"""
    <html>
        <head>
            <title>Docker Python App</title>
            <style>
                body {{
                    font-family: Arial;
                    text-align: center;
                    background: #eef2f7;
                    padding-top: 100px;
                }}
                .card {{
                    background: white;
                    padding: 35px;
                    margin: auto;
                    max-width: 500px;
                    border-radius: 12px;
                }}
                h1 {{ color: #2563eb; }}
            </style>
        </head>
        <body>
            <div class="card">
                <h1>Dockerized Python Web Application</h1>
                <p>Hello! My Flask application is running.</p>
                <p><b>Container Hostname:</b> {hostname}</p>
                <p>Project Status: Successfully Running</p>
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
