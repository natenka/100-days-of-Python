from datetime import datetime

NOW = datetime.now()


class Promo:
    def __init__(self, name, expires):
        self.expires = expires

    @property
    def expired(self):
        return self.expires <= NOW
