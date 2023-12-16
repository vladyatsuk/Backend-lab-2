from my_app import app
from flask import jsonify
from datetime import datetime

@app.route('/healthcheck')
def healthcheck():
    current_time = datetime.now().isoformat()
    status = "OK"

    response_data = {
        "status": status,
        "timestamp": current_time
    }

    return response_data, 200
