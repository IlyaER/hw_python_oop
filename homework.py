class InfoMessage:
    """Информационное сообщение о тренировке."""
    pass


class Training:
    """Базовый класс тренировки."""
    M_IN_KM = 1000
    LEN_STEP = 0.65

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        pass

    def get_distance(self) -> float:
        """Получить дистанцию в км."""

        dist = self.action * LEN_STEP / M_IN_KM
        return dist

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""

        speed = self.get_distance() / self.duration
        return speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        pass


class Running(Training):
    """Тренировка: бег."""
    cal_mult_1 = 18
    cal_mult_2 = 20

    def get_spent_calories(self) -> float:
        spent_cal = ((cal_mult_1 * self.get_mean_speed() - cal_mult_2) * self.weight / M_IN_KM \
                     * self.duration)
        return spent_cal


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float,
                 ) -> None:
        super().__init__(self, action, duration, weight)
        self.height = height

    def get_spent_calories(self):
        cal_mult_1 = 0.035
        cal_mult_2 = 2
        cal_mult_3 = 0.029
        spent_cal = (cal_mult_1 * self.weight + (self.get_mean_speed() ** cal_mult_2 // self.height) * cal_mult_3 * self.weight) * self.duration
        return spent_cal


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP = 1.38

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: int,
                 count_pool: int,
                 ) -> None:
        super().__init__(self, action, duration, weight)
        self.height = height

    def get_mean_speed(self) -> float:
        speed = length_pool * count_pool / M_IN_KM / self.duration
        return speed

    def get_spent_calories(self) -> float:
        cal_mult_1 = 1.1
        cal_mult_2 = 2
        spent_cal = (self.get_mean_speed() + cal_mult_1) * cal_mult_2 * self.weight
        return spent_cal


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

