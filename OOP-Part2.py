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
    def __init__(self, enchanter, forge): # 
        self.__forge = forge
        self.__enchanter = enchanter
        self.__materials = []
        self.__weapons = []
        self.__enchantment = [] 
    
    # this method takes material as a parameter and adds it to the material 
    def addMaterial(self, material):
        self.__materials.append(material)
    
    def removeMaterial(self, material):
        self.__materials.remove(material)
    
    # this method takes weapon as a parameter and adds it to the weapons list
    def addWeapon(self, weapon):
        self.__weapons.append(weapon)
        
    def removeWeapon(self, weapon):
        self.__weapons.remove(weapon)
    
    # this method takes echantment as a parameter and adds it to the echantment list
    def addEchantment(self,echantment):
        self.__enchantment.append(echantment)

    def removeEchantment(self, enchantment):
        self.__enchantment.remove(enchantment)

    def displayWeapons(self):
        result = '' 
        
        for  weapon in self.__weapons: # iterates over each weapon in sel.__weapons list
            if weapon.enchantment: # checks if weapon has an enchantment by using this in the conditional statement 
                enchantmentDetails = f"The {weapon.enchantment.useEffect()}"
            else:
                enchantmentDetails = f"{self.__weapons} is not enchanted"
                        
            weaponDetails = f'The {weapon.name} is {enchantmentDetails}. It deals {weapon.attack()} damage.\n'
            
            result += weaponDetails
        return result
    
# Display enchantments
    def displayEnchantments(self):
        enchantmentNames = []
        
        for enchantment in self.__enchantment:
            enchantmentNames.append('A {} enchantment is stored in workshop.'.format(enchantment.getName()))

        return '\n'.join(enchantmentNames)  

class Crafter(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def craft(self): # implementation of the craft method
        pass

    @abstractmethod    
    def disassemble(self): # implemenetation of the disassemble method
        pass

        


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

# Disassemble the extra weapon.
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