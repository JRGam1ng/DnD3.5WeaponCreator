import random

print("Hello Madam, my name is Sir Westershire, and I shall be your weapon creator today.  Please answer the following questions so I can make you the perfect weapon.")
while True:
    distance = input("Would you like a melee or ranged weapon?")
    exotic = input("May I consider an exotic weapon?")
    masterwork = input("Shall I pay for a Masterwork?")
    magic = input("Shall I infuse it with Magic?")
    repeat = input("Would you like to make another weapon after this one Madam?")
    
    ranged_standard = ["Heavy Crossbow (1d10)", "Light Crossbow (1d8)", "Dart (1d4)", "Javelin (1d6)", "Sling (1d4)", "Longbow (1d8)", "Composite Longbow (1d8)", "Shortbow (1d6)", "Composite Shortbow (1d6)"]
    ranged_exotic = ["Bolas (1d4)", "Hand Crossbow (1d4)", "Repeating Heavy Crossbow (1d10)", "Repeating Light Crossbow (1d8)", "Net (no damage)", "Shuriken (1d2)"]
    melee_standard = ["Gauntlet (1d3)",	"Dagger (1d4)",	"Punching Dagger (1d4)",	"Spiked Gauntlet (1d4)",	"Light Mace (1d6)",	"Sickle (1d6)",	"Club (1d6)",	"Heavy Mace (1d8)",	"Morningstar (1d8)",	"Shortspear (1d6)",	"Longspear (1d8)",	"Quarterstaff (1d6/1d6)",	"Spear (1d8)",	"Throwing Axe (1d6)",	"Light Hammer (1d4)",	"Handaxe (1d6)",	"Kukri (1d4)",	"Light Pick (1d4)",	"Sap (1d6)",	"Light Shield (1d3)",	"Spiked Armor (1d6)",	"Light Spiked Shield (1d4)",	"Short Sword (1d6)",	"Battleaxe (1d8)",	"Flail (1d8)",	"Longsword (1d8)",	"Heavy Pick (1d6)",	"Rapier (1d6)",	"Scimitar (1d6)",	"Heavy Sheild (1d4)",	"Spiked Heavy Shield (1d6)",	"Trident (1d8)",	"Warhammer (1d8)",	"Falchion (2d4)",	"Glaive (2d10)",	"Greataxe (1d12)",	"Greatclub (1d10)",	"Heavy Flail (1d8)",	"Greatsword (2d6)",	"Guisarme (2d4)",	"Halberd (1d10)",	"Lance (1d8)",	"Ranseur (2d4)",	"Scythe (2d4)"]
    melee_exotic = ["Kama (1d6)",	"Nunchaku (1d6)",	"Sai (1d4)",	"Siangham (1d6)",	"Bastard Sword (1d10)",	"Dwarven Waraxe (1d10)",	"Whip (1d3)",	"Orc Double Axe (1d8/1d8)",	"Spiked Chain (2d4)",	"Dire Flail (1d8/1d8)",	"Gnome Hooked Hammer (1d8/1d6)",	"Two Bladed Sword (1d8/1d8)",	"Dwarven Urgosh (1d8/1d6)"]

    enchantments = ["Anarchic",	"Axiomatic", "Bane", "Brilliant Energy",	"Dancing",	"Defending",	"Disruption",	"Distance",	"Flaming",	"Flaming Burst",	"Frost",	"Ghost Touch",	"Holy",	"Icy Burst",	"Keen",	"Ki Focus",	"Merciful",	"Mighty Cleaving",	"Returning",	"Seeking",	"Shock",	"Shocking Burst",	"Speed",	"Spell Storing",	"Thundering",	"Throwing",	"Unholy",	"Vicious",	"Vorpal",	"Wounding"]

    i=0

    if distance == "melee":
        if exotic == "yes":
            typeofweapon = random.choice(melee_exotic)
        elif exotic == "no":
            typeofweapon = random.choice(melee_standard)
    elif distance == "ranged":
        if exotic == "yes":
            typeofweapon = random.choice(ranged_exotic)
        elif exotic == "no":
            typeofweapon = random.choice(ranged_standard)
    else:
        pass

    if masterwork == "yes":
        i = 1
    elif masterwork == "no":
        pass

    if magic == "yes":
        enchant = random.choice(enchantments)
    if magic == "no":
        enchant = "no enchantments"

    print("Here is your weapon.  It is a " + typeofweapon + "+" + str(i) + " with " + enchant + " on it.  Thank you much Madam, I hope my services have met your expectations.  Enjoy your weapon!")

    if repeat =="no":
        break