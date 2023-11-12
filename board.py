import json

from knight import Knight
from Item import Item
from coordinates import Position
from scores import Score


class Board:

    def __init__(self):
        self.__knights: {str: Knight} = dict()
        self.__items: {str: Item} = dict()
        self.initialize_knights()
        self.initialize_items()

    @property
    def knights(self):
        """
        :return:
        """
        return self.__knights

    @knights.setter
    def knights(self, value: Knight):
        """
        :param value:
        :return:
        """
        self.__knights[value.name] = value

    @property
    def items(self):
        """
        :return:
        """
        return self.__items

    @items.setter
    def items(self, value: Knight):
        """
        :param value:
        :return:
        """
        self.__items[value.name] = value

    def initialize_knights(self):
        """
        :return:
        """
        with open("data.json") as json_file:
            data = json.load(json_file)
            for key, value in data["knights"].items():
                self.knights[key] = Knight(key, Position(value["x"], value["y"]), value["direction"])
        
        

    def initialize_items(self):
        """
        :return:
        """
        with open("data.json") as json_file:
            data = json.load(json_file)
            for key, value in data["items"].items():
                self.items[key] = Item(key, Position(value["x"], value["y"]))

    def has_any_item(self, name):
        """
        :param name:
        :return:
        """
        return self.items[name].is_available
        

    def validate_fight_and_item(self, name):
        """
        :param name:
        :return:
        """
        if self.has_any_item(name):
            return True
        return False

    def update_acquired_items_location(self):
        """
        :return:
        """
        for key, value in self.items.items():
            if value.is_available:
                value.update_location()

    def main(self, name, direction):
        """
        :param name:
        :param direction:
        :return:
        """
        if self.validate_fight_and_item(name):
            self.knights[name].update_location(direction)
            self.update_acquired_items_location()
            self.knights[name].update_score(Score(self.items[name].name))
            self.items[name].is_available = False
            self.items[name].location = Position(-1, -1)
            self.knights[name].update_direction(direction)
        else:
            self.knights[name].update_location(direction)
            self.knights[name].update_direction(direction)

    def read_input(self, knight, direction):
        """
        :param knight:
        :param direction:
        :return:
        """
        self.main(knight, direction)

    # this function return desired output
    def output(self):
        """
        :return:
        """
        return {
            "red": self.knights["R"].to_list(),
            "blue": self.knights["B"].to_list(),
            "green": self.knights["G"].to_list(),
            "yellow": self.knights["Y"].to_list(),
            "magic_staff": self.items["M"].to_list(),
            "helmet": self.items["H"].to_list(),
            "dagger": self.items["D"].to_list(),
            "axe": self.items["A"].to_list()
        }


if __name__ == '__main__':
    board = Board()
    print(board.output())
