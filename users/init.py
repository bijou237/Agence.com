from user_dao import UserDAO

(message, user) = UserDAO.get_one()

print(message, user)