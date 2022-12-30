import random
import time
#END OF IMPORTS---------------------------------------------------------------------------------
DummyNumber=["one","two"]
DummyRewardListWeapon=["one","two","three","four","five"]
DummyRewardListMagic=["one","two","three","four","five"]
DummyRewardListArmour=["one","two","three","four"]
SkelotonRewardListWeapon=["one","two","three","four","five"]
SkelotonRewardListMagic=["one","two","three","four"]
DummyRewardListArmour=["one","two","three"]
DragonMoveNumber=["one","two","three"]
DragonRewardListWeapon=["one","two","three","four","five"]
DragonRewardListMagic=["one","two","three","four","five"]
DragonRewardListArmour=["one","two","three","four"]
BossMoveNumber=["one","two","three","four","five"]
#END OF RANDOM NUMBER LISTS----------------------------
DummyAttacks = {"Nothing": 0, "Fell": 1}
SkelotonWarriorAttacks={"Sword":18}
DragonAttacks={"Tail Whip":45, "Fire Breath":70}
DragonMagic={"Magic":40}
BossAttacks={"Confusion Curse":65,"Fire Spell":70,"Lightning Spell":90}
BossMagic={"Magic":55, "Super Magic": 100}
Weapons = {"Basic Short Sword": 15, "Basic Spear": 20, "Basic Dagger": 10, "Basic Broad Sword": 25,"Improved Short Sword": 35, "Improved Spear": 30, "Improved Dagger": 40, "Improved Broad Sword": 45,"Dragon Short Sword": 70, "Dragon Spear": 75, "Dragon Dagger": 60, "Dragon Broad Sword": 65, "Dragon Cannon": 100}
#end of weopns lists
Magic = {"Basic Crystal Necklace": 5, "Basic Wand": 10, "Basic Amulet": 15, "Basic Gem Stone": 20,"Improved Cystal Necklace": 25, "Improved Wand": 35, "Improved Amulet": 30, "Improved Gem Stone": 40,"Dragon Fire Necklace": 45, "Dragon Horn Wand": 50, "Dragon Amulet": 55, "Dragon Fire Gem Stone": 60, "Dragon Staff": 75}
# end of magic items
Armour = {"Basic Sheild": 5, "Basic Chainmail": 10, "Basic Full Body Armour": 15,"Improved Sheild":30, "Improved Chainmail": 45, "Improved Full Body Armour": 50,"Dragon Scale Sheild": 55, "Dragon Chain Mail": 60, "Full Body Dragon Armour":65, "Full Body Armour with Dragon Scale Sheild": 120}

#END OF LISTS-------------------------------------------------

class Character():
  def __init__(self, name, attack, magic, defense, health):
    self.name = name
    self.attack = attack
    self.magic = magic
    self.defense = defense
    self.health = health
    
  def nameCheck(self):
     print(self.name.title())


class Dummy():
  def __init__(self, name, attackone, attacktwo, health):
    self.name = name
    self.attackone = attackone
    self.attacktwo = attacktwo
    self.health = health
class Skeloton():
  def __init__(self, name, attack, health):
    self.name = name
    self.attack = attack
    self.health = health

class Dragon():
  def __init__(self, name, attackOne, attackTwo, magic, health):
    self.name = name
    self.attackOne = attackOne
    self.attackTwo = attackTwo
    self.magic = magic 
    self.health = health
class Boss():
  def __init__(self,name, attackOne, attackTwo, attackThree, magicOne, magicTwo, health):
    self.name = name
    self.attackOne = attackOne
    self.attackTwo = attackTwo
    self.attackThree = attackThree
    self.magicOne = magicOne
    self.magicTwo = magicTwo
    self.health = health
#CLASSSES AREA------------------------------------------------

    
print("WELCOME TO THE WOLRD OF DUNGEONS, DUNGEONS, AND MORE DUNGEONS. MY NAME IS THE WIZARD OZ, AND I WILL BE YOUR GUIDE.(I will only address you in all caps)")
print(" ")
time.sleep(2.5)
print("IT IS TIME FOR YOU TO START YOUR JOURNY, BUT FIRST WHAT IS YOUR NAME?")
UserName = input()
UserWeapon = Weapons["Basic Short Sword"]
UserMagic = Magic["Basic Crystal Necklace"]
UserDefense = Armour["Basic Sheild"]
UserHealth = 100
UserCharacter = Character(UserName, UserWeapon, UserMagic, UserDefense, UserHealth)
# WEAPON CHECKIN / SWITHCING MUST BE DONE OUT SIDE OF CLASS
def weaponCheck(UserWeapon):
    if UserWeapon == Weapons["Basic Short Sword"]:
      UserWeaponName = "Basic Short Sword"
      print(UserWeaponName)
    elif UserWeapon == Weapons["Basic Spear"]:
      UserWeaponName = "Basic Spear"
      print(UserWeaponName)
    elif UserWeapon == Weapons["Basic Dagger"]:
      UserWeaponName = "Basic Dagger"
      print(UserWeaponName)
    elif UserWeapon == Weapons["Basic Broad Sword"]:
      UserWeaponName = "Basic Broad Sword"
      print(UserWeaponName)
    elif UserWeapon == Weapons["Improved Short Sword"]:
      UserWeaponName = "Improved Short Sword"
      print(UserWeaponName)
    elif UserWeapon == Weapons["Improved Spear"]:
      UserWeaponName = "Improved Spear"
      print(UserWeaponName)
    elif UserWeapon == Weapons["Improved Dagger"]:
      UserWeaponName = "Improved Dagger"
      print(UserWeaponName)
    elif UserWeapon == Weapons["Improved Broad Sword"]:
      UserWeaponName = "Improved Broad Sword"
      print(UserWeaponName)
    elif UserWeapon == Weapons["Dragon Short Sword"]:
      UserWeaponName = "Dragon Short Sword"
      print(UserWeaponName)
    elif UserWeapon == Weapons["Dragon Spear"]:
      UserWeaponName = "Dragon Spear"
      print(UserWeaponName)
    elif UserWeapon == Weapons["Dragon Dagger"]:
      UserWeaponName = "Dragon Dagger"
      print(UserWeaponName)
    elif UserWeapon == Weapons["Dragon Broad Sword"]:
      UserWeaponName = "Dragon Broad Sword"
      print(UserWeaponName)
    elif UserWeapon == Weapons["Dragon Cannon"]:
      UserWeaponName = "Dragon Cannon"
      print(UserWeaponName)
#END OF WEAPONS CHECK FUNCTION--------------------------------
def magicCheck(UserMagic):
  if UserMagic == Magic["Basic Crystal Necklace"]:
    UserMagicName = "Basic Crystal Necklace"
    print(UserMagicName)
  elif UserMagic == Magic["Basic Wand"]:
    UserMagicName = "Basic Wand"
    print(UserMagicName)
  elif UserMagic == Magic["Basic Amulet"]:
    UserMagicName = "Basic Amulet"
    print(UserMagicName)
  elif UserMagic == Magic["Basic Gem Stone"]:
    UserMagicName = "Basic Gem Stone"
    print(UserMagicName)
  elif UserMagic == Magic["Improved Cystal Necklace"]:
    UserMagicName = "Improved Cystal Necklace"
    print(UserMagicName)
  elif UserMagic == Magic["Improved Wand"]:
    UserMagicName = "Improved Wand"
    print(UserMagicName)
  elif UserMagic == Magic["Improved Amulet"]:
    UserMagicName = "Improved Amulet"
    print(UserMagicName)
  elif UserMagic == Magic["Improved Gem Stone"]:
    UserMagicName = "Improved Gem Stone"
    print(UserMagicName)
  elif UserMagic == Magic["Dragon Fire Necklace"]:
    UserMagicName = "Dragon Fire Necklace"
    print(UserMagicName)
  elif UserMagic == Magic["Dragon Horn Wand"]:
    UserMagicName = "Dragon Horn Wand"
    print(UserMagicName)
  elif UserMagic == Magic["Dragon Amulet"]:
    UserMagicName = "Dragon Amulet"
    print(UserMagicName)
  elif UserMagic == Magic["Dragon Fire Gem Stone"]:
    UserMagicName = "Dragon Fire Gem Stone"
    print(UserMagicName)
  elif UserMagic == Magic["Dragon Staff"]:
    UserMagicName = "Dragon Staff" 
    print(UserMagicName)
# END OF MAGIC FUNCTION -------------------------------------

def defenceCheck(UserDefense):
  if UserDefense == Armour["Basic Sheild"]:
    UserDefenseName = "Basic Sheild"
    print(UserDefenseName)
  elif UserDefense == Armour["Basic Chainmail"]:
    UserDefenseName = "Basic Chainmail"
    print(UserDefenseName)
  elif UserDefense == Armour["Basic Full Body Armour"]:
    UserDefenseName = "Basic Full Body Armour"
    print(UserDefenseName)
  elif UserDefense == Armour["Improved Sheild"]:
    UserDefenseName = "Improved Sheild"
    print(UserDefenseName)
  elif UserDefense == Armour["Improved Chainmail"]:
    UserDefenseName = "Improved Chainmail"
    print(UserDefenseName)
  elif UserDefense == Armour["Improved Full Body Armour"]:
    UserDefenseName = "Improved Full Body Armour"
    print(UserDefenseName)
  elif UserDefense == Armour["Dragon Scale Sheild"]:
    UserDefenseName = "Dragon Scale Sheild"
    print(UserDefenseName)
  elif UserDefense == Armour["Dragon Chain Mail"]:
    UserDefenseName = "Dragon Chain Mail"
    print(UserDefenseName)
  elif UserDefense == Armour["Full Body Dragon Armour"]:
    UserDefenseName = "Full Body Dragon Armour"
    print(UserDefenseName)
  elif UserDefense == Armour["Full Body Armour with Dragon Scale Sheild"]:
    UserDefenseName = "Full Body Armour with Dragon Scale Sheild"
    print(UserDefenseName)
#END OF DEFENSE / ARMOUR CHECK---------------------------
def healthCheck(UserHealth):
  print("Your health : "+str(UserHealth))
#END OF HELTH CHECK-------------------------------------
def statCheck():
  print(" ")
  print("YOUR CHARACTER STATS:")
  UserCharacter.nameCheck()
  weaponCheck(UserWeapon)
  print(str(UserWeapon)+" Attack Points.")
  magicCheck(UserMagic)
  print(str(UserMagic)+" Health Points.")
  defenceCheck(UserDefense)
  print(str(UserDefense)+" Defense Points")
  healthCheck(UserHealth)
  print(" ")
#END OF STAT CHECK--------------------------------
statCheck()
time.sleep(1)
print("ABOVE YOU WILL SEE YOUR CHARACTER STATS!")
print(" ")
time.sleep(2)
print("THE FIRST LINE IS ALWAYS YOUR NAME")
print(" ")
time.sleep(3)
print("THEN THE NEXT LINE STATES YOUR CURRENTLY EQIPED WEAPON. IT'S ATTACK POINTS ARE UNDER IT WHICH YOU WILL USE TO ATTACK YOUR ENEMIES.")
print(" ")
time.sleep(3.5)
print("THE NEXT LINE SHOWS YOU YOUR CURRENT MAGICAL ITEM. WHEN USED, THE ITEM GIVES YOU BACK THE NUMBER OF HEALTH POINTS UNDER IT'S NAME.")
print(" ")
time.sleep(3.5)
print("THE NEXT LINE SHOWS YOU YOUR CURRENT ARMOUR AND HOW MUCH PROTECTION IT GIVES YOU. IF YOUR PROTECION IS HIGHER THEN THE ENEMY'S ATTACK THEY WILL RECIVE THE DAMAGE INSTEAD. ")
time.sleep(5.5)
print(" ")
print("LETS GET YOU TRAINNED ON THE MAGICAL TRAINNING DUMMY!")
time.sleep(2)
print(" ")
print("The Dummy has two moves it can do nothing or it can fall on you and do 1 attack point of damage.")
time.sleep(2.5)
DummyName = "Training Dummy"
DummyFirstAttack = DummyAttacks["Nothing"]
DummySecondAttack = DummyAttacks["Fell"]
DummyHealth = 60#CHANGE THIS BEFORE SUBMITION!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
MagicDummy = Dummy(DummyName, DummyFirstAttack, DummySecondAttack, DummyHealth)
#THE GAME BEGINS----------------------------------------
def dummyHealthCheck(DummyHealth):
  print("The Training Dummy's total health: "+str(DummyHealth))
while DummyHealth > 0:  
  if UserHealth > 0 :
    dummyHealthCheck(DummyHealth)
    statCheck()
    print(" ")
    print("Enter 1 to attack or type 2 to use your magic")
    print(" ")
    DummyActionAnswer = input() 
    if DummyActionAnswer == "1":
      DummyHealth = DummyHealth - UserWeapon
      print("You have attacked the Dummy with your weapon. Now it is their turn to attack.")
      time.sleep(2)
      if DummyHealth>0: 
        DummyMoveNumber = random.randint(0,1)
        print(" ")
        time.sleep(1)
        if DummyMoveNumber == 0:
          print("The Training Dummy Did nothing so you did not lose any health.")
          time.sleep(2)
        elif DummyMoveNumber == 1: 
          DummyTotalAttack = DummySecondAttack - UserDefense
          print("The Dummy fell on you")
          time.sleep(2)
          if DummyTotalAttack<0:
            print("Because your Armour is stronger than the Dummy's attack they will recive any damage intended to hit you.")
            time.sleep(2.5)
            DummyHealth = DummyHealth - DummySecondAttack
            if DummyHealth<0:
              print("The Dummy has been defeated.")
              time.sleep(2)
            else:
              continue 
          else:
            UserHealth = UserHealth - DummyTotalAttack
            #This line will never logically be used but it's good to have as a referance line.
            print(DummyHealth)
            if DummyHealth<0:
              print("The Dummy has been defeated.")
              break
      elif DummyHealth<0:
        print("The Dummy has been defeated!")
        break
    elif DummyActionAnswer == "2":
      print("You have decided to use your Magic to heal yourself")
      time.sleep(2)
      UserHealth = UserHealth + UserMagic
      print(UserHealth)
      print("Now it is the Dummy's turn to attack.")
      time.sleep(2)
      if DummyHealth>0:
        DummyMoveNumber = random.randint(0,1)
        print(" ")
        time.sleep(1)
        if DummyMoveNumber == 0:
          print("The Training Dummy Did nothing so you did not lose any health.")
          time.sleep(2)
        elif DummyMoveNumber == 1:
          DummyTotalAttack = DummySecondAttack - UserDefense
          if DummyTotalAttack<0:
            print("Because your Armour is stronger than the Dummy's attack they will recive any damage intended to hit you.")
            time.sleep(2.5)
            DummyHealth = DummyHealth - DummySecondAttack
            if DummyHealth<=0:
              print("The Dummy has been defeated.")
              break
            else:
              continue 
          else:
            UserHealth = UserHealth - DummyTotalAttack
            #This line will never logically be used but it's good to have as a referance line.
            print(DummyHealth)
            if DummyHealth<=0:
              print("The Dummy has been defeated.")
              break
      elif DummyHealth<=0:
        print("The Dummy has been defeated!")
        break
print(" ")
print("GREAT WORK YOUNG WARIOR! NOW IT IS TIME TO PICK YOUR REWARDs!")
print(" ")
time.sleep(2)
print("YOU WILL HAVE THE CHANCE TO EQUIP ONE NEW RANDOM WEAPON, MAGICAL ITEM, AND PERICE OF ARMOUR.")
print(" ")
time.sleep(2.5)
print(" LET'S START WITH THE WEAPON.")
print(" ")
DummyRewardNumberWeapon = random.randint(0,4)
if DummyRewardNumberWeapon == 0: 
  DummyRewardWeapon = Weapons["Basic Short Sword"]
  DummyRewardNameWeapon = "Basic Short Sword"
  DRWattackPoints = "15"
elif DummyRewardNumberWeapon == 1:
  DummyRewardWeapon = Weapons["Basic Spear"]
  DummyRewardNameWeapon = "Basic Spear"
  DRWattackPoints = "20"
elif DummyRewardNumberWeapon == 2:
  DummyRewardWeapon = Weapons["Basic Dagger"]
  DummyRewardNameWeapon = "Basic Dagger"
  DRWattackPoints = "10"
elif DummyRewardNumberWeapon == 3:
  DummyRewardWeapon = Weapons["Basic Broad Sword"]
  DummyRewardNameWeapon = "Basic Broad Sword"
  DRWattackPoints = "25"
elif DummyRewardNumberWeapon == 4:
  DummyRewardWeapon = Weapons["Improved Short Sword"]
  DummyRewardNameWeapon = "Improved Short Sword"
  DRWattackPoints = "35"
time.sleep(2)
print("The weapon you have found is a "+str(DummyRewardNameWeapon)+", it has "+str(DRWattackPoints)+" attack points. If you want the weapon enter 1 to claim it or hit enter to recive a 25 point health increast")
UserDummyWeaponChoice = input()
if UserDummyWeaponChoice == "1":
  UserWeapon = DummyRewardWeapon
  weaponCheck(UserWeapon)
  statCheck()
else:
  DummyHealthReward = 25
  UserHealth = UserHealth + DummyHealthReward
  healthCheck(UserHealth)
  statCheck()
print("YOUR STATS HAVE BEEN UPDATED!")
print(" ")
time.sleep(2)
#DO item swithichng outside of funtions, it's more code but it works cleaner.
print("NOW LET'S TALK ABOUT A NEW MAGICAL ITEM.")
DummyRewardNumberMagic = random.randint(0,4)
if DummyRewardNumberMagic == 0: 
  DummyRewardMagic = Magic["Basic Crystal Necklace"]
  DummyRewardMagicName = "Basic Crystal Necklace"
  DRMpoints = "5"
elif DummyRewardNumberMagic == 1:
  DummyRewardMagic = Magic["Basic Wand"]
  DummyRewardMagicName = "Basic Wand"
  DRMpoints = "10"
elif DummyRewardNumberMagic == 2:
  DummyRewardMagic = Magic["Basic Amulet"]
  DummyRewardMagicName = "Basic Amulet"
  DRMpoints = "15"
elif DummyRewardNumberMagic == 3:
  DummyRewardMagic = Magic["Basic Gem Stone"]
  DummyRewardMagicName = "Basic Gem Stone"
  DRMpoints = "20"
elif DummyRewardNumberMagic == 4:
  DummyRewardMagic = Magic["Improved Cystal Necklace"]
  DummyRewardMagicName = "Improved Cystal Necklace"
  DRMpoints = "25"
print(" ")
time.sleep(2)
print("The magical item you have found is a "+str(DummyRewardMagicName)+", it has "+str(DRMpoints)+" health points. If you want to equip it type 1,if you do not hit enter and you will receive a 25 point health increase.")
UserDummyMagicChoice = input()
if UserDummyMagicChoice == "1":
  UserMagic = DummyRewardMagic
  magicCheck(UserMagic)
  statCheck()
else:
  DummyHealthReward = 25
  UserHealth = UserHealth + DummyHealthReward
  healthCheck(UserHealth)
  statCheck()
print("YOUR STATS HAVE BEEN UPDATED!")
time.sleep(2)
print(" ")
print("THE FINAL ITEM YOU CAN HAVE IS ARMOUR.")
DummyRewardNumberArmour = random.randint(0,3)
if DummyRewardNumberArmour == 0:
  DummyRewardArmour = Armour["Basic Sheild"]
  DummyRewardArmourName = "Basic Sheild"
  DMApoints = "5"
elif DummyRewardNumberArmour == 1:
  DummyRewardArmour = Armour["Basic Chainmail"]
  DummyRewardArmourName = "Basic Chainmail"
  DMApoints = "10"
elif DummyRewardNumberArmour == 2:
  DummyRewardArmour = Armour["Basic Full Body Armour"]
  DummyRewardArmourName = "Basic Full Body Armour"
  DMApoints = "15"
elif DummyRewardNumberArmour == 3:
  DummyRewardArmour = Armour["Improved Sheild"]
  DummyRewardArmourName = "Improved Sheild"
  DMApoints = "30"
print(" ")
time.sleep(2)
print("The peice of armour you have found is a "+str(DummyRewardArmourName)+", and it has "+str(DMApoints)+" defense points. If you want to equip it type 1 or hit enter to receave a 25 point health increase.")
UserDummyArmourChoice = input()
if UserDummyArmourChoice == "1":
  UserDefense = DummyRewardArmour
  defenceCheck(UserDefense)
  statCheck()
else:
  DummyHealthReward = 25
  UserHealth = UserHealth + DummyHealthReward
  healthCheck(UserHealth)
  statCheck()
print("YOUR STATS HAVE BEEN UPDATED!")
print(" ")
time.sleep(2)
print("CONGRATULATIONS! YOU HAVE COMPLEATED THE TUTORIAL.")
#END OF TUTORIAL----------------------------------------------------------------------------------------------------------------
print(" ")
time.sleep(2)
print("THERE WILL BE 3 ENIMIES YOU WILL HAVE TO FACE. THE FIRST ENEMY WILL BE EASY DIFFICULTY, THE SECOND ENEMY WILL BE MEDIUM DIFFICULTY, AND THIRD ENEMY YOU WILL FACE WILL BE THE FINAL BOSS!")
time.sleep(3)
print(" ")
print("LET THE GAME BEGIN!")
time.sleep(1.5)
SkelotonName = "Skeloton Warrrior"
SkelotonAttack = SkelotonWarriorAttacks["Sword"]
SkelotonHealth = 125
SkelotonWarrior = Skeloton(SkelotonName, SkelotonAttack, SkelotonHealth)
print(" ")
print("THE FIRST ENEMY THAT YOU WILL ENCOUNTER IS A SKELOTON WARRIOR! THIS ENEMY'S TOTAL HEALTH is 125. THE ONLY MOVE IT HAS IS IT'S SWORD WHICH HAS 18 ATTACK POINTS.")
time.sleep(4)
print(" ")
print("GOOD LUCK!")
time.sleep(1.5)
def getSkelotonHealth(SkelotonHealth):
  print("The Skeloton Warrior's total health: "+str(SkelotonHealth))
getSkelotonHealth(SkelotonHealth)
while SkelotonHealth > 0:
  if UserHealth > 0 :
    print(" ")
    getSkelotonHealth(SkelotonHealth)
    print(" ")
    statCheck()
    print(" ")
    print("Enter 1 to attack or type 2 to use your magic")
    UserSkelotonAction = input()
    if UserSkelotonAction == "1":
      SkelotonHealth = SkelotonHealth - UserWeapon
      print(" ")
      print("You have attacked the Skeloton Warrior with your weapon. Now it is the Skeloton Warrior's turn to attack.")
      print(" ")
      time.sleep(2.5)
      if SkelotonHealth > 0:
        SkelotonTotalAttack = SkelotonAttack - UserDefense
        if SkelotonTotalAttack < 0: 
          print("Your armour is stronger than your opponent's attack, so they will recive the damage.")
          time.sleep(2.5)
          print(" ")
          SkelotonHealth = SkelotonHealth - SkelotonAttack
        elif SkelotonTotalAttack > 0: 
          print("Your armour is not stronger than your oponent's att but it will shield you from some of the damage. You will only lose "+str(SkelotonTotalAttack)+" health points")
          print(" ")
          time.sleep(3)
          UserHealth = UserHealth - SkelotonTotalAttack
      elif SkelotonHealth <= 0:
        print("YOU HAVE DEFEATED THE SKELOTON WARRIOR!")
        key = "yes"
        break
    elif UserSkelotonAction == "2":
      print(" ")
      print("You have decided to heal yourself with Magic.")
      time.sleep(2)
      UserHealth = UserHealth + UserMagic
      print(UserHealth)
      print(" ")
      if SkelotonHealth > 0:
        SkelotonTotalAttack = SkelotonAttack - UserDefense
        if SkelotonTotalAttack < 0:
          print("Your armour is stronger than your opponent's attack, so they will recive the damage.")
          print(" ")
          time.sleep(2)
          SkelotonHealth = SkelotonHealth - SkelotonAttack
        elif SkelotonTotalAttack > 0:
          print("Your armour is not stronger than your oponent's attack but it will shield you from some of the damage. You will only lose "+str(SkelotonTotalAttack)+" health points")
          print(" ")
          time.sleep(3.5)
          UserHealth = UserHealth - SkelotonTotalAttack
      elif SkelotonHealth <= 0:
        print("YOU HAVE DEFEATED THE SKELOTON WARRIOR!")
        key = "yes"
        break
  else:
    key = "no"
    break
if UserHealth <= 0:
  print("YOU HAVE BEEN DEFEATED!")
  print(" ")
  print("TRY AGAIN?")
else:#Each level will have to be contained inside of the else of the previouse event so that the game continues to flow toward the boss and to ensure that the user doesn't jump to the winning/lossing print lines.
  print("CONGRATULATIONS! NOW IT IS TIME TO PICK YOUR REWARDS.")
  print(" ")
  time.sleep(2)
  SkelotonRewardNumberWeapon = random.randint(0,4) 
  if SkelotonRewardNumberWeapon == 0:
    SkelotonRewardWeapon = Weapons["Improved Short Sword"]
    SkelotonRewardNameWeapon = "Improved Short Sword"
    SRWattackPoints = "35"
  elif SkelotonRewardNumberWeapon == 1:
    SkelotonRewardWeapon = Weapons["Improved Spear"]
    SkelotonRewardNameWeapon = "Improved Spear"
    SRWattackPoints = "30"
  elif SkelotonRewardNumberWeapon == 2:
    SkelotonRewardWeapon = Weapons["Improved Dagger"]
    SkelotonRewardNameWeapon = "Improved Dagger"
    SRWattackPoints = "40"
  elif SkelotonRewardNumberWeapon == 3:
    SkelotonRewardWeapon = Weapons["Improved Broad Sword"]
    SkelotonRewardNameWeapon = "Improved Broad Sword"
    SRWattackPoints = "45"
  elif SkelotonRewardNumberWeapon == 4:
    SkelotonRewardWeapon = Weapons["Dragon Dagger"]
    SkelotonRewardNameWeapon = "Dragon Dagger"
    SRWattackPoints = "60"
  print("The weapon you have found is a "+str(SkelotonRewardNameWeapon)+", it has "+str(SRWattackPoints)+" attack points. If you want the weapon enter 1 to claim it or hit enter to recive a 35 point health increase.")
  UserSkelotonWeaponChoice = input()
  if UserSkelotonWeaponChoice == "1":
    UserWeapon = SkelotonRewardWeapon
    weaponCheck(UserWeapon)
    statCheck()
  else:
    SkelotonHealthReward = 35
    UserHealth = UserHealth + SkelotonHealthReward
    healthCheck(UserHealth)
    statCheck()
  print(" ")
  print("YOUR STATS HAVE BEEN UPDATED!")
  print(" ")
  time.sleep(2)
  SkelotonRewardNumberMagic = random.randint(0,3) 
  if SkelotonRewardNumberMagic == 0:
    SkelotonRewardMagic = Magic["Improved Cystal Necklace"]
    SkelotonRewardMagicName = "Improved Cystal Necklace"
    SRMpoints = "25"
  elif SkelotonRewardNumberMagic == 1:
    SkelotonRewardMagic = Magic["Improved Wand"]
    SkelotonRewardMagicName = "Improved Wand"
    SRMpoints = "35"
  elif SkelotonRewardNumberMagic == 2:
    SkelotonRewardMagic = Magic["Improved Amulet"]
    SkelotonRewardMagicName = "Improved Amulet"
    SRMpoints = "30"
  elif SkelotonRewardNumberMagic == 3:
    SkelotonRewardMagic = Magic["Improved Gem Stone"]
    SkelotonRewardMagicName = "Improved Gem Stone"
    SRMpoints = "40"
  print("The magical item you have found is a "+str(SkelotonRewardMagicName)+", it has "+str(SRMpoints)+" health points. If you want to equip it type 1,if you do not hit enter and you will receive a 35 point health increase.")
  UserSkelotonMagicChoice = input()
  if UserSkelotonMagicChoice == "1":
    UserMagic = SkelotonRewardMagic
    magicCheck(UserMagic)
    statCheck()
  else:
    SkelotonHealthReward = 35
    UserHealth = UserHealth + SkelotonHealthReward
    healthCheck(UserHealth)
    statCheck()
  print("YOUR STATS HAVE BEEN UPDATED!")
  print(" ")
  time.sleep(2)
  SkelotonRewardNumberArmour = random.randint(0,2) 
  if SkelotonRewardNumberArmour == 0:
    SkelotonRewardArmour = Armour["Improved Sheild"]
    SkelotonRewardArmourName = "Improved Sheild"
    SRApoints = "30"
  elif SkelotonRewardNumberArmour == 1:
    SkelotonRewardArmour = Armour["Improved Chainmail"]
    SkelotonRewardArmourName = "Improved Chainmail"
    SRApoints = "45"
  elif SkelotonRewardNumberArmour == 2:
    SkelotonRewardArmour = Armour["Improved Full Body Armour"]
    SkelotonRewardArmourName = "Improved Full Body Armour"
    SRApoints = "50"
  print("The peice of armour you have found is a "+str(SkelotonRewardArmourName)+", and it has "+str(SRApoints)+" defense points. If you want to equip it type 1 or hit enter to receave a 35 point health increase.")
  UserSkelotonArmourChoice = input()
  if UserSkelotonArmourChoice == "1":
    UserDefense = SkelotonRewardArmour
    defenceCheck(UserDefense)
    statCheck()
  else:
    SkelotonHealthReward = 35
    UserHealth = UserHealth + SkelotonHealthReward
    healthCheck(UserHealth)
    statCheck()
  # END OF SKELLOTON -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
  print(" ")
  print("CONGRATULATIONS! YOU HAVE NOW ADVANCED TO THE NEXT ENEMY THE DARAGON!")
  print(" ")
  time.sleep(2.5)
  DragonName = "Dragon"
  DragonAttackOne = DragonAttacks["Tail Whip"]
  DragonAttackTwo = DragonAttacks["Fire Breath"]
  DragonMagicHeal = DragonMagic["Magic"]
  DragonHealth = 250
  DragonCharater = Dragon(DragonName, DragonAttackOne, DragonAttackTwo, DragonMagicHeal, DragonHealth)
  print("THE DRAGON HAS 250 HEALTH POINTS")
  print(" ")
  time.sleep(2)
  print("A TAIL WHIP ATTACK FOR 45 ATTACK POINTS")
  print(" ")
  time.sleep(2)
  print("A FIRE BREATH ATTACK FOR 70 ATTACK POINTS")
  print(" ")
  time.sleep(2)
  print("AND A MAGICAL ABILITY TO HEAL ITSELF WITH 40 HEALTH POINTS")
  print(" ")
  time.sleep(2)
  print("GOOD LUCK")
  print(" ")
  time.sleep(1.5)
  def getDragonHealth(DragonHealth): 
    print("The Dragon's total health: "+str(DragonHealth))
  while DragonHealth > 0: 
    if UserHealth > 0 :
      getDragonHealth(DragonHealth)
      statCheck()
      print(" ")
      print("Enter 1 to attack or type 2 to use your magic")
      print(" ")
      DragonActionAnswer = input()
      if DragonActionAnswer == "1": 
        DragonHealth = DragonHealth - UserWeapon
        print("You have attacked the Dragon with your weapon. Now it is their turn to attack.") 
        if DragonHealth>0: 
          DragonMoveNumber = random.randint(0,2)
          print(" ")
          time.sleep(2)
          if DragonMoveNumber == 0: 
            DragonTotalAttack = DragonAttackOne - UserDefense
            print("The Dragon has whiped you with their tail.")
            print(" ")
            time.sleep(2)
            if DragonTotalAttack < 0:
              print("Your armour is stronger than your opponent's attack, so they will recive the damage.")
              print(" ")
              time.sleep(2.5)
              DragonHealth = DragonHealth - DragonAttackOne 
            elif DragonTotalAttack > 0:
              print("Your armour is not stronger than your oponent's attack but it will shield you from some of the damage. You will only lose "+str(DragonTotalAttack)+" health points")
              UserHealth = UserHealth - DragonTotalAttack
              print(" ")
              time.sleep(3.5)
              #END of TAIL WHIP
          elif DragonMoveNumber == 1:
            DragonTotalAttack = DragonAttackTwo - UserDefense
            print("The Dragon has used their Fire Breath against you.")
            print(" ")
            time.sleep(2)
            if DragonTotalAttack < 0:
              print("Your armour is stronger than your opponent's attack, so they will recive the damage.")
              print(" ")
              time.sleep(2)
              DragonHealth = DragonHealth - DragonAttackTwo
            elif DragonTotalAttack > 0:
              print("Your armour is not stronger than your oponent's att but it will shield you from some of the damage. You will only lose "+str(DragonTotalAttack)+" health points")
              UserHealth = UserHealth - DragonTotalAttack
              print(" ")
              time.sleep(3.5)
              # End of fire breath
          elif DragonMoveNumber == 2: #SEARCH KEY
            print("The Dragon used magic to heal itself")
            DragonHealth = DragonHealth + 40
            print(" ")
            time.sleep(2)
            #END of first user dragon attack.
        elif DragonHealth <= 0:
          print("YOU HAVE DEFEATED THE DRAGON!")
          print(" ")
          time.sleep(2)
          break    
      elif DragonActionAnswer == "2": 
        print("You have decided to use your Magic to heal yourself. Now it is the Dragon's turn to attack.")
        UserHealth = UserHealth + UserMagic
        if DragonHealth>0:
          DragonMoveNumber = random.randint(0,2)
          print(" ")
          time.sleep(2.5)
          if DragonMoveNumber == 0:
            DragonTotalAttack = DragonAttackOne - UserDefense
            print("The Dragon has whiped you with their tail.")
            print(" ")
            time.sleep(2)
            if DragonTotalAttack < 0:
              print("Your armour is stronger than your opponent's attack, so they will recive the damage.")
              print(" ")
              time.sleep(2.5)
              DragonHealth = DragonHealth - DragonAttackOne 
            elif DragonTotalAttack > 0:
              print("Your armour is not stronger than your oponent's att but it will shield you from some of the damage. You will only lose "+str(DragonTotalAttack)+" health points")
              UserHealth = UserHealth - DragonTotalAttack
              print(" ")
              time.sleep(3.5)
          elif DragonMoveNumber == 1:
            DragonTotalAttack = DragonAttackTwo - UserDefense
            print("The Dragon has used their Fire Breath against you.")
            print(" ")
            time.sleep(2)
            if DragonTotalAttack < 0:
              print("Your armour is stronger than your opponent's attack, so they will recive the damage.")
              print(" ")
              time.sleep(2.5)
              DragonHealth = DragonHealth - DragonAttackTwo
            elif DragonTotalAttack > 0:
              print("Your armour is not stronger than your oponent's att but it will shield you from some of the damage. You will only lose "+str(DragonTotalAttack)+" health points")
              print(" ")
              time.sleep(3.5)
              UserHealth = UserHealth - DragonTotalAttack
          elif DragonMoveNumber == 2:
             print("The Dragon used magic to heal itself 40 health points")
             DragonHealth = DragonHealth + 40
             print(" ")
          time.sleep(2)
        elif DragonHealth <= 0:
          print("YOU HAVE DEFEATED THE DRAGON!")
          break    
    else:
      break
  if UserHealth <= 0:
    print("YOU LOSE")
    print(" ")
    print("TRY AGAIN?")
  else: 
    print(" ")
    print("CONGRATULATIONS! YOU HAVE DEFEATED THE DRAGON AND NOW FOR THE REWARDS")
    print(" ")
    time.sleep(2.5)
    DragonRewardNumberWeapon = random.randint(0,4)
    if DragonRewardNumberWeapon == 0:
      DragonRewardWeapon = Weapons["Dragon Short Sword"]
      DragonRewardNameWeapon = "Dragon Short Sword"
      DragonRWattackPoints = "70"
    elif DragonRewardNumberWeapon == 1:
      DragonRewardWeapon = Weapons["Dragon Spear"]
      DragonRewardNameWeapon = "Dragon Spear"
      DragonRWattackPoints = "75"
    elif DragonRewardNumberWeapon == 2:
      DragonRewardWeapon = Weapons["Dragon Dagger"]
      DragonRewardNameWeapon = "Dragon Dagger"
      DragonRWattackPoints = "60"
    elif DragonRewardNumberWeapon == 3:
      DragonRewardWeapon = Weapons["Dragon Broad Sword"]
      DragonRewardNameWeapon = "Dragon Broad Sword"
      DragonRWattackPoints = "65"
    elif DragonRewardNumberWeapon == 4:
      DragonRewardWeapon = Weapons["Dragon Cannon"]
      DragonRewardNameWeapon = "Dragon Cannon"
      DragonRWattackPoints = "100"
    print("The weapon you have found is a "+str(DragonRewardNameWeapon)+", it has "+str(DragonRWattackPoints)+" attack points. If you want the weapon enter 1 to claim it or hit enter to recive a 45 point health increase.")
    UserDragonWeaponChoice = input()
    if UserDragonWeaponChoice == "1":
      UserWeapon = DragonRewardWeapon
      weaponCheck(UserWeapon)
      statCheck()
    else:
      DragonHealthReward = 45
      UserHealth = UserHealth + DragonHealthReward
      healthCheck(UserHealth)
      statCheck()
    print(" ")
    print("YOUR STATS HAVE BEEN UPDATED!")
    time.sleep(2)
    print(" ")
    DragonRewardNumberMagic = random.randint(0,4)
    if DragonRewardNumberMagic == 0:
      DragonRewardMagic = Magic["Dragon Fire Necklace"]
      DragonRewardMagicName = "Dragon Fire Necklace"
      DragonRMpoints = "45"
    elif DragonRewardNumberMagic == 1:
      DragonRewardMagic = Magic["Dragon Horn Wand"]
      DragonRewardMagicName = "Dragon Horn Wand"
      DragonRMpoints = "50"
    elif DragonRewardNumberMagic == 2:
      DragonRewardMagic = Magic["Dragon Amulet"]
      DragonRewardMagicName = "Dragon Amulet"
      DragonRMpoints = "55"
    elif DragonRewardNumberMagic == 3:
      DragonRewardMagic = Magic["Dragon Fire Gem Stone"]
      DragonRewardMagicName = "Dragon Fire Gem Stone"
      DragonRMpoints = "60"
    elif DragonRewardNumberMagic == 4:
      DragonRewardMagic = Magic["Dragon Staff"]
      DragonRewardMagicName = "Dragon Staff"
      DragonRMpoints = "75"
    print("The magical item you have found is a "+str(DragonRewardMagicName)+", it has "+str(DragonRMpoints)+" health points. If you want to equip it type 1,if you do not hit enter and you will receive a 45 point health increase.")
    UserDragonMagicChoice = input()
    if UserDragonMagicChoice == "1":
      UserMagic = DragonRewardMagic
      magicCheck(UserMagic)
      statCheck()
    else:
      DragonHealthReward = 45
      UserHealth = UserHealth + DragonHealthReward
      healthCheck(UserHealth)
      statCheck()
    print(" ")
    time.sleep(2)
    print("YOUR STATS HAVE BEEN UPDATED!")
    print(" ")
    DragonRewardNumberArmour = random.randint(0,3)
    if DragonRewardNumberArmour == 0:
      DragonRewardArmour = Armour["Dragon Scale Sheild"]
      DragonRewardArmourName = "Dragon Scale Sheild"
      DragonRApoints = "55"
    elif DragonRewardNumberArmour == 2:
      DragonRewardArmour = Armour["Dragon Chain Mail"]
      DragonRewardArmourName = "Dragon Chain Mail"
      DragonRApoints = "60"
    elif DragonRewardNumberArmour == 3:
      DragonRewardArmour = Armour["Full Body Dragon Armour"]
      DragonRewardArmourName = "Full Body Dragon Armour"
      DragonRApoints ="65"
    elif DragonRewardNumberArmour == 4:
      DragonRewardArmour =Armour["Full Body Armour with Dragon Scale Sheild"]
      DragonRewardArmourName = "Full Body Armour with Dragon Scale Sheild"
      DragonRApoints = "120"
    print("The peice of armour you have found is a "+str(DragonRewardArmourName)+", and it has "+str(DragonRApoints)+" defense points. If you want to equip it type 1 or hit enter to receave a 45 point health increase.")
    UserDragonArmourChoice = input()
    if UserDragonArmourChoice == "1":
      UserDefense = DragonRewardArmour
      defenceCheck(UserDefense)
      statCheck()
    else:
      DragonHealthReward = 45
      UserHealth = UserHealth + DragonHealthReward
      healthCheck(UserHealth)
      statCheck()
    print(" ")
    print("YOUR STATS HAVE BEEN UPDATED!")
    print(" ")
    time.sleep(2)
    print("CONGRATULATIONS! THERE IS ONLY THE BOSS LEFT IN YOUR JOURNY.")
    time.sleep(2)
    print(" ")
    print("BUT WHO COULD THAT BOSS BE...")
    print(" ")
    time.sleep(2)
    print("HOW ABOUT ME, THE DARK WIZARD OZ!")
    BossName = "The Dark Wizard Oz"
    BossAttackOne = BossAttacks["Confusion Curse"]
    BossAttackTwo = BossAttacks["Fire Spell"]
    BossAttackThree = BossAttacks["Lightning Spell"]
    BossMagicOne = BossMagic["Magic"]
    BossMagicTwo = BossMagic["Super Magic"]
    BossHealth = 500
    Oz = Boss(BossName, BossAttackOne, BossAttackTwo, BossAttackThree, BossMagicOne, BossMagicTwo, BossHealth)
    def getBossHealth(BossHealth):
      print("The Dark Wizard Oz's total health: "+str(BossHealth))
    print(" ")
    print("The Dark Wizard Oz has three attacks. A Confusion Curse for 65 attack points, a Fire Spell for 70 attack points, and a Lightning Spell for 90 attack points.")
    print(" ")
    time.sleep(4)
    print("Oz can also heal himself with magic 55 or 100 health points.")
    print(" ")
    time.sleep(3.5)
    print("LET THE FINAL BATTLE BEGIN!")
    print(" ")
    time.sleep(2)
    while BossHealth > 0: 
      if UserHealth > 0 :
        getBossHealth(BossHealth)
        print(" ")
        statCheck()
        print(" ")
        print("Enter 1 to attack or type 2 to use your magic")
        print(" ")
        BossActionAnswer = input()
        if BossActionAnswer == "1":
          BossHealth = BossHealth - UserWeapon
          print("You have attacked Oz with your weapon now it is their turn to attack.")
          print(" ")
          time.sleep(2)
        elif BossActionAnswer == "2":
          print("You have decided to use your Magic to heal yourself. Now it is Oz's turn to attack.")
          print(" ")
          time.sleep(2)
          UserHealth = UserHealth + UserMagic
        if BossHealth > 0:
          BossMoveNumber = random.randint(0,4)
          if BossMoveNumber == 0:
            BossTotalAttack = BossAttackOne - UserDefense
            print("The Dark Wizard Oz has used a Confusion Curse")
            print(" ")
            time.sleep(2)
            if BossTotalAttack < 0:
              print("Your armour is stronger than your opponent's attack, so they will recive the damage.")
              print(" ")
              time.sleep(2)
              BossHealth = BossHealth - BossAttackOne
            elif BossTotalAttack > 0:
              print("Your armour is not stronger than your oponent's attack but it will shield you from some of the damage. You will only lose "+str(BossTotalAttack)+" health points")
              print(" ")
              time.sleep(3.5)
              UserHealth = UserHealth - BossTotalAttack
          elif BossMoveNumber == 1: 
            BossTotalAttack = BossAttackTwo - UserDefense
            print("The Dark Wizard Oz has used a Fire Spell.")
            print(" ")
            time.sleep(2)
            if BossTotalAttack < 0:
              print("Your armour is stronger than your opponent's attack, so they will recive the damage.")
              BossHealth = BossHealth - BossAttackTwo
              print(" ")
              time.sleep(2.5)
            elif BossTotalAttack > 0:
              print("Your armour is not stronger than your oponent's attack but it will shield you from some of the damage. You will only lose "+str(BossTotalAttack)+" health points")
              UserHealth = UserHealth - BossTotalAttack
              print(" ")
              time.sleep(3.5)
          elif BossMoveNumber == 2:
            BossTotalAttack = BossAttackThree - UserDefense
            print("The Dark Wizard Oz has used a Lightning Spell.")
            print(" ")
            time.sleep(2)
            if BossTotalAttack < 0 :
              print("Your armour is stronger than your opponent's attack, so they will recive the damage.")
              print(" ")
              time.sleep(2.5)
              BossHealth = BossHealth - BossAttackThree
            elif BossTotalAttack > 0:
              print("Your armour is not stronger than your oponent's attack but it will shield you from some of the damage. You will only lose "+str(BossTotalAttack)+" health points")
              UserHealth = UserHealth - BossTotalAttack #Search KEY
              print(" ")
              time.sleep(3.5)
          elif BossMoveNumber == 3:
            print("The Dark Wizard Oz used magic to heal himself 55 health points")
            print(" ")
            time.sleep(2.5)
            BossHealth = BossHealth + 55
          elif BossMoveNumber == 4:
            print("The Dark Wizard Oz used magic to heal himself 100 health points.")
            BossHealth = BossHealth + 100
            print(" ")
            time.sleep(2.5)
        elif BossHealth <= 0: # THE END IF YOU WIN
          print("The Boss has been defeated!")
          time.sleep(1)
          print(" ")
          print("NO YOU HAVE DEFEATED ME!")
          time.sleep(1)
          print(" ")
          print("Congratulations, you have won the game!")
          break
      elif UserHealth <= 0: #THE END OF YOU LOSE
        print("You have been defeated.")
        print(" ")
        print("Try again?")
        break