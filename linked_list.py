class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"{self.__class__.__name__}({self.data!r})"

    def __eq__(self, other):
        return self.data == other.data


class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def add_node(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def remove_node(self, node):
        """
        Remove the first occurence of the node in the list. Return the node.
        """
        if self.head == node:
            self.head = self.head.next
        else:
            currentNode = self.head
            while currentNode.next != node:
                currentNode = currentNode.next
            currentNode.next = currentNode.next.next
        return node

    def __len__(self):
        """Return linked list's length"""
        if self.head is None:
            return 0
        else:
            count = 1
            curNode = self.head
            while curNode.next is not None:
                count += 1
                curNode = curNode.next
            return count

    def __repr__(self):
        if self.head is None:
            return f"{self.__class__.__name__}()"
        else:
            string = str(self.head)
            curNode = self.head
            while curNode.next is not None:
                string = string + f", {str(curNode.next)}"
                curNode = curNode.next
            return f"{self.__class__.__name__}({string})"


if __name__ == '__main__':
    node1 = Node(11)
    node2 = Node('26')
    ll1 = LinkedList()
    ll2 = LinkedList(node1)
    ll3 = LinkedList()
    for n in (12, 'Pete', True, [2, '3'], {'w': 12, 'g': 'dd'}):
        ll3.add_node(Node(n))
