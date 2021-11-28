import queue 

q = queue.Queue()
q.put(1)
q.put(2)
q.put(3)

print(q.get())
print(q.get())
print(q.get())