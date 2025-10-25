import threading
import webbrowser
import time
from waitress import serve
import app  # tu archivo app.py

def open_browser():
    time.sleep(1)  # Espera un segundo para que el servidor arranque
    webbrowser.open('http://127.0.0.1:5000/')

if __name__ == '__main__':
    # Abrir navegador en un hilo separado
    threading.Thread(target=open_browser).start()
    # Ejecutar servidor Waitress
    serve(app.app, host='127.0.0.1', port=5000)
