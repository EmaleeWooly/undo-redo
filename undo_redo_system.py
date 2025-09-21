from node import Node

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        removed_data = self.top.data
        self.top = self.top.next
        return removed_data

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    def display(self):
        actions = []
        current = self.top
        while current:
            actions.append(current.data)
            current = current.next
        return actions


def run_undo_redo():
    undo_stack = Stack()
    redo_stack = Stack()

    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            action = input("Describe the action (e.g., Insert 'a'): ")
            undo_stack.push(action)
            redo_stack = Stack()  # clear redo stack
            print(f"Action performed: {action}")

        elif choice == "2":
            action = undo_stack.pop()
            if action:
                redo_stack.push(action)
                print(f"Undid action: {action}")
            else:
                print("Nothing to undo.")

        elif choice == "3":
            action = redo_stack.pop()
            if action:
                undo_stack.push(action)
                print(f"Redid action: {action}")
            else:
                print("Nothing to redo.")

        elif choice == "4":
            print("Undo Stack:")
            actions = undo_stack.display()
            if actions:
                for act in actions:
                    print(f"- {act}")
            else:
                print("(empty)")

        elif choice == "5":
            print("Redo Stack:")
            actions = redo_stack.display()
            if actions:
                for act in actions:
                    print(f"- {act}")
            else:
                print("(empty)")

        elif choice == "6":
            print("Exiting Undo/Redo Manager.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_undo_redo()
