from flask import Flask
from flask import render_template

#Объект программы
app_cosmo = Flask(__name__)


#Запросы
@app_cosmo.route("/")
def main_page():
    return render_template("index.html")


@app_cosmo.route("/about")
def about_page():
    return render_template("about.html")


@app_cosmo.route("/faq")
def faq_page():
    return render_template("faq.html")


if __name__ == "__main__":
    app_cosmo.run()

