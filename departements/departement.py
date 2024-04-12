class Departement:
    def __init__(self, finance, it, rh, projet):
        self.__finance = finance
        self.__it = it
        self.__rh = rh
        self.__Projet= projet 

    @property
    def _finance(self):
        return self.__finance

    @_finance.setter
    def _finance(self, value):
        self.__finance = value

    @property
    def _it(self):
        return self.__it

    @_it.setter
    def _it(self, value):
        self.__it = value

    @property
    def _rh(self):
        return self.__rh

    @_rh.setter
    def _rh(self, value):
        self.__rh = value

    @property
    def _Projet(self):
        return self.__Projet

    @_Projet.setter
    def _Projet(self, value):
        self.__Projet = value


   