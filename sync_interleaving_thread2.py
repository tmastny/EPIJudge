import threading

class OddEvenCondition(threading.Condition):
    EVEN = True
    ODD = False

    def __init__(self):
        super().__init__()
        self.turn = self.ODD

    def thread_wait(self, turn):
        with self:
            if self.turn != turn:
                self.wait()

    def thread_done(self, turn):
        with self:
            self.turn = not turn
            self.notify_all()

def print_odds():
    for i in range(1, 50 + 1):
        cond.thread_wait(OddEvenCondition.ODD)
        print(2 * i - 1)
        cond.thread_done(OddEvenCondition.ODD)


def print_evens():
    for i in range(1, 50 + 1):
        cond.thread_wait(OddEvenCondition.EVEN)
        print(2 * i)
        cond.thread_done(OddEvenCondition.EVEN)

cond = OddEvenCondition()
t1 = threading.Thread(target=print_odds)
t2 = threading.Thread(target=print_evens)

t1.start()
t2.start()
t1.join()
t2.join()
