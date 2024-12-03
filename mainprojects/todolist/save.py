def load_tasks_from_file():
    try:
        with open(FILENAME, 'r') as file:
            global tasks
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
        save_tasks_to_file()
    except json.JSONDecodeError:
        print("Błąd wczytywania pliku. Plik może być uszkodzony.")
        tasks = []