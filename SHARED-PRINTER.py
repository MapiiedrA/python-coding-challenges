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