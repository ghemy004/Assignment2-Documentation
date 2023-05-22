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
    
    def addMaterial(self, material):
        self.materials.append(material)
    
    def removeMaterial(Self, material):
        self.materials.remove(material)
    
    def addWeapon(self, weapon):
        self.weapons.append(weapon)
    
    def removeWeapon(Self, weapon):
        self.weapons.remove(weapon)
    
    def addEchantment(self,echantment):
        self.enchantment.append(echantment)

    def removeEchantment(self, enchantment):
        self.enchantment.remove(enchantment)
    
    def displayWeapons(self):




    
    




  