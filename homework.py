class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float,
                 ) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self):
        message = (f'Тип тренировки: {self.training_type}; '
                   f'Длительность: {self.duration} ч.; '
                   f'Дистанция: {self.distance} км; '
                   f'Ср.скорость: {self.speed} км / ч; '
                   f'Потрачено ккал: {self.calories}.')
        return message


class Training:
    """Базовый класс тренировки."""

    M_IN_KM = 1000
    LEN_STEP = 0.65

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        dist = self.action * Training.LEN_STEP / Training.M_IN_KM
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
        print(self.action, self.duration, self.get_distance(), self.get_mean_speed(), self.get_spent_calories())
        info = InfoMessage(self.action,
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories()
                           )
        return info
        pass


class Running(Training):
    """Тренировка: бег."""
    cal_mult_1 = 18
    cal_mult_2 = 20

    def get_spent_calories(self) -> float:
        spent_cal = ((cal_mult_1 * self.get_mean_speed() - cal_mult_2) * self.weight / M_IN_KM
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
        super().__init__(action, duration, weight)
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
                 length_pool: float,
                 count_pool: float,
                 ) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        speed = self.length_pool * self.count_pool / Training.M_IN_KM / self.duration
        return speed

    def get_spent_calories(self) -> float:
        cal_mult_1 = 1.1
        cal_mult_2 = 2
        spent_cal = (self.get_mean_speed() + cal_mult_1) * cal_mult_2 * self.weight
        return spent_cal


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    train_dict = {"SWM": Swimming,
                  "RUN": Running,
                  "WLK": SportsWalking,
                  }
    train_type = train_dict.get(workout_type)
    train = train_type(*data)
    return train


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    mes = info.get_message()
    print(f'{mes}')


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

