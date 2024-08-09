from queue import Queue 

n =  int (input ("Enter the Size of Queue :"))

q = Queue(n)

q.put('w')

q.put(3)

print (q.get())
print (q.get())

print(q.qsize())

print (q.empty())

print (q.full())