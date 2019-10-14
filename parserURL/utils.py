import threading

def delay_task(task, delay):
    task_timer = threading.Timer(delay, task.parse, args=())
    task_timer.daemon = True
    task_timer.start()