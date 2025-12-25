import os
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)
DATA_PATH = os.path.join("data", "out.csv")

df = pd.read_csv(DATA_PATH)


@app.route("/")
def index():
    mkb_list = sorted(df["МКБ-10"].dropna().unique())
    return render_template("index.html", mkb_list=mkb_list)


@app.route("/search")
def search():
    code = request.args.get("code", "").strip()
    if not code:
        results = []
    else:
        results = df[df["МКБ-10"].str.contains(f"^{code}", na=False, regex=False)]
        results = results.to_dict(orient="records")
    return render_template("search.html", code=code, results=results)


if __name__ == "__main__":
    app.run(debug=True)
