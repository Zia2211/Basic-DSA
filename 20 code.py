class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_duplicates(head):
    current = head

    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next

    return head


def print_list(head):
    current = head

    while current:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


# Create: 1 -> 1 -> 2 -> 3 -> 3
head = Node(1)
head.next = Node(1)
head.next.next = Node(2)
head.next.next.next = Node(3)
head.next.next.next.next = Node(3)

head = remove_duplicates(head)
print_list(head)
