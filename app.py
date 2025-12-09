from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/over-mij")
def over_mij():
    return render_template("over-mij.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/flex-grid")
def flex_grid():
    return render_template("flex-grid.html")


if __name__ == "__main__":
    app.run(debug=True)
