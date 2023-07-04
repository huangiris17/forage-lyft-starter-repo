from tire.tire import Tire


class OctoprimeTire(Tire):

    def __init__(self, tire_status):
        self.tire_status = tire_status

    def needs_service(self):
        return sum(self.tire_status) >= 3.0
