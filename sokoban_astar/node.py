class Node:
    def __init__(self, action, state, depth, previous, priority):
        self.action = action
        self.state = state
        self.depth = depth
        self.previous = previous
        self.priority = priority

    def __lt__(self, other):
        if self.priority < other.priority:
            return True
        if self.priority > other.priority:
            return False
        if self.depth < other.depth:
            return True
        if self.depth > other.depth:
            return False
        return str(self.state) < str(other.state)

    def print_actions(self):
        if self.previous is not None:
            self.previous.print_actions()
            print(self.action, end=' ')

    def __repr__(self):
        return f"{self.state}, depth: {self.depth}, priority: {self.priority}"
