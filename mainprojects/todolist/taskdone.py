def mark_task_done():
    display_tasks()
    try:
        task_num = int(input("Podaj numer zadania do oznaczenia jako ukończone: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]["done"] = True
            print(f"Zadanie '{tasks[task_num]['name']}' zostało oznaczone jako ukończone.")
        else:
            print("Nieprawidłowy numer zadania.")
    except ValueError:
        print("Podaj poprawny numer.")