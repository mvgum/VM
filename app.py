import os

from flask import Flask, render_template, send_from_directory, abort

root_dir = os.path.dirname(os.path.abspath(__file__))
template_folder = os.path.join(root_dir, "templates")
static_folder = os.path.join(root_dir, "static")

app = Flask(__name__, template_folder=template_folder)

@app.route("/")
def index():
    return render_template("index.html")

# Универсальный endpoint для статики
@app.route("/static/<path:filename>")
def send_static(filename):
    # Проверяем, что файл существует
    file_path = os.path.join(static_folder, filename)
    if not os.path.exists(file_path):
        abort(404)
    return send_from_directory(static_folder, filename)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
