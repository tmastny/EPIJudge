import threading
from threading import Semaphore
"""
The issue is the race condition between checking the new word against `w_last`
and returning the `closest_to_last_word` response.

For example, if there are two concurrent requests, thread 1 could check
if `w == w_last` and suppose that is true.

Next, thread 1 could suspend and thread 2 could check if `w == w_last`.
Suppose this time it is false. Then thread 2 would fetch the
closest_in_dictionry(w) and save that to closet_to_last_word.

If thread 2 suspends and thread 1 resumes, thread 1 will proceed to
encode `closet_to_last_word` into the response from thread 2's word!
"""
def closet_in_dictionary(word):
    pass

class SpellCheckServiceOld:
    w_last = closest_to_last_word = None
    semaphore = Semaphore()

    @staticmethod
    def service(req, resp) :
        w = req.extract_word_to_check_from_request()


        SpellCheckServiceOld.semaphore.acquire()
        if w != SpellCheckServiceOld.w_last:
            SpellCheckServiceOld.w_last = w
            SpellCheckServiceOld.closest_to_last_word = closet_in_dictionary(w)

        resp.encode_into_response(SpellCheckServiceOld.closest_to_last_word)
        SpellCheckServiceOld.semaphore.release()


class SpellCheckService:
    w_last = closest_to_last_word = None
    lock = threading.Lock()

    @staticmethod
    def service(req, resp) :
        w = req.extract_word_to_check_from_request()

        result = None
        with SpellCheckService.lock:
            if w == SpellCheckService.w_last:
                result = SpellCheckService.closest_to_last_word.copy()

        if not result:
            result = closet_in_dictionary(w)
            with SpellCheckService.lock:
                SpellCheckService.w_last = w
                SpellCheckService.closest_to_last_word = result

        resp.encode_into_response(result)

class CriticalService:
    lock = threading.Lock()
    condition = threading.Condition(lock)
    n = 10
    nrendezvous = 0

    @staticmethod
    def critical():
        pass

    @staticmethod
    def rendezvous():
        pass

    @staticmethod
    def service():
        CriticalService.rendezvous()

        with CriticalService.condition:
            CriticalService.nrendezvous += 1
            if CriticalService.nrendezvous == CriticalService.n:
                CriticalService.nrendezvous = 0
                CriticalService.condition.notify_all()
            else:
                CriticalService.condition.wait()

        with CriticalService.lock:
            CriticalService.critical()


class CriticalServiceBarrier:
    lock = threading.Lock()
    n = 10
    barrier = threading.Barrier(n)

    @staticmethod
    def critical():
        pass

    @staticmethod
    def rendezvous():
        pass

    @staticmethod
    def service():
        CriticalServiceBarrier.rendezvous()
        CriticalServiceBarrier.barrier.wait()

        with CriticalService.lock:
            CriticalService.critical()
