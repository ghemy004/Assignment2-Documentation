from abc import ABC, abstractmethod

import Material

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


class Forge(Crafter):
    def __init__(self):
        
        





materials[primaryMaterial.__class__.__name__] -= 1
materials[catalystMaterial.__class__.__name__] -= 1
materials[primaryMaterial.__class__.__name__] += 1
materials[catalystMaterial.__class__.__name__] += 1