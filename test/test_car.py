import unittest
from datetime import datetime

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from tire.carrigan_tire import CarriganTire
from tire.octoprime_engine import OctoprimeTire


class TestCarrigan(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        status_tire = [0.8, 0.8, 1.0, 0.9]

        tire = CarriganTire(status_tire)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        status_tire = [0.8, 0.8, 0.8, 0.8]

        tire = CarriganTire(status_tire)
        self.assertFalse(tire.needs_service())


class TestOctoprime(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        status_tire = [0.9, 0.9, 0.9, 0.3]

        tire = OctoprimeTire(status_tire)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        status_tire = [0.9, 0.9, 0.9, 0.2]

        tire = OctoprimeTire(status_tire)
        self.assertFalse(tire.needs_service())


class TestNubbin(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        battery = NubbinBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        battery = NubbinBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())
##


class TestSpindler(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)

        battery = SpindlerBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        battery = SpindlerBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())
##


class TestCapulet(unittest.TestCase):

    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage,
                               last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage,
                               last_service_mileage)
        self.assertFalse(engine.needs_service())

##


class TestSternman(unittest.TestCase):

    def test_engine_should_be_serviced(self):
        warning_light_is_on = True

        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False

        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())


class TestWilloughby(unittest.TestCase):

    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage,
                                  last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage,
                                  last_service_mileage)
        self.assertFalse(engine.needs_service())


#     def test_battery_should_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 3)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = Glissade(last_service_date, current_mileage,
#                        last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_battery_should_not_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 1)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = Glissade(last_service_date, current_mileage,
#                        last_service_mileage)
#         self.assertFalse(car.needs_service())

#     def test_engine_should_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 60001
#         last_service_mileage = 0

#         car = Glissade(last_service_date, current_mileage,
#                        last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_engine_should_not_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 60000
#         last_service_mileage = 0

#         car = Glissade(last_service_date, current_mileage,
#                        last_service_mileage)
#         self.assertFalse(car.needs_service())


# class TestPalindrome(unittest.TestCase):
#     def test_battery_should_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 5)
#         warning_light_is_on = False

#         car = Palindrome(last_service_date, warning_light_is_on)
#         self.assertTrue(car.needs_service())

#     def test_battery_should_not_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 3)
#         warning_light_is_on = False

#         car = Palindrome(last_service_date, warning_light_is_on)
#         self.assertFalse(car.needs_service())

#     def test_engine_should_be_serviced(self):
#         last_service_date = datetime.today().date()
#         warning_light_is_on = True

#         car = Palindrome(last_service_date, warning_light_is_on)
#         self.assertTrue(car.needs_service())

#     def test_engine_should_not_be_serviced(self):
#         last_service_date = datetime.today().date()
#         warning_light_is_on = False

#         car = Palindrome(last_service_date, warning_light_is_on)
#         self.assertFalse(car.needs_service())


# class TestRorschach(unittest.TestCase):
#     def test_battery_should_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 5)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = Rorschach(last_service_date, current_mileage,
#                         last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_battery_should_not_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 3)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = Rorschach(last_service_date, current_mileage,
#                         last_service_mileage)
#         self.assertFalse(car.needs_service())

#     def test_engine_should_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 60001
#         last_service_mileage = 0

#         car = Rorschach(last_service_date, current_mileage,
#                         last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_engine_should_not_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 60000
#         last_service_mileage = 0

#         car = Rorschach(last_service_date, current_mileage,
#                         last_service_mileage)
#         self.assertFalse(car.needs_service())


# class TestThovex(unittest.TestCase):
#     def test_battery_should_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 5)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = Thovex(last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_battery_should_not_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 3)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = Thovex(last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())

#     def test_engine_should_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 30001
#         last_service_mileage = 0

#         car = Thovex(last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_engine_should_not_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 30000
#         last_service_mileage = 0

#         car = Thovex(last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
