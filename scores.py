class Score:

    def __init__(self, attack, defence):
        self.__defence = defence
        self.__attack = attack

    @property
    def defence(self):
        """
        :return:
        """
        return self.__defence

    @defence.setter
    def defence(self, value):
        """
        :param value:
        :return:
        """
        self.__defence = value

    @property
    def attack(self):
        """
        :return:
        """
        return self.__attack

    @attack.setter
    def attack(self, value):
        """
        :param value:
        :return:
        """
        self.__attack = value

    def __str__(self):
        """
        :return:
        """
        return f" attack = {self.attack}, defence = {self.defence}"
