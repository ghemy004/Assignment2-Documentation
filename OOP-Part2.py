from abc import ABC, abstractmethod

from Material import *

'''
File: OOP-Part2.py
Description: A brief description of this Python module.
Author: Matewos Ghebreab
StudentID: 110350204
EmailID: ghemy004@mymail.unisa.edu.au
This is my own work as defined by the University's Academic Misconduct Policy.
'''

class Workshop: # The main class
    def __init__(self, forge, enchanter): # 
        self.forge = forge
        self.enchanter = enchanter
        self.materials = {}
        self.weapons = []
        self.enchantments = [] 
    
    # this method takes material as a parameter and adds it to the material 
    def addMaterial(self, material, num):
        self.materials[material] = num
    
    def removeMaterial(self, material):
        del self.materials[material]
    
    # this method takes weapon as a parameter and adds it to the weapons list
    def addWeapon(self, weapon):
        self.weapons.append(weapon)
        
    def removeWeapon(self, weapon):
        self.weapons.remove(weapon)
    
    # this method takes echantment as a parameter and adds it to the echantment list
    def addEnchantment(self,enchantment):
        self.enchantments.append(enchantment)

    def removeEnchantment(self, enchantment):
        self.enchantments.remove(enchantment)

    def displayWeapons(self):
        enchantmentDetails = ""

        for weapon in self.weapons: 
            
            if weapon.getEnchanted() == True: 

                enchantmentDetails += f'The {weapon.getName()} is imbued with a {weapon.getEnchantment().useEffect()}. {weapon.attack()}'
            else:
                enchantmentDetails += f"{weapon.getName()} is not enchanted. {weapon.attack()}"

        return enchantmentDetails
    
    def displayEnchantments(self):
        enchantmentNames = []
        
        for enchantment in self.enchantments:
            enchantmentNames.append('A {} enchantment is stored in workshop.'.format(enchantment.getName()))

        return '\n'.join(enchantmentNames)  
    
    def displayMaterials(self):
        materialDisplay = ""

        for material in self.materials:
            materialDisplay += f"{material}: {self.materials[material]} remaining.\n"

        return materialDisplay

class Crafter(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def craft(self): # implementation of the craft method
        pass
    
    @abstractmethod
    def disassemble(self): # implemenetation of the disassemble method
        pass

class Weapon:
    def __init__(self, primaryMaterial, catalystMaterial):
        self.__primaryMaterial = primaryMaterial
        self.__catalystMaterial = catalystMaterial
        self.__damage = 0
        self.__enchantment = ''
        self.__enchanted = False
        self.__name = ''
    
    def getName(self):
        return self.__name
    
    def getDamage(self):
        return self.__damage
    
    def getEnchanted(self):
        return self.__enchanted
    
    def getPrimaryMaterial(self):
        return self.__primaryMaterial
    
    def getCatalystMaterial(self):
        return self.__catalystMaterial
    
    def getEnchantment(self):
        return self.__enchantment
    
    def setName(self, name):
        self.__name = name
    
    def setDamage(self, damage):
        self.__damage = damage
    
    def setEnchanted(self, enchanted):
        self.__enchanted = enchanted
    
    def setEnchantment(self, enchantment):
        self.__enchantment = enchantment
    
    def calculateDamage(self, primaryMaterial, catalystMaterial):

        if isinstance(primaryMaterial, Wood) and isinstance(catalystMaterial, Wood):
            damage = primaryMaterial.strength * catalystMaterial.strength

        elif isinstance (primaryMaterial, Metal) and isinstance(catalystMaterial, Metal):
            damage = (primaryMaterial.strength * primaryMaterial.purity) + (catalystMaterial.strength * catalystMaterial.purity)
        
        elif isinstance (primaryMaterial, Wood) and isinstance(catalystMaterial, Metal):
            damage = primaryMaterial.strength * (catalystMaterial.strength * catalystMaterial.purity)
        else:
            damage = catalystMaterial.strength * (primaryMaterial.strength * primaryMaterial.purity)
        
        return damage
    
    def attack(self):
        return f"It deals {self.getDamage():.2f} damage.\n"

class Forge(Crafter):
    def __init__(self):
        pass
    
    def craft(self, name, primaryMaterial, catalystMaterial, materials):
        weapon = Weapon(primaryMaterial, catalystMaterial)
        weapon.setDamage(weapon.calculateDamage(primaryMaterial, catalystMaterial))
        weapon.setName(name)

        materials[primaryMaterial.__class__.__name__] -= 1
        materials[catalystMaterial.__class__.__name__] -= 1

        return weapon
    
    def disassemble(self, weapon, materials):
        primaryMaterial = weapon.getPrimaryMaterial()
        catalystMaterial = weapon.getCatalystMaterial()

        materials[primaryMaterial.__class__.__name__] += 1
        materials[catalystMaterial.__class__.__name__] += 1 
        return weapon

        
class Enchanter(Crafter):
    def __init__(self):
        self.recipes = {
            "Holy": "pulses a blinding beam of light",
            "Lava": "melts the armour off an enemy",
            "Pyro": "applies a devastating burning effect",
            "Darkness": "binds the enemy in dark vines",
            "Cursed": "causes the enemy to become crazed",
            "Hydro": "envelops the enemy in a suffocating bubble",
            "Venomous": "afflicts a deadly, fast-acting toxin",
            "Earthly":"Down to earth"}
        

    def craft(self, name, primaryMaterial, catalystMaterial, materials):
        materials[primaryMaterial.__class__.__name__] -= 1
        materials[catalystMaterial.__class__.__name__] -= 1 
        enchantment = Enchantment(name, primaryMaterial, catalystMaterial)
        enchantment.setEffect(self.recipes[name])
        enchantment.setMagicDamage(enchantment.calculateMagicDamage(primaryMaterial, catalystMaterial))
        return enchantment

    def disassemble(self, enchantment, materials):
        primaryMaterial = enchantment.getPrimaryMaterial()
        catalystMaterial = enchantment.getCatalystMaterial()

        materials[primaryMaterial.__class__.__name__] += 1
        materials[catalystMaterial.__class__.__name__] += 1 
        return enchantment
    
    def enchant(self, weapon, newName, enchantment):
        weapon.setEnchanted(True)
        weapon.setEnchantment(enchantment)
        weapon.setDamage(weapon.getDamage() * enchantment.getMagicDamage())
        weapon.setName(newName)

        return weapon
        


class Enchantment:
    def __init__(self, name, primaryMaterial, catalystMaterial):
        self.__name = name
        self.__magicDamage = 0
        self.__effect = ''
        self.__primaryMaterial = primaryMaterial
        self.__catalystMaterial = catalystMaterial
    
    def getName(self):
        return self.__name
    
    def getMagicDamage(self):
        return self.__magicDamage
    
    def getEffect(self):
        return self.__effect

    def getPrimaryMaterial(self):
        return self.__primaryMaterial
    
    def getCatalystMaterial(self):
        return self.__catalystMaterial
    
    def setEffect(self, value):
        self.__effect = value
    
    def setMagicDamage(self, damage):
        self.__magicDamage = damage
    
    def calculateMagicDamage(self, primaryMaterial, catalystMaterial):
        damage = (primaryMaterial.strength * primaryMaterial.magicPower + catalystMaterial.strength * catalystMaterial.magicPower)

        return damage
    
    def useEffect(self):
        return f'{self.__name} enchantment and {self.__effect}'

# Create a workshop, forge, enchanter.
workshop = Workshop(Forge(), Enchanter())

# Create a set of materials and lists for testing.
materials = [Maple(), Oak(), Ash(), Bronze(), Iron(), Steel(),
    Ruby(), Sapphire(), Emerald(), Diamond(), Amethyst(), Onyx()]

weaponBlueprints = {
    "Sword": [Steel(), Maple()],
    "Shield": [Bronze(), Oak()],
    "Axe": [Iron(), Ash()],
    "Scythe": [Steel(), Ash()],
    "Bow": [Oak(), Maple()],
    "Wand": [Ash(), Oak()],
    "Staff": [Bronze(), Maple()],
    "Dagger": [Bronze(), Bronze()]}

enchantmentBlueprints = {
    "Holy": [Diamond(), Diamond()],
    "Lava": [Ruby(), Onyx()],
    "Pyro": [Ruby(), Diamond()],
    "Darkness": [Onyx(), Amethyst()],
    "Cursed": [Onyx(), Onyx()],
    "Hydro": [Sapphire(), Emerald()],
    "Venomous": [Emerald(), Amethyst()],
    "Earthly": [Emerald(), Emerald()]}

enchantedWeapons = ["Holy Greatsword", "Molten Defender", "Berserker Axe", "Soul Eater",
    "Twisted Bow", "Wand of the Deep", "Venemous Battlestaff"]

# Adds a number of materials to use for crafting.
for material in materials:
    if isinstance(material, Wood):
        workshop.addMaterial(material.__class__.__name__, 20)
    elif isinstance(material, Metal):
        workshop.addMaterial(material.__class__.__name__, 10)
    else:
        workshop.addMaterial(material.__class__.__name__, 5)

print("--------------------------------Material Store--------------------------------")
print(workshop.displayMaterials())

# Crafts the following: Sword, Shield, Axe, Scythe, Bow, Wand and Staff weapons.
for weapon, materials in weaponBlueprints.items():
    craftedWeapon = workshop.forge.craft(
        weapon, materials[0], materials[1], workshop.materials)
    workshop.addWeapon(craftedWeapon)

# Disassemble the extra weapon.'
workshop.removeWeapon(workshop.forge.disassemble(
    workshop.weapons[7], workshop.materials))

print("------------------------------------Armoury-----------------------------------")
print(workshop.displayWeapons())

# Crafts the following: Holy, Lava, Pyro, Darkness, Cursed, Hydro and Venomous enchantments.
for enchantment, materials in enchantmentBlueprints.items():
    craftedEnchantment = workshop.enchanter.craft(
        enchantment, materials[0], materials[1], workshop.materials)
    workshop.addEnchantment(craftedEnchantment)

# Disassemble the extra enchantment.
workshop.removeEnchantment(workshop.enchanter.disassemble(
    workshop.enchantments[7], workshop.materials))

print("------------------------------------Enchantments------------------------------------")
print(workshop.displayEnchantments())

print("-----------------------------------Material Store-----------------------------------")
print(workshop.displayMaterials())

# Enchant the following weapons: Sword, Shield, Axe, Scythe, Bow, Wand and Staff.
for i in range(len(enchantedWeapons)):
    workshop.enchanter.enchant(
        workshop.weapons[i], enchantedWeapons[i], workshop.enchantments[i])
    
print("-----------------------------------Enchanted Armoury----------------------------------")
print(workshop.displayWeapons())