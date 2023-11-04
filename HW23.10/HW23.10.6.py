from queue import Queue

to_do = Queue()

def add_to_do(to_do):
    to_do.put("task 1")
    to_do.put("task 2")

def remove_to_do(to_do):
   task = to_do.get("task 1")
add_to_do(to_do)
remove_to_do(to_do)
print(to_do.queue)