class Node:
    def __init__(self, data, nextNode=None):
        self.data = data
        self.next = nextNode

    def __repr__(self):
        return f"Node({self.data!r})"

    def __eq__(self, other):
        return self.data == other.data


class LinkedList:
    def __init__(self, node=None):
        if node is None:
            self.head = None
            self.tail = None
        else:
            self.head = node
            self.tail = node

    def add_node(self, node):
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            self.tail = node

    def remove_node(self, node):
        if self.head == node:
            self.head = self.head.next
        else:
            currentNode = self.head
            while currentNode.next != node:
                currentNode = currentNode.next
            currentNode.next = currentNode.next.next

    def __repr__(self):
        display = "" if self.head is None else str(self.head)
        return f"LinkedList(head={display})"


if __name__ == '__main__':
    node1 = Node(11)
    node2 = Node('26')
    ll1 = LinkedList()
    ll2 = LinkedList(node1)
    ll3 = LinkedList(node2)
    for n in ('Pete', True, [2, '3'], {'w': 12, 'g': 'dd'}):
        ll3.add_node(Node(n))
