from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    def __init__(self, protection=120, price=15):
        super().__init__(protection, price)

    def increase_price(self):
        self.price *= (self.price * 0.15)

