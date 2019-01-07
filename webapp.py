import os
import logging
from datetime import datetime, timedelta
from flask import Flask, request, abort, jsonify , render_template

def temp_token():
    import binascii
    temp_token = binascii.hexlify(os.urandom(24))
    return temp_token.decode('utf-8')

logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger()
rootLogger.setLevel(logging.DEBUG)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)

WEBHOOK_VERIFY_TOKEN = os.getenv('WEBHOOK_VERIFY_TOKEN')
CLIENT_AUTH_TIMEOUT = 24 # in Hours

app = Flask(__name__)

@app.route('/get_token', methods=['GET'])
def get_token_webhook():
    rootLogger.info(request.remote_addr + "on method : " + request.method)
    if request.method == 'GET':
        return render_template('token.html',get_token=WEBHOOK_VERIFY_TOKEN , times=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    else:
        abort(400)

if __name__ == '__main__':
    if WEBHOOK_VERIFY_TOKEN is None:
        print('WEBHOOK_VERIFY_TOKEN has not been set in the environment.\nGenerating random token...')
        token = temp_token()
        print('Token: %s' % token)
        print('You can get token flag on $[URL]:5000/get_token')
        WEBHOOK_VERIFY_TOKEN = token
    app.run(host='0.0.0.0') #default allow on port 5000.