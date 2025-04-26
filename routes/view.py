# ====================================================================

#        CryptPaste
# The open-source Pastebin alternative
# Under the GPL v3 license

# ====================================================================


from flask import render_template, request, redirect, flash, url_for, jsonify, session, Blueprint,make_response
import shared
import db
import html

import time

bp = Blueprint('view', __name__, url_prefix='/')

@bp.route('/view')
def view_paste():
    temp_session = db.get_session()
    try:
        paste_id = request.args.get('id')
        paste_text = "Paste not found"
        paste = temp_session.query(db.Paste).filter_by(pid=paste_id).first()
        if paste is None:
            paste_text = "Paste not found"
        else:
            paste_text = paste.content
        paste_text += f'''

======== PASTE INFO ========

Paste ID : {paste_id}
Date : {time.ctime(paste.date)}
Raw URL : /raw/{paste_id}'''
        #paste_text = html.escape(paste_text) >> DISABLED TEMP
        return render_template('view.html',paste_text=paste_text)
    except Exception as e:
        return "Error: " + str(e)
    finally:
        temp_session.close()

@bp.route('/raw/<paste_id>')
def raw_paste(paste_id):
    WITH_INFO = False
    if request.args.get('with_info') is not None:
        WITH_INFO = True
    temp_session = db.get_session()
    try:
        paste = temp_session.query(db.Paste).filter_by(pid=paste_id).first()
        if paste is None:
            return make_response("not found", 200, {'Content-Type': 'text/plain'})
        paste_text = paste.content
        if WITH_INFO:
            paste_text += f'''

======== PASTE INFO ========

Paste ID : {paste_id}
Date : {time.ctime(paste.date)}
Raw URL : /raw/{paste_id}'''
        return make_response(paste_text, 200, {'Content-Type': 'text/plain'})
    except Exception as e:
        return "error", 500
    finally:
        temp_session.close()
