from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
	return 'Bot is aLive!'

def run():
    app.run(host="0.0.0.0", port=8000)

def keep_alive():
    server = Thread(target=run)
    server.start()

if __name__ == "__main__":
    from gevent import pywsgi
    server = pywsgi.WSGIServer(('0.0.0.0', 8000), app)
    server.serve_forever()