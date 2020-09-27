class State:
    def __init__(self, player, boxes):
        self.player = player
        self.boxes = boxes

    def success(self, goals):
        return all(map(lambda g: g in self.boxes, goals))

    def __repr__(self):
        return f"player: {self.player}, boxes: {self.boxes}"

    @staticmethod
    def manhattan(b, g):
        return abs(b[0] - g[0]) + abs(b[1] - g[1])

    def distance(self, goals):
        boxes_copy = list(self.boxes)
        result = 0
        for g in goals:
            b, d = min([(b, self.manhattan(b, g)) for b in boxes_copy], key=lambda t: t[1])
            result += d
            boxes_copy.remove(b)
        return result
