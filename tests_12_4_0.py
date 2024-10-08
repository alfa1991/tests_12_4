import logging

class Runner:
    def __init__(self, name, speed=5):
        """
        Инициализация объекта Runner (бегун).

        :param name: Имя бегуна.
        :param speed: Скорость бегуна (по умолчанию 5).
        """
        self.name = name  # Имя бегуна
        self.distance = 0  # Начальная дистанция
        self.speed = speed  # Скорость бегуна

    def run(self):
        """Метод для имитации бега, увеличивает дистанцию бегуна."""
        self.distance += self.speed * 2  # Увеличиваем дистанцию в два раза за "шаг"

    def walk(self):
        """Метод для имитации ходьбы, увеличивает дистанцию бегуна на его скорость."""
        self.distance += self.speed

    def __str__(self):
        """Возвращает строковое представление бегуна (его имя)."""
        return self.name

    def __eq__(self, other):
        """
        Сравнение бегуна с другим объектом.

        :param other: Объект для сравнения (может быть строкой или другим бегуном).
        :return: True, если имена равны, иначе False.
        """
        if isinstance(other, str):
            return self.name == other  # Сравниваем с именем
        elif isinstance(other, Runner):
            return self.name == other.name  # Сравниваем с другим бегуном


class Tournament:
    def __init__(self, distance, *participants):
        """
        Инициализация объекта Tournament (турнир).

        :param distance: Полная дистанция турнира.
        :param participants: Участники турнира.
        """
        self.full_distance = distance  # Полная дистанция турнира
        self.participants = list(participants)  # Список участников

    def start(self):
        """Запускает турнир и возвращает результаты."""
        finishers = {}  # Словарь для хранения финишировавших
        place = 1  # Начальное место

        # Пока есть участники
        while self.participants:
            for participant in self.participants[:]:  # Используем копию списка участников
                participant.run()  # Каждый участник пробегает "шаг"
                if participant.distance >= self.full_distance:  # Проверяем, достиг ли участник финиша
                    if place not in finishers:  # Если место еще не занято
                        finishers[place] = participant  # Сохраняем участника
                        place += 1  # Увеличиваем место
                        self.participants.remove(participant)  # Убираем финишировавшего участника

        return finishers  # Возвращаем словарь с результатами

    def display_results(self, finishers):
        """Отображает результаты турнира."""
        print("Результаты турнира:")
        for place, runner in sorted(finishers.items()):
            print(f"{place} место: {runner.name} на дистанции {runner.distance}")

class RunnerTest:
    def test_walk(self):
        try:
            r1 = Runner('Вася', -5 )
            r1.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner: %s", e)

    def test_run(self):
        try:
            r2 = Runner(2)
            r2.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner: %s", e)

# Настройка логирования
logging.basicConfig(
    filename='runner_tests.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w',
    encoding='utf-8'
)

# Создание экземпляра класса для тестирования
test_runner = RunnerTest()

# Выполнение тестов
test_runner.test_walk()
test_runner.test_run()