import time

def fibrilator(x):
    if x<2: return x
    else: return fib(x-1) + fib(x-2)

i = time.time()

print fibrilator(32)
print time.time()-i
