from abc import ABC

class Material(ABC):
    def __init__(self, strength):
        self.strength = strength


class Wood(Material):
    def __init__(self, strength):
        super().__init__(strength)


class Metal(Material):
    def __init__(self, strength, purity):
        super().__init__(strength)
        self.purity = purity


class Gemstone(Material):
    def __init__(self, strength, magicPower):
        super().__init__(strength)
        self.magicPower = magicPower


class Maple(Wood):
    def __init__(self, strength=5):
        super().__init__(strength)


class Ash(Wood):
    def __init__(self, strength=3):
        super().__init__(strength)


class Oak(Wood):
    def __init__(self, strength=4):
        super().__init__(strength)


class Bronze(Metal):
    def __init__(self, strength=3, purity=1.3):
        super().__init__(strength, purity)


class Iron(Metal):
    def __init__(self, strength=6, purity=1.1):
        super().__init__(strength, purity)


class Steel(Metal):
    def __init__(self, strength=10, purity=1.8):
        super().__init__(strength, purity)


class Ruby(Gemstone):
    def __init__(self, strength=1, magicPower=1.8):
        super().__init__(strength, magicPower)


class Sapphire(Gemstone):
    def __init__(self, strength=1.2, magicPower=1.6):
        super().__init__(strength, magicPower)


class Emerald(Gemstone):
    def __init__(self, strength=1.6, magicPower=1.1):
        super().__init__(strength, magicPower)


class Diamond(Gemstone):
    def __init__(self, strength=2.1, magicPower=2.2):
        super().__init__(strength, magicPower)


class Amethyst(Gemstone):
    def __init__(self, strength=1.8, magicPower=3.2):
        super().__init__(strength, magicPower)


class Onyx(Gemstone):
    def __init__(self, strength=0.1, magicPower=4.6):
        super().__init__(strength, magicPower)