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
        
        for  weapon in self.__weapons: 
            if weapon.enchantment: 
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
    def craft(self): # implementation of the craft method
        pass
    
    def disassemble(self): # implemenetation of the disassemble method
        pass

class Weapon:
    def __init__(self, primaryMaterial, catalystMaterial):
        self.__primaryMaterial = primaryMaterial
        self.__catalystMaterial = catalystMaterial
        self.__damage = 0
        self.__enchantment = None
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
    
    def calculateDamage(self, primaryMaterial, cataystMaterial):

        if isinstance(primaryMaterial, Wood) and isinstance(cataystMaterial, Wood):
            damage = primaryMaterial.strength * cataystMaterial.strength

        elif isinstance (primaryMaterial, Metal) and isinstance(cataystMaterial, Metal):
            damage = (primaryMaterial.strength * primaryMaterial.purity) + (cataystMaterial.strength * cataystMaterial.purity)
        
        elif isinstance (primaryMaterial, Wood) and isinstance(cataystMaterial, Metal):
            damage = primaryMaterial.strength * (cataystMaterial.strength * cataystMaterial.purity)
        else:
            damage = cataystMaterial * (primaryMaterial.strength * primaryMaterial.purity)
        
        return damage

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
        

        
