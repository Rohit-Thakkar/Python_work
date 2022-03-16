# 20ce147_prac9
# LINK:https://github.com/Rohit-Thakkar/python_assign_sem4/
# Aim:Write a Program in Python to implement a Stack Data Structure using Class and Objects, with push, pop, and traversal method.
class Stack:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def push(self, data):
        self.items.append(data)
 
    def pop(self):
        return self.items.pop()
 
 
s = Stack()
while True:
    print('push value (put a space bettween push and whatever value u need to push)')
    print('pop')
    print('quit')
    do = input('What would you like to do? ').split(" ")
 
    operation = do[0].strip().lower()
    if operation == 'push':
        s.push(int(do[1]))
    elif operation == 'pop':
        if s.is_empty():
            print('Stack is empty.')
        else:
            print('Popped value: ', s.pop())
    elif operation == 'quit':
        break
