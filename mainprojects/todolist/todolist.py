import tkinter
import addtask
import displaytasks
import removetask
import taskdone
import save
import json

tasks = []

def main():
    while True:
        print("\n--- Lista zadań ---")
        print("1. Wyświetl wszystkie zadania")
        print("2. Dodaj nowe zadanie")
        print("3. Usuń zadanie")
        print("4. Oznacz zadanie jako ukończone")
        print("5. Wyjdź")
        
        choice = input("Wybierz opcję (1-5): ")
        
        if choice == "1":
            display_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_task_done()
        elif choice == "5":
            print("Koniec programu. Do widzenia!")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    main()
    
load_tasks_from_file()