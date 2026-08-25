"""
Exercise = Stack (LIFO = Last In, First Out)
"""

stack = []
# push
stack.append(1) # Push (when we stack an element onto a stack)
stack.append(2)
stack.append(3)
print(stack)

# pop (when we remove elements from the stack)
stack_item = stack[len(stack) - 1]
del stack[len(stack) - 1]
print(stack_item)

print(stack.pop())

print(stack)

# Queue (FIFO = First In, First Out)

queue = []

# enqueue
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)

# dequeue
queue_item = queue[0]
del queue[0]
print(queue_item)

print(queue.pop(0))

print(queue)

"""
- Using the stack implementation and text strings, simulate a web browser's 
  forward/back navigation mechanism. Create a program where you can navigate to a page 
  or instruct it to move forward or backward, displaying the name of the website in each case.
  The words "forward" and "back" trigger these actions, while all other words are interpreted 
  as the name of a new website.
- Using the queue implementation and text strings, simulate a shared printer 
  mechanism that receives documents and prints them when instructed.
  The word "print" prints an element from the queue, while all other words are 
  interpreted as document names.
"""

# Web

def web_navigation():

    stack = []

    while True:

        action = input(
            "Add a URL or interact with the keywords forward/back/exit: "
        )

        if action == "exit":
            print("Exiting WebNav.")
            break
        elif action == "forward":
            pass
        elif action == "back":
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(action)

        if len(stack) > 0:
            print(f"You have navigated to the website: {stack[len(stack) - 1]}.")
        else:
            print("You are on the home page.")


web_navigation()

def shared_printer():

    queue = []

    while True:

        action = input("Add a document or select print/exit: ")

        if action == "exit":
            break
        elif action == "print":
            if len(queue) > 0:
                print(f"Printing: {queue.pop(0)}")
        else:
            queue.append(action)

            print(f"Print queue: {queue}")


shared_printer()