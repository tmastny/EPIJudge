import threading

odd_ready = threading.Event()
even_ready = threading.Event()

def print_odds():
    for i in range(1, 50 + 1):
        odd_ready.wait()
        print(2 * i - 1)
        odd_ready.clear()
        
        even_ready.set()

def print_evens():
    odd_ready.set()
    
    for i in range(1, 50 + 1):
        even_ready.wait()
        print(2 * i)
        even_ready.clear()
        
        odd_ready.set()

t1 = threading.Thread(target=print_odds)
t2 = threading.Thread(target=print_evens)

t1.start()
t2.start()
t1.join()
t2.join()
