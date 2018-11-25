def main():
    print("===== Welcome to Task Management Application =====")
    print("[S]how: Show all tasks")
    print("[Sd]how: Show all done tasks")
    print("[Su]how: Show all undone tasks")
    print("[A]dd: Add new task")
    print("[D]one: Done task")
    print("[Q]uit")
    print("==================================================")

    command = input("Your Command > ")

    while command != "q" and command != "Q":

        if command == "S" or command == "s":
            pass
        elif command == "Sd" or command == "sd":
            pass
        elif command == "Su" or command == "su":
            pass
        elif command == "A" or command == "a":
            pass
        elif command == "D" or command == "d":
            pass

        command = input("Your Command > ")


if __name__ == "__main__":
    main()
