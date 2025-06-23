"""
Min: 1_000_000
  * thread 1 reads 0, calculates counter + 1 == 0
    * thread 1 suspends
  * thread 2 resumes
    * calculates and saves all increments
  * thread 1 resumes
    * saves counter == 1 and finishes
  * final result will be N == 1_000_000

Max: 2_000_000
  * threads do not suspend after adding but before saving
"""
import threading

N = 1_000_000
counter = 0

def increment_thread():
    global counter
    for _ in range(N):
        counter = counter + int(1)

t1 = threading.Thread(target=increment_thread)
t2 = threading.Thread(target=increment_thread)

t1.start()
t2.start()
t1.join()
t2.join()

print(counter)