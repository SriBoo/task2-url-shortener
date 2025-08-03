

from flask import Flask, render_template, request, redirect, flash
from app.models import url_mapping
from app.utils import generate_short_id

app = Flask(__name__)
app.secret_key = 'retainsecret' 

@app.route("/", methods=["GET", "POST"])
def index():
    shortened_url = None
    if request.method == "POST":
        original_url = request.form.get("original_url")

        if not original_url:
            flash("URL cannot be empty", "error")
            return render_template("index.html")

        short_id = generate_short_id()
        url_mapping[short_id] = original_url
        shortened_url = request.host_url + "api/" + short_id

    return render_template("index.html", shortened_url=shortened_url)

@app.route("/api/<short_id>")
def redirect_to_url(short_id):
    original_url = url_mapping.get(short_id)
    if original_url:
        return redirect(original_url)
    else:
        return "Invalid short URL", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
