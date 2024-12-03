def remove_task():
    display_tasks()
    try:
        task_num = int(input("Podaj numer zadania do usunięcia: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            print(f"Zadanie '{removed_task['name']}' zostało usunięte.")
        else:
            print("Nieprawidłowy numer zadania.")
    except ValueError:
        print("Podaj poprawny numer.")