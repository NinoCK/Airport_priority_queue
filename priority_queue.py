from node import Node

class PriorityQueue:
    """
    A priority queue implementation using a doubly linked list.

    Attributes:
        head: The head of the queue.
        tail: The tail of the queue.

    Methods:
        insert(data, priority): Insert a new node in the queue with the given data and priority.
        remove(): Remove and return the node with the highest priority.
        peek(): Return the node with the highest priority without removing it.
        traverse(): Traverse the queue and print the priority of each node.
        is_not_empty(): Check if the queue is empty.
        full_capacity(): Check if the queue has reached its maximum capacity.
    """
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert(self, data, priority):
        """
        Insert a new node in the queue with the given data and priority.

        Args:
            data: The data to be stored in the new node.
            priority: The priority of the new node.
        """
        node = Node(data, priority)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            iteration = self.head
            while iteration is not None and iteration.priority < priority:
                iteration = iteration.next
            if iteration is None:
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
            else:
                if iteration == self.head:
                    iteration.prev = node
                    node.next = iteration
                    self.head = node
                else:
                    iteration.prev.next = node
                    node.prev = iteration.prev
                    iteration.prev = node
                    node.next = iteration

    def remove(self):
        """
        Remove and return the node with the highest priority.

        Returns:
            The node with the highest priority, or None if the queue is empty.
        """
        if self.tail is None:
            return None
        elif self.tail == self.head:
            node = self.tail
            self.tail = None
            self.head = None
        else:
            node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
        return node

    def peek(self):
        """
        Return the node with the highest priority without removing it.

        Returns:
            The node with the highest priority, or None if the queue is empty.
        """
        if self.tail is None:
            return None
        else:
            node = self.tail
        return node

    def traverse(self):
        """
        Traverse the queue and print the priority of each node.
        """
        iteration = self.head
        while iteration is not None:
            print(f'Flight {iteration}')
            iteration = iteration.next

    def is_not_empty(self):
        """
        Check if the queue is empty.

        Returns:
            True if the queue is not empty, False otherwise.
        """
        return self.head is not None

    def full_capacity(self):
        """
        Check if the queue has reached its maximum capacity.

        Returns:
            True if the queue has not reached its maximum capacity, False otherwise.
        """
        counter = 0
        iteration = self.head
        while iteration is not None:
            counter += 1
            iteration = iteration.next
        return counter < 3