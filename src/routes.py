from flask import Blueprint, render_template


site= Blueprint("site", __name__)


@site.route("/")
@site.route("/home")
def home():
    return render_template(
        "index.html",
        view="home.html"
    )

@site.route("/gallery")
def gallery():
    return render_template(
        "index.html",
        view="gallery.html"
    )

@site.route("/store")
def store():
    return render_template(
        "index.html",
        view="store.html"
    )

@site.route("/inquire")
def inquire():
    return render_template(
        "index.html",
        view="inquire.html"
    )