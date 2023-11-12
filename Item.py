import knight
from coordinates import Position
from scores import Score


class Item:

    def __init__(self, name: str, position: Position, score: Score, acquired_by=None):
        self.__name: str = name
        self.__position: Position = position
        self.__acquired_by: knight.Knight = acquired_by
        self.__score: Score = score

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

    @property
    def acquired_by(self):
        """
        :return:
        """
        return self.__acquired_by

    @property
    def score(self):
        """
        :return:
        """
        return self.__score

    @acquired_by.setter
    def acquired_by(self, value):
        """
        :param value:
        :return:
        """
        self.__acquired_by = value

    @score.setter
    def score(self, value):
        """
        :param value:
        :return:
        """
        self.__score = value

    # update position of items according to their knight so when knight drop the item then the position of knight is
    #  also same as knight. we can manage it by other logics also
    def update_position_by_acquired_knight(self):
        """
        :return:
        """
        self.position = self.acquired_by.position
       

    # return output of each item according to desire output
    def to_list(self):
        """
        :return:
        """
        return [
            [self.position.x, self.position.y],
            self.acquired_by is not None
        ]
