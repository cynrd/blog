from state import State


class Move:
    def __init__(self, walls):
        self.walls = walls

    def get_state(self, state):
        if not self.can_move_in_direction(state):
            return None
        target_player_pos = (self.next_row(state), self.next_col(state))
        if self.walls[target_player_pos[0]][target_player_pos[1]] == 1:
            return None
        if target_player_pos not in state.boxes:
            return State(target_player_pos, state.boxes)
        if target_player_pos in state.boxes:
            target_box_pos = (self.next_next_row(state), self.next_next_col(state))
            if self.can_move_box_in_direction(state) and \
                self.walls[target_box_pos[0]][target_box_pos[1]] == 0 and \
                target_box_pos not in state.boxes:
                boxes_copy = list(state.boxes)
                boxes_copy.remove(target_player_pos)
                boxes_copy.append(target_box_pos)
                return State(target_player_pos, boxes_copy)

    def can_move_in_direction(self, state):
        raise NotImplementedError

    def next_next_row(self, state):
        raise NotImplementedError

    def next_col(self, state):
        raise NotImplementedError

    def next_row(self, state):
        raise NotImplementedError

    def next_next_col(self, state):
        raise NotImplementedError

    def can_move_box_in_direction(self, state):
        raise NotImplementedError


class Up(Move):
    @staticmethod
    def can_move_in_direction(state):
        return state.player[0] > 0

    @staticmethod
    def can_move_box_in_direction(state):
        return state.player[0] > 1

    @staticmethod
    def next_row(state):
        return state.player[0]-1

    @staticmethod
    def next_col(state):
        return state.player[1]

    @staticmethod
    def next_next_row(state):
        return state.player[0]-2

    @staticmethod
    def next_next_col(state):
        return state.player[1]


class Down(Move):
    def can_move_in_direction(self, state):
        return state.player[0] < len(self.walls)-1

    def can_move_box_in_direction(self, state):
        return state.player[0] < len(self.walls)-2

    @staticmethod
    def next_row(state):
        return state.player[0]+1

    @staticmethod
    def next_col(state):
        return state.player[1]

    @staticmethod
    def next_next_row(state):
        return state.player[0]+2

    @staticmethod
    def next_next_col(state):
        return state.player[1]

class Left(Move):
    @staticmethod
    def can_move_in_direction(state):
        return state.player[1] > 0

    @staticmethod
    def can_move_box_in_direction(state):
        return state.player[1] > 1

    @staticmethod
    def next_row(state):
        return state.player[0]

    @staticmethod
    def next_col(state):
        return state.player[1]-1

    @staticmethod
    def next_next_row(state):
        return state.player[0]

    @staticmethod
    def next_next_col(state):
        return state.player[1]-2

class Right(Move):
    def can_move_in_direction(self, state):
        return state.player[1] < len(self.walls[0])-1

    def can_move_box_in_direction(self, state):
        return state.player[1] < len(self.walls[0])-2

    @staticmethod
    def next_row(state):
        return state.player[0]

    @staticmethod
    def next_col(state):
        return state.player[1]+1

    @staticmethod
    def next_next_row(state):
        return state.player[0]

    @staticmethod
    def next_next_col(state):
        return state.player[1]+2
