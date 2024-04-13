class Departement:
    def __init__(self, nom,emplacement,direction) -> None:
        self.__nom = nom
        self.__emplacement = emplacement
        self.__direction = direction

    @property
    def _nom(self):
        return self.__nom

    @_nom.setter
    def _nom(self, value):
        self.__nom = value

    @property
    def _emplacement(self):
        return self.__emplacement

    @_emplacement.setter
    def _emplacement(self, value):
        self.__emplacement = value

    @property
    def _direction(self):
        return self.__direction

    @_direction.setter
    def _direction(self, value):
        self.__direction = value

