from app import app
import time
# timeout nodig om mariadb op te starten
time.sleep(10)

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
