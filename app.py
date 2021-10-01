from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signup_form")
def signup_form():
    return render_template("signup.html")


@app.route("/thankyou")
def thankyou():
    uppercase_letter = False
    lowercase_letter = False
    ends_with_num = False
    meets_reqs = False

    username = request.args.get("username")

    uppercase_letter = any(letter.islower() for letter in username)
    lowercase_letter = any(letter.isupper() for letter in username)
    ends_with_num = username[-1].isdigit()

    if lowercase_letter and ends_with_num and uppercase_letter:
        meets_reqs = True

    return render_template(
        "thankyou.html",
        uppercase_letter=uppercase_letter,
        lowercase_letter=lowercase_letter,
        ends_with_num=ends_with_num,
        meets_reqs=meets_reqs,
    )


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
