from flask import Flask, request, render_template
from .bot import analyze_code

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    findings, suggestions = [], ""
    if request.method == "POST":
        code = request.form.get("code")
        findings, suggestions = analyze_code(code)
    return render_template("index.html", findings=findings, suggestions=suggestions)

if __name__ == "__main__":
    app.run(debug=True)
