class Video:
    def __init__(self, title: str, duration: int, time_now: int = 0, adult_mode: bool = False):
        """
        Инициализация объекта класса видео
        :param title: Название видео
        :param duration: Продолжительность видео
        :param time_now: Время на котором смотрит пользователь
        :param adult_mode: Режим для взрослых
        """
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f"{self.title}"


if __name__ == '__main__':
    video1 = Video('Видео 1', 100)
    print(video1)
