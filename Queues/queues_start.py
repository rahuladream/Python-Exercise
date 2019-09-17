'''
Collection that support adding and removing items
LIFO

Example:
Order Processing, Messaging
'''
from collection import deque

queue = deque()

# Inserting the data into queue
queue.append(1)
queue.append(2)
queue.append(33)
queue.append(6)
queue.append(17)

print(queue)

# Poping the data from left
x = queue.popleft()
print(x)
print(queue)
