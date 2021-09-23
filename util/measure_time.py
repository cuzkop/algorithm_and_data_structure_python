import time

def measure(func):
    def inner(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(f"{(t2 - t1):.8f}s")
        return result
    return inner

# def snooze():
#     time.sleep(1)

# @time_decorator
# def naptime():
#     snooze()

# naptime()