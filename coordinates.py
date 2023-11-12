class Position:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        """
        :return:
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        :param value:
        :return:
        """
        self.__x = value

    @property
    def y(self):
        """
        :return:
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        :param value:
        :return:
        """
        self.__y = value

