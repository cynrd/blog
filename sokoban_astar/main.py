import os
import psutil
import time

import queue
from move import Up, Down, Left, Right
from node import Node
from state import State


def main():
    walls = [[0, 1, 0, 1, 0, 0],
             [0, 1, 0, 1, 1, 1],
             [1, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 1],
             [1, 1, 1, 0, 1, 0],
             [0, 0, 1, 0, 1, 0]]
    player = (3, 3)
    boxes = [(2, 2), (2, 4), (3, 2), (4, 3)]
    goals = [(0, 2), (2, 5), (3, 0), (5, 3)]

    visited = set()
    pq = queue.PriorityQueue()
    state = State(player, boxes)
    pq.put(Node(None, state, 0, None, state.distance(goals)))
    success = False
    success_node = None
    success_move = None
    while not pq.empty():
        node = pq.get()
        if node.state in visited:
            continue
        visited.add(node.state)
        # node.print_actions()
        # print()
        moves = [Up, Down, Right, Left]
        success = False
        for cm in moves:
            m = cm(walls)
            new_state = m.get_state(node.state)
            if new_state is None:
                continue
            if new_state.success(goals):
                success = True
                # success_state = new_state
                success_node = node
                success_move = cm
                break
            if new_state in visited:
                continue
            pq.put(Node(cm.__name__,  new_state, node.depth+1, node, node.depth+new_state.distance(goals)))
        if success:
            break
    if success:
        print("Success")
        success_node.print_actions()
        print(success_move.__name__)
        print("visited states: ", len(visited))

        process = psutil.Process(os.getpid())
        print(process.memory_info().rss/(1024*1024))  # in megabytes


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
