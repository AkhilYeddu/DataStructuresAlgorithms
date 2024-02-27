# QUEUE is a FIFO object
queue=[]

queue.append("a")
queue.append("b")
queue.append("c")

print(queue)
print(len(queue)) #to check the size of the queue

# to search an object
try:
    obj="c"
    pos=queue.index(obj)
    if obj in queue:
        print(obj,"is in index",pos)
except ValueError:
    print("the",obj,"is not found in the queue")        
    

while queue:
    print(queue.pop(0)) #removed every element
print(queue)

if not queue:
    print("empty")
else:
    print("notempty")    