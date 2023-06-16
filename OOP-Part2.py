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


'''
the workshop class represents the workshop it's self, it takes forge and enchanter as attributes.
'''
class Workshop: 
    def __init__(self, forge, enchanter): # 
        self.forge = forge
        self.enchanter = enchanter
        self.materials = {}
        self.weapons = []
        self.enchantments = [] 
    
    def addMaterial(self, material, num):
        self.materials[material] = num
    
    def removeMaterial(self, material):
        del self.materials[material]
    
    def addWeapon(self, weapon):
        self.weapons.append(weapon)
        
    def removeWeapon(self, weapon):
        self.weapons.remove(weapon)
    
    def addEnchantment(self,enchantment):
        self.enchantments.append(enchantment)

    def removeEnchantment(self, enchantment):
        self.enchantments.remove(enchantment)

    '''
    this displayWeapons is reponsible for displaying the information about the weapons stored within the workshop class.
    '''
    def displayWeapons(self):
        enchantmentDetails = ""

        for weapon in self.weapons: 
            
            if weapon.getEnchanted() == True: 

                enchantmentDetails += f'The {weapon.Name} is imbued with a {weapon.getEnchantment().useEffect()}. {weapon.Attack}'
            else:
                enchantmentDetails += f"{weapon.Name} is not enchanted. {weapon.Attack}"

        return enchantmentDetails
    
    '''
    this displayEnchantments is reponsible for displaying information about the enchantments stored in the workshop class.
    it generates a string that includes the names of the enchantments stored, each enchantment name is listed on a separate line.
    '''
    def displayEnchantments(self):
        enchantmentNames = []
        
        for enchantment in self.enchantments:
            enchantmentNames.append('A {} enchantment is stored in workshop.'.format(enchantment.getName()))

        return '\n'.join(enchantmentNames)  
    
    '''
    this displayMaterials is responsible for displaying information about the materials stored in the workshop
    is basically generates a string that includes the names of the materials and the amount remaining for each material stored within the workshop
    '''
    def displayMaterials(self):
        materialDisplay = ""

        for material in self.materials:
            materialDisplay += f"{material}: {self.materials[material]} remaining.\n"

        return materialDisplay
    
'''
the Crafter class is an abstract class, this class defines abstract method craft() and disassemble()
'''
class Crafter(ABC):
    def __init__(self):
        pass

    '''
    the craft method below is an abstract method, that is declared but does not have any implementations.
    '''        
    @abstractmethod
    def craft(self): 
        pass
    '''
    this is another abstract method, it also does not have an implementation within this class.
    '''
    @abstractmethod
    def disassemble(self): 
        pass
'''
the weapon class reprsents a weapon, taking mutliple attributes such as primary material, cataylst material, damage etc...
this class holds the methods to calculate damage based on the materials used and then performs an attack
'''
class Weapon:
    def __init__(self, name, primaryMaterial, catalystMaterial):
        self.__primaryMaterial = primaryMaterial
        self.__catalystMaterial = catalystMaterial
        self.__damage = 0
        self.__enchantment = ''
        self.__enchanted = False
        self.__name = name
        
    
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
    
    '''
    this calculateDamage method, is reponsible for calculating the damage value of a weapon based on it's primary and catalyst materials.
    it determines the damage value of a weapon based on the combination of the primary and cataylst material.
    '''
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
    
    '''
    this attack method is responsible for providing a text display representation of the damage dealt by a weapon
    '''
    def attack(self):
        return f"It deals {self.getDamage():.2f} damage.\n"
    
    Name = property(getName,setName)
    PrimaryMaterial = property(getPrimaryMaterial)
    CatalystMaterial = property(getCatalystMaterial)
    damage = property(getDamage)
    Attack = property(attack)
    
'''
Forge being the subclass of crafter it reprsents a crafter that's specialized in weapon forging.
this class implements the craft() and disassemble() methods
'''
class Forge(Crafter):
    def __init__(self):
        pass
    
    '''
    the craft method is inherited from the crafter abstract class, this method is responsible for crafting a new weapon by combining a primary and catalyst material
    it creates a new instance of a weapon, calculates its damage and sets the name of the weapon and updates the material count within the workshop.
    '''
    def craft(self, name, primaryMaterial, catalystMaterial, materials):
        weapon = Weapon(name, primaryMaterial, catalystMaterial)
        weapon.setDamage(weapon.calculateDamage(primaryMaterial, catalystMaterial))
        #weapon.setName(name)

        materials[primaryMaterial.__class__.__name__] -= 1
        materials[catalystMaterial.__class__.__name__] -= 1

        return weapon
    '''
    this method is also inherited from the crafter abstract class, it is responsible for disassembling a weapon and retrieving it's primary and catalyst materials
    it updates the materials counts in the workshop aswell
    '''
    def disassemble(self, weapon, materials):
        primaryMaterial = weapon.PrimaryMaterial
        catalystMaterial = weapon.CatalystMaterial

        materials[primaryMaterial.__class__.__name__] += 1
        materials[catalystMaterial.__class__.__name__] += 1 
        return weapon

'''
Enchanter being another subclass of crafter it represents a crafter specialized in enchanting weapons.
This class also implements the craft() and disassemble() methods.
'''     
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
    
    '''
    the craft method within this enchanter class, is inherited from the crafter abstract class, it is responsible for crafting new enchantments by combining primary and catalyst material
    creates a new instance of an enchantment, sets its effects and magic damage and returns the crafted enchantment
    '''  
    def craft(self, name, primaryMaterial, catalystMaterial, materials):
        materials[primaryMaterial.__class__.__name__] -= 1
        materials[catalystMaterial.__class__.__name__] -= 1 
        enchantment = Enchantment(name, primaryMaterial, catalystMaterial)
        enchantment.setEffect(self.recipes[name])
        enchantment.setMagicDamage(enchantment.calculateMagicDamage(primaryMaterial, catalystMaterial))
        return enchantment
    '''
    also inherited from crafter abstract class, it is responsible for disassembling an existing enchantment and returning the primary and catylst materials used
    it retrieves the primary and cataylst materials from the enchantment and it adds the material count in the workshop and returns the disassembled enchantment
    '''
    def disassemble(self, enchantment, materials):
        primaryMaterial = enchantment.primaryMaterial
        catalystMaterial = enchantment.catalystMaterial

        materials[primaryMaterial.__class__.__name__] += 1
        materials[catalystMaterial.__class__.__name__] += 1 
        return enchantment
    
    '''
    this Enchant method is used to apply an enchantment to a weapon and modifying it's properties. 
    '''
    def enchant(self, weapon, newName, enchantment):
        weapon.setEnchanted(True)
        weapon.setEnchantment(enchantment)
        weapon.setDamage(weapon.damage * enchantment.magicDamage)
        weapon.setName(newName)

        return weapon
        
'''
this enchantment class represents enchantment, has attributes such as name, damage, effect and materials.
this class also stores methods to caclulate magic damage and to display the effects of enchantment
'''
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
    
    '''
    it is responsible for calculating the magic damage caused by the enchantment based on the strength and magic power of the primary and catlyst materials used
    it calculates the magic damaged caused by the enchantment based on the strength and magic power 
    '''
    def calculateMagicDamage(self, primaryMaterial, catalystMaterial):
        damage = (primaryMaterial.strength * primaryMaterial.magicPower + catalystMaterial.strength * catalystMaterial.magicPower)

        return damage
    '''
    the useEffect is responsible for returning a string of the effect produced by the enchantment when it is exacuted
    it takes the name and effect of enchantment and returns a string explaining the effect done by the enchantment that's being used.
    '''
    def useEffect(self):
        return f'{self.__name} enchantment and {self.__effect}'
    
    primaryMaterial = property(getPrimaryMaterial)
    catalystMaterial = property(getCatalystMaterial)
    magicDamage = property(getMagicDamage)

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


