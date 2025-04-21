# ====================================================================

#        CryptPaste
# The open-source Pastebin alternative
# Under the GPL v3 license

# ====================================================================

from flask import Flask, render_template, request,redirect, flash
import os
import shared
import db


app = Flask(__name__, template_folder="html", static_folder="static")
app.secret_key = os.urandom(24)  

@app.route('/')
def index():
    return render_template('index.html')
@app.context_processor
def context_processor():
    return dict(config=shared.config_json["app"])

# load routes
from routes import view,api
app.register_blueprint(view.bp)
app.register_blueprint(api.bp)

# Recommend to run with Gunicorn
if shared.config_json["http"]["debug"]:


    print("Hey, the debug server is not for production, use gunicorn instead")
    print("Disable debug mode in the config.json")

    app.run(host=shared.config_json["http"]["host"], port=shared.config_json["http"]["port"], debug=shared.config_json["http"]["debug"])