from User import User
from Video import Video
from time import sleep
from typing import LiteralString


class UrTube:
    def __init__(self):
        """
        Инициализация класса UrTube
        :ivar self.users: словарь пользователей
        :ivar self.videos: словарь видео
        :ivar self.current_user: текущий пользователь
        """
        self.users = {}
        self.videos = {}
        self.current_user = None

    def login_in(self, login: str, password: str):
        """
        Авторизация пользователя
        :param login: Логин пользователя
        :param password:  Пароль пользователя
        """

        if self.users.get(login):
            if self.users[login].password == hash(password):
                self.current_user = self.users[login]
        else:
            print(f'Пользователь {login} не найден')

    def register(self, nickname, password, age):
        """
        Регистрация нового пользователя
        :param nickname: Имя пользователя
        :param password:  Пароль пользователя
        :param age: Возраст пользователя
        """
        if not self.users.get(nickname):
            self.users[nickname] = User(nickname, password, age)
            self.login_in(nickname, password)
        else:
            print(f'Пользователь {nickname} уже зарегистрирован')

    def add(self, *videos: Video):
        """
        Добавление видео в библиотеку
        :param videos: список видео
        """
        for video in videos:
            if not self.videos.get(video.title):
                self.videos[video.title] = video

    def get_videos(self, word: str) -> LiteralString:
        """
        Поиск видел по ключевому слову
        :param word: Ключевое слово для поиска
        """
        list_video = []
        for video in self.videos.values():
            if word.lower() in video.title.lower():
                list_video.append(video.title)
        return ', '.join(list_video)

    def watch_video(self, film_title: str):
        """
        Воспроизведение видео и проверка возрастного ограничения
        """
        if self.current_user:
            if self.videos.get(film_title):
                if self.current_user.age >= 18:
                    self.videos[film_title].time_now += 1
                    print(f'Вы смотрите {self.videos[film_title].title}')
                    for i in range(1, self.videos[film_title].duration + 1):
                        sleep(1)
                        print(i, end=' ')
                    print('Конец видео')
                else:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
        else:
            print('Вы не авторизованы')


if __name__ == '__main__':
    ur = UrTube()
    ur.login_in('Вася', '1q2w3e4r5t')
