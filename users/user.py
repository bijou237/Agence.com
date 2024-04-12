class User:
    def __init__(self, nom_complet, username, password) -> None:
        self.__nom_complet = nom_complet
        self.__username = username
        self.__password = password

    @property
    def _nom_complet(self):
        return self.__nom_complet

    @_nom_complet.setter
    def _nom_complet(self, value):
        self.__nom_complet = value

    @property
    def _username(self):
        return self.__username

    @_username.setter
    def _username(self, value):
        self.__username = value

    @property
    def _password(self):
        return self.__password

    @_password.setter
    def _password(self, value):
        self.__password = value


