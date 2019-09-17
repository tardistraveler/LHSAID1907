import time


list01 = [item for item in range(10 * 5 + 1)]
# print(list01)
st = time.time()
list01.insert(1, '007')
print('time:', time.time() - st)
