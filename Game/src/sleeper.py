import time


class sleeper:
    @staticmethod
    def sleep(checks:dict,seconds:int):
        time.sleep(seconds)
        checks["sleep_finished"] = True
