import datetime as dt
import time

elapsedTime = dt.datetime(1,1,1)
print("toàn số 0------", elapsedTime)

PC = dt.datetime(1,1,1).now()
print("PC----", PC)

t = time.localtime()
Zeros = dt.timedelta(hours=t[3], minutes=t[4], seconds=t[5])
print("zero time------", Zeros)

# zeroTime = PC - elapsedTime
# print("abc-----", zeroTime)

elapsedtime = PC - Zeros
print("-----", elapsedtime)

