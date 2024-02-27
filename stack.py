stack=[] #declaring a list
# stack is a LIFO data structure. Last-in First-out

#push operation
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
stack.append("akhil")

# to check a stack is empty or not
if not stack:
    print("empty")
else:
    print("notempty") 

search="akhil"
print(stack)
pos=stack.index(search)
if search in stack:
    print(search,"is found at index ",pos)  

   #remove the top element 
top_el=stack.pop()
stack.pop(0)   # remove the element corresponding to its index    

print(stack)
print("top element=",top_el)

print("popped last element")
print("popped first element")      

