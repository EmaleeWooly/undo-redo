from node import Node

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear:
            self.rear.next = new_node
        self.rear = new_node
        if self.front is None:
            self.front = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        removed_data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return removed_data

    def peek(self):
        if self.is_empty():
            return None
        return self.front.data

    def display(self):
        customers = []
        current = self.front
        while current:
            customers.append(current.data)
            current = current.next
        return customers


def run_help_desk():
    queue = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            queue.enqueue(name)
            print(f"{name} added to the queue.")

        elif choice == "2":
            customer = queue.dequeue()
            if customer:
                print(f"Helped: {customer}")
            else:
                print("No customers in queue.")

        elif choice == "3":
            customer = queue.peek()
            if customer:
                print(f"Next customer: {customer}")
            else:
                print("No customers waiting.")

        elif choice == "4":
            print("Waiting customers:")
            customers = queue.display()
            if customers:
                for c in customers:
                    print(f"- {c}")
            else:
                print("No customers in queue.")

        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()
