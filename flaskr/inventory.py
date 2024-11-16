from flask import Blueprint, g, flash, redirect, render_template, request, url_for
from werkzeug.exceptions import abort
from flaskr.db import get_db
from . import auth

bp = Blueprint("inventory", __name__, url_prefix="/inventory")


def get_item(id):
    item = get_db().execute("SELECT * FROM items WHERE id = ?", (id,)).fetchone()

    if item is None:
        abort(404, f"Item id {id} doesn't exist.")

    return item


@bp.route("/")
@auth.login_required
def index():
    db = get_db()
    item_type_filter = request.args.get("item_type")

    # Récupérer les différents item_type
    item_types = db.execute("SELECT DISTINCT item_type FROM items WHERE user_id = ?", (str(g.user["id"]),)).fetchall()

    # Filtrer les items en fonction du item_type sélectionné
    if item_type_filter:
        items = db.execute(
            "SELECT * FROM items WHERE user_id = ? AND item_type = ?", (str(g.user["id"]), item_type_filter)
        ).fetchall()
    else:
        items = db.execute(
            "SELECT * FROM items WHERE user_id = ?", (str(g.user["id"]),)
        ).fetchall()

    return render_template("inventory/index.html", items=items, item_types=item_types, selected_item_type=item_type_filter)


@bp.route("/create", methods=["GET", "POST"])
@auth.login_required
def create():
    if request.method == "POST":
        item_type = request.form["item_type"]
        item_name = request.form["item_name"]
        item_quantity = request.form["item_quantity"]
        user_id = g.user["id"]  # Récupère l'ID de l'utilisateur connecté
        error = None
        
        if not item_type:
            error = "Item type is required."
        if not item_name:
            error = "Item name is required."
        elif not item_quantity:
            error = "Item quantity is required."

        if error is not None:
            flash(error, "error")
        else:
            db = get_db()
            db.execute(
                "INSERT INTO items (item_type, item_name, item_quantity, user_id) VALUES (?, ?, ?, ?)",
                (item_type, item_name, item_quantity, user_id),
            )
            db.commit()
            return redirect(url_for("inventory.index"))

    return render_template("inventory/create.html")


@bp.route("/<int:id>", methods=("GET", "POST"))
@auth.login_required
def view(id):
    item = get_item(id)

    if request.method == "POST":
        item_type = request.form["item_type"]
        item_name = request.form["item_name"]
        item_quantity = request.form["item_quantity"]
        error = None

        if not item_type:
            error = "Type is required."
        
        if not item_name:
            error = "Name is required."

        if not item_quantity:
            error = "Quantity is required."
            

        if error is not None:
            flash(error, "error")
        else:
            db = get_db()
            db.execute(
                "UPDATE items SET item_type = ?, item_name = ?, item_quantity = ? WHERE id = ?",
                (item_type,item_name, item_quantity, id),
            )
            db.commit()
            return redirect(url_for("inventory.index"))

    return render_template("inventory/view.html", item=item)


@bp.route("/<int:id>", methods=["DELETE"])
@auth.login_required
def delete(id):
    print(f"Received ID: {id}")  # Vérifie l'ID reçu dans la console
    item = get_item(id)
    if item is None:
        return "Item not found", 404

    db = get_db()
    db.execute("DELETE FROM items WHERE id = ?", (id,))
    db.commit()

    return "", 200
