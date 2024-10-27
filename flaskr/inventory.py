from flask import Blueprint, flash, redirect, render_template, request, url_for
from werkzeug.exceptions import abort
from flaskr.db import get_db

bp = Blueprint("inventory", __name__)


@bp.route("/")
def index():
    db = get_db()
    items = db.execute("SELECT * FROM items").fetchall()
    return render_template("inventory/index.html", items=items)


@bp.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        item_name = request.form["item_name"]
        item_quantity = request.form["item_quantity"]
        error = None

        if not item_name:
            error = "Name is required."

        if not item_quantity:
            error = "Quantity is required."

        if error is not None:
            flash(error, "error")
        else:
            db = get_db()
            db.execute(
                "INSERT INTO items (item_name, item_quantity) VALUES (?, ?)",
                (item_name, item_quantity),
            )
            db.commit()
            return redirect(url_for("inventory.index"))
    return render_template("inventory/create.html")


def get_item(id):
    item = get_db().execute("SELECT * FROM items WHERE id = ?", (id,)).fetchone()

    if item is None:
        abort(404, f"Item id {id} doesn't exist.")

    return item


@bp.route("/edit/<int:id>", methods=("GET", "POST"))
def edit(id):
    item = get_item(id)

    if request.method == "POST":
        item_name = request.form["item_name"]
        item_quantity = request.form["item_quantity"]
        error = None

        if not item_name:
            error = "Name is required."

        if not item_quantity:
            error = "Quantity is required."

        if error is not None:
            flash(error, "error")
        else:
            db = get_db()
            db.execute(
                "UPDATE items SET item_name = ?, item_quantity = ? WHERE id = ?",
                (item_name, item_quantity, id),
            )
            db.commit()
            return redirect(url_for("inventory.index"))

    return render_template("inventory/edit.html", item=item)


@bp.route("/delete/<int:id>", methods=["DELETE"])
def delete(id):
    get_item(id)
    db = get_db()
    db.execute("DELETE FROM items WHERE id = ?", (id,))
    db.commit()

    return "", 200
