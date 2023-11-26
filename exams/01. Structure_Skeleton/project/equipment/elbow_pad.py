from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    def __init__(self, protection=90, price=25):
        super().__init__(protection, price)

    def increase_price(self):
        self.price *= (self.price * 0.10)