# ====================================================================

#        CryptPaste
# The open-source Pastebin alternative
# Under the GPL v3 license

# ====================================================================


from flask import render_template, request, redirect, flash, url_for, jsonify, session, Blueprint
import shared
import db
import uuid
import time


bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/paste/new', methods=['POST'])
def new_paste():
    temp_session = db.get_session()
    try:
        paste_id = str(uuid.uuid4())
        content = request.json.get('content')
        if content is None:
            return jsonify({"status": "error", "error": "No content provided"})
        x = db.Paste(pid=paste_id, content=content, is_password_protected=0, date=int(time.time()))
        temp_session.add(x)
        temp_session.commit()
        return jsonify({"url": "/view?id=" + paste_id,"status": "success"})
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        temp_session.close()

@bp.route('/recent')
def recent_pastes():
    temp_session = db.get_session()
    try:
        pastes = temp_session.query(db.Paste).order_by(db.Paste.date.desc()).limit(50).all()
        return jsonify([{"id": paste.pid, "date": time.ctime(paste.date), "url": "/view?id=" + paste.pid, "raw": "/raw/" + paste.pid} for paste in pastes])
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        temp_session.close()

