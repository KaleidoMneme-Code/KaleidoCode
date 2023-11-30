import threading

class Create_Thread(threading.Thread):
    def __init__(self, target, args=None):
        self._stop_event = threading.Event()
        self.name = threading.Thread.__init__(self, target=target, args=(args))

    def Begin(self):
        self._stop_event = threading.Event()
        return self._stop_event
    
    def Stop(self):
        self._stop_event.set()

    def Stopped(self):
        return self._stop_event.is_set()

