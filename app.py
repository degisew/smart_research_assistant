from flask import Flask, Response, jsonify, request, render_template
from chains.llm_chain import generate_company_summary

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process() -> Response:
    company_name: str = request.form["company_name"]
    data = generate_company_summary(company_name)

    return jsonify(
        {
            "parsed_data": data.to_dict(),
        }
    )


if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)
