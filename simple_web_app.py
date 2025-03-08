from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
    <html>
        <head>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    font-size: 36px;
                    font-weight: bold;
                    text-align: center;
                    margin-top: 20%;
                }
            </style>
        </head>
        <body>
            Hello, World! Roman has long hair and a tail
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
