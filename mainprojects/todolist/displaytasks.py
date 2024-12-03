def display_tasks():
    if not tasks:
        print("Lista zadań jest pusta.")
    else:
        for idx, task in enumerate(tasks):
            status = "✓" if task["done"] else "✗"
            print(f"{idx + 1}. {task['name']} [{status}]")