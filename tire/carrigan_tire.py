from tire.tire import Tire


class CarriganTire(Tire):

    def __init__(self, tire_status):
        self.tire_status = tire_status

    def needs_service(self):
        for x in self.tire_status:
            if x < 0.9:
                return False
            else:
                return True
