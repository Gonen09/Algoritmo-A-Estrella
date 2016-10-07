import threading
import time


def worker():
    print threading.currentThread().getName(), 'Lanzado'
    time.sleep(2)
    print threading.currentThread().getName(), 'Deteniendo'


def servicio():
    print threading.currentThread().getName(), 'Lanzado'
    print threading.currentThread().getName(), 'Deteniendo'

    
t = threading.Thread(target=servicio, name='Servicio')
w = threading.Thread(target=worker, name='Worker')
z = threading.Thread(target=worker)

w.start()
z.start()
t.start()
