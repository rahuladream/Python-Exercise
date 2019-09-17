"""
Collection that support push and pop operations
Workk as LIFO
Last in First count

Example:
Expression Processing, Backtracking(How web browser manage
the back and front data in stack)
"""

stack = []

# Inserting the several items
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

print(stack)


x = stack.pop()
print(x)
print(stack)
