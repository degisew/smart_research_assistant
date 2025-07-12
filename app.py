from flask import Flask, jsonify, request, render_template

from agents.linkedin_lookup import get_user_summary

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    data = get_user_summary(name)
    return jsonify(
        {
            "summary_and_facts": data.to_dict(),
        }
    )


if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)
