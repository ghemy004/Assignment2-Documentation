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
        self.forge = forge
        self.enchanter = enchanter
        self.materials = []
        self.weapons = []
        self.enchantment = [] 
    
    # this method takes material as a parameter and adds it to the material 
    def addMaterial(self, material):
        self.materials.append(material)
    
    def removeMaterial(self, material):
        self.materials.remove(material)
    
    # this method takes weapon as a parameter and adds it to the weapons list
    def addWeapon(self, weapon):
        self.weapons.append(weapon)
        
    def removeWeapon(self, weapon):
        self.weapons.remove(weapon)
    
    # this method takes echantment as a parameter and adds it to the echantment list
    def addEchantment(self,echantment):
        self.enchantment.append(echantment)

    def removeEchantment(self, enchantment):
        self.enchantment.remove(enchantment)
  
    def displayWeapons(self): 
        value = " "
        for weapon in self.weapons:
            if weapon.enchantment:
                value += "The {} is imbued with a {}. {}\n".format(weapon.name, weapon.echantment.useEffect(), weapon.attack())
            else:
                value += "The {} is not enchanted. {}\n".format(weapon.name, weapon.attack()) 
        return value

