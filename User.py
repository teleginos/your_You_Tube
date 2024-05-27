class User:
    """
    Класс пользователя
    """
    def __init__(self, nickname: str, password: str, age: int):
        """
        Инициализация объекта класса User

        :param nickname: Имя пользователя
        :param password: Пароль пользователя
        :param age: Возраст пользователя
        """
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self) -> str:
        return f"{self.nickname}"


if __name__ == '__main__':
    user1 = User('Вася', '123456', 20)
    print(user1)
    print(hash(user1))
