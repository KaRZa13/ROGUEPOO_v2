class Attacks:
    def __init__(self, name, damage):
        self.__name = name
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def damage(self):
        return self.__damage