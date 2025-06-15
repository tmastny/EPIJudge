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
class SpellCheckService :
    w_last = closest_to_last_word = None
    semaphore = Semaphore()

    @staticmethod
    def service(req, resp) :
        w = req.extract_word_to_check_from_request()

        semphaore.acquire()
        if w != SpellCheckService.w_last:
            SpellCheckService.w_last = w
            SpellCheckService.closest_to_last_word = closet_in_dictionary(w)

        resp.encode_into_response(SpellCheckService.closest_to_last_word)
        semphaore.release()
        
class SpellCheckService :
    w_last = closest_to_last_word = None
    lock = threading.lock()

    @staticmethod
    def service(req, resp) :
        w = req.extract_word_to_check_from_request()

        result = None
        with SpellCheckService.lock:
            if w == SpellCheckService.w_last:
                result = SpellCheckService.closest_to_last_word.copy()
        
        if not result:
            result = SpellCheckService.closet_in_dictionary(w)
            with SpellCheckService.lock:
                SpellCheckService.w_last = w
                SpellCheckService.closest_to_last_word = result
                
        resp.encode_into_response(result)

