def add_task():
  name = input("Podaj nazwę zadania: ")
  tasks.append({"name": name, "done": False})
  print(f"Zadanie '{name}' zostało dodane")