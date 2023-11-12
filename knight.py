from coordinates import Position
from scores import Score
from Item import Item
from state import State


class Knight:
    def __init__(self, name: str, position: Position, score: Score, item: Item = None, state: State = State.Live):
        self.__name = name
        self.__position = position
        self.__score = score
        self.__item = item
        self.__state = state

    @property
    def name(self):
        """
        :return:
        """
        return self.__name

    @property
    def position(self):
        """
        :return:
        """
        return self.__position

    @property
    def score(self):
        """
        :return:
        """
        return self.__score

    @property
    def item(self):
        """
        :return:
        """
        return self.__item

    @name.setter
    def name(self, value):
        """
        :param value:
        :return:
        """
        self.__name = value

    @position.setter
    def position(self, value):
        """
        :param value:
        :return:
        """
        self.__position = value

    @score.setter
    def score(self, value):
        """
        :param value:
        :return:
        """
        self.__score = value

    @item.setter
    def item(self, value):
        """
        :param value:
        :return:
        """
        self.__item = value

    @property
    def state(self) -> State:
        """
        :return:
        """
        return self.__state

    @state.setter
    def state(self, value: State):
        """
        :param value:
        :return:
        """
        self.__state = value

    def is_live(self) -> bool:
        """
        :return:
        """
        return self.state == State.Live

    def does_not_has_item(self):
        """
        :return:
        """
        return self.item is None

    def drop_item(self, state: State):
        """
        :param state:
        :return:
        """
        self.item = None
        self.state = state
      

    def declare_dead(self):
        """
        :return:
        """
        self.drop_item(State.Dead)

    def declare_drowned(self):
        """
        :return:
        """
        self.drop_item(State.DROWNED)

    # update score  of current knight according to items attack and defence score
    def acquire_item(self, item: Item):
        if self.item is None:  # Check if the knight doesn't already have an item
            self.score.attack += item.score.attack
            self.score.defence += item.score.defence
            self.item = item
            item.acquired_by = self

        

    # return true if attacker win the fight else return false
    def is_winner(self, defender) -> bool:
        if self.score.attack > defender.score.defence:
            return True
        return False

        

    # check if item and knight has same positioned and item is not acquired by any other knight
    def found_item(self, item: Item):
        return item.position == self.position and item.acquired_by is None

    # equal operator overload that return true if both knights has same position else false
    def __eq__(self, other):
        """
        :param other:
        :return:
        """
        return other is not None and self.position.x == other.position.x and self.position.y == other.position.y

    # updated position of knight when it moves towards north
    def move_north(self):
        self.position.y += 1

    # updated position of knight when it moves towards south
    def move_south(self):
        self.position.y -= 1

    # updated position of knight when it moves towards wast
    def move_west(self):
        self.position.x -= 1

    # updated position of knight when it moves towards east
    def move_east(self):
        self.position.x += 1

    # convert state into string for output purpose. because output required state of each knight in string format,
    # but we use enum in code
    def state_to_str(self):
        """
        :return:
        """
        if self.state == State.Live:
            return "LIVE"
        elif self.state == State.Dead:
            return "DEAD"
        else:
            return "DROWNED"

    # check current knight has any fight with other knights or not
    def has_any_fight(self, knights: dict):
        for other_knight in knights.values():
            if self.position == other_knight.position and self.name != other_knight.name:
                return True
        return False

    # return output required format for every knight
    def to_list(self):
        """
        :return:
        """
        return [
            [self.position.x, self.position.y] if self.state != State.DROWNED else None,
            self.state_to_str(),
            self.item.name if self.item is not None else None,
            self.score.attack,
            self.score.defence
        ]
