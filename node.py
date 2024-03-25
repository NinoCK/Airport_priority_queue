class Node:
    """
    Represents a node in a priority queue.

    Attributes:
        data: The data stored in the node.
        priority: The priority of the node.
        next: Reference to the next node in the priority queue.
        prev: Reference to the previous node in the priority queue.
    """

    def __init__(self, data, priority) -> None:
        """
        Initializes a new instance of the Node class.

        Args:
            data: The data to be stored in the node.
            priority: The priority of the node.
        """
        self.data = data
        self.priority = priority
        self.next = None
        self.prev = None

    def __str__(self):
        """
        Returns a string representation of the node.

        Returns:
            A string representation of the node, which includes the priority and data.
        """
        return str(self.priority) + " " + self.data