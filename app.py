from flask import Flask, render_template,request
import  model

app = Flask(__name__)

@app.route("/")
def hello():
    return  render_template("index.html")


@app.route("/sub", methods=['POST'])
def submit():
    if request.method == "POST":
        density=request.form["density"]
        breast=request.form["breast"]
        view=request.form["view"]
        massShape=request.form["massShape"]
        massMargins=request.form["massmargins"]
        abnormality=request.form["abnormality"]
        assessment=request.form["assessment"]
        subtlety=request.form["subtlety"]

    return render_template("sub.html",n = model.result(density,breast,view,abnormality,massShape,massMargins,assessment,subtlety))


if __name__  == "__main__":
    app.run(debug=True)