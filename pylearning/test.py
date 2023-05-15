from datetime import datetime

now = datetime.now()
print(now)

def oneup():
    global x
    x = x + 1
    return x

x = 0
print(oneup())
print(oneup())
