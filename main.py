import sys


class Menu:
    """
    A CLI based UI to interact with the TO-DO application
    """

    def __init__(self):
        self.choices = {
            "1": self.add_todo,
            "2": self.mark_todo_as_done,
            "3": self.remove_todo,
            "4": self.update_todo,
            "5": self.exit,

        }

    def run(self):
        while True:
            self.display_menu()

            choice = input("Enter your choice: ")
            action = self.choices.get(choice)

            if action:
                action()
            else:
                print(f"{choice} is not a valid choice!")

    def exit(self):
        print("Thank you using the todo application.")
        sys.exit(1)

    def display_menu(self):
        print("""
        Welcome to the To-Do app!

        1. Add an item
        2. Mark an item as done
        3. Remove an item
        4. Update an item
        5. Exit
        """)

    def add_todo(self):
        pass

    def update_todo(self):
        pass

    def remove_todo(self):
        pass

    def mark_todo_as_done(self):
        pass


if __name__ == '__main__':
    menu = Menu()
    menu.run()
