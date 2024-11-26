import logging      # Импортируем логирование
import runner
import unittest

# Настраиваем логирование basicConfig под требования задачи
logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_test.log',
                    encoding='utf-8', format='%(asctime)s : %(levelname)s : %(message)s')


class RunnerTest(unittest.TestCase):
    """Проверим на юниттесте класс Runner из модуля runner.py"""
    is_frozen = False

    def walk_object(self, runner_):     # Метод для вызывания метода walk класса Runner
        for i in range(10):
            runner_.walk()

    def run_object(self, runner_):      # Метод для вызывания метода run класса Runner
        for i in range(10):
            runner_.run()

    @unittest.skipIf(is_frozen is True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        # Проверяем логирование с помощью try-except в методе test-walk, специально ставя отрицательную скорость
        try:
            runner1 = runner.Runner('ivan', -10)
            self.walk_object(runner1)
            self.assertEqual(runner1.distance, 100)
            logging.info('"test_walk" выполнен успешно', exc_info=True)
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    @unittest.skipIf(is_frozen is True, 'Тесты в этом кейсе заморожены')
    # Проверяем логирование с помощью try-except в методе test-run, специально ставя неправильный тип данных в имя
    def test_run(self):
        try:
            runner2 = runner.Runner(0, 12)       # Создаем произвольный, но другой объект класса и тестируем его
            self.run_object(runner2)
            self.assertEqual(runner2.distance, 100)
            logging.info('"test_run" выполнен успешно', exc_info=True)
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    @unittest.skipIf(is_frozen is True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):                   # Создаем два произвольных объекта класса Runner и тестируем их
        some_object3 = runner.Runner("name1")   # на двух разных методах класса
        some_object4 = runner.Runner("name1")

        self.walk_object(some_object3)
        self.walk_object(some_object3)
        self.run_object(some_object4)
        self.run_object(some_object4)

        self.assertNotEqual(some_object3.distance, some_object4.distance)


if __name__ == '__main__':
    unittest.main()
