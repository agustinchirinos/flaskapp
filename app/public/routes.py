from flask import render_template, request

import app
from . import public



@public.route('/', methods=["GET","POST"])
def index():  # put application's code here
    msg = ""
    if request.method == "POST":
        msg = request.form.get("msg")
    return render_template('index.html', msg=msg)
