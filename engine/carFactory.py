from capulet_engine import CapuletEngine
from sternman_engine import SternmanEngine
from willoughby_engine import WilloughbyEngine
from nubbin_battery import NubbinBattery
from spindler_battery import SpindlerBattery
from car import Car

class CarFactory():

    def  create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(CapuletEngine(current_mileage, last_service_mileage), SpindlerBattery(last_service_date, current_date))

    def  create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage), SpindlerBattery(last_service_date, current_date))

    def  create_palindrome(current_date, last_service_date, warning_light_on):
        return Car(SternmanEngine(warning_light_on), SpindlerBattery(last_service_date, current_date))

    def  create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage), NubbinBattery(last_service_date, current_date))

    def  create_thovex(current_date, last_service_date, current_mileage, last_service_mileage): 
        return Car(CapuletEngine(current_mileage, last_service_mileage), NubbinBattery(last_service_date, current_date))