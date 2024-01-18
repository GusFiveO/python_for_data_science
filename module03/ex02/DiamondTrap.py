from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """King Class"""

    def set_eyes(self, eyes: str):
        """change the eyes attribute"""
        self.eyes = eyes

    def set_hairs(self, hairs: str):
        """change the hairs attribute"""
        self.hairs = hairs

    def get_eyes(self):
        """return the eyes attribute"""
        return self.eyes

    def get_hairs(self):
        """return the hairs attribute"""
        return self.hairs
