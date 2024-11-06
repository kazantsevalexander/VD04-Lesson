from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def current_datetime_view():
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    return f"Текущая дата и время: {formatted_datetime}"

if __name__ == "__main__":
    app.run()