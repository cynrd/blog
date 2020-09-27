import os
import psutil
import time
from state import State
from move import Up, Down, Left, Right

def counted(f):
    def wrapped(*args, **kwargs):
        wrapped.calls += 1
        return f(*args, **kwargs)
    wrapped.calls = 0
    return wrapped

class MyPuzzle:
    def __init__(self):
        self.walls = [[0, 1, 0, 1, 0, 0],
                      [0, 1, 0, 1, 1, 1],
                      [1, 1, 0, 0, 0, 0],
                      [0, 0, 0, 0, 1, 1],
                      [1, 1, 1, 0, 1, 0],
                      [0, 0, 1, 0, 1, 0]]
        self.player = (3, 3)
        self.boxes = [(2, 2), (2, 4), (3, 2), (4, 3)]
        self.goals = [(0, 2), (2, 5), (3, 0), (5, 3)]

@counted
def search(path, g, bound, puzzle):
    node = path[-1]
    f = g + node.distance(puzzle.goals)
    if f > bound:
        return False, f
    if node.success(puzzle.goals):
        for state_index in range(1, len(path)):
            if path[state_index-1].player[0] < path[state_index].player[0]:
                print("Down", end=" ")
            elif path[state_index-1].player[0] > path[state_index].player[0]:
                print("Up", end=" ")
            elif path[state_index-1].player[1] < path[state_index].player[1]:
                print("Right", end=" ")
            else:
                print("Left", end=" ")
        return True, bound
    minimum = None
    moves = [Up, Down, Right, Left]
    for cm in moves:
        m = cm(puzzle.walls)
        new_state = m.get_state(node)
        if new_state is None:
            continue
        if new_state not in path:
            path.append(new_state)
            found, value = search(path, g+1, bound, puzzle)
            if found:
                return found, bound
            if value is not None and (minimum is None or value < minimum):
                minimum = value
            path.pop(-1)
    return False, minimum


def main():
    puzzle = MyPuzzle()
    state = State(puzzle.player, puzzle.boxes)
    bound = state.distance(puzzle.goals)*2  # since in general we have to move and go back
    path = [state]
    while True:
        found, value = search(path, 0, bound, puzzle)
        if found:
            print()
            print("search calls:", search.calls)
            process = psutil.Process(os.getpid())
            print(process.memory_info().rss / (1024 * 1024))  # in megabytes
            return path, bound
        if value is None:
            return "not found"
        bound = value


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))