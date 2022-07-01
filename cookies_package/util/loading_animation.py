import itertools
import threading
import time
import sys
 
def animate_loading(method):
    def animated():
        done = False
        def animate():
            time.sleep(0.000001)
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\r Loading ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\r Done!       ')
            
        t = threading.Thread(target=animate)
        t.start()
 
        method()
        done = True
    return animated