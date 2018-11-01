"""this commented section needs reworking after update to document formatting"""

# these are parts of an automation task I was completing for a personal hobby
# it doesn't represent a complete, encapsulated project, just the parts I thought warranted automation

import json
import ftfy # this is a godsend for fixing garbage mojibakes

# import PyPDF2
# import in_place

# ##defunct, doesn't rip all text, need better solution (ended up copy/paste from document, couldn't find
# ##better pdf dumping module that retrieved all text, but might revisit this later)
# pdfFileObj = open('grimgrim.pdf', 'rb') 
# # creating a pdf reader object 
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

# # extracting text from pdf doc
# f = open('allspells.txt', 'a')
# num = 6 # pg 6 is beginning of spells in this document
# while num < 57: # pg 56 is end of spells in this document
#     page = pdfReader.getPage(num)
#     line = page.extractText()
#     f.write(line)
#     num += 1
#     break
# f.close()
# pdfFileObj.close()

# at this point I edit in terms like "Definition" and "Name" using a mass text editor, as well after this part
# manually recreating newlines that should actually be in the definition (way too many different cases to 
# bother coding) using visual studio code. Multiline editing is convenient and there is zero net sum advantage
# in designing what I could do smarter, better, and faster by hand with pre-existing software

## I think this method worked as intended? Honestly don't remember, writing this program was a fever dream. 
## But the end product was nice!
# def killNewLines():
#     switch = False
#     spellLevel = 0
#     while spellLevel < 11:
#         with in_place.InPlace("level0spells.txt") as file:
#             for line in file:
#                 if "Definition: " in line:
#                     switch = True
#                     defline = ""
#                 if line.startswith("\n"):
#                     switch = False
#                     line = defline + "\n\n" + line
#                 if switch == True:
#                     defline += line.replace("\n", " ")
#                     line = ""
#                 if switch == False:
#                     line.replace("Definition: ", "")
#                     line = line + "\n"
#                     file.write(line)        
#             file.write(defline) # ensures last line in file is written to new file
#             file.close()
#             spellLevel += 1

def classDocCreate():
    bard = open("bard.txt", "a")
    cleric = open("cleric.txt", "a")
    druid = open("druid.txt", "a")
    paladin = open("paladin.txt", "a")
    ranger = open("ranger.txt", "a")
    sorcerer = open("sorcerer.txt", "a")
    warlock = open("warlock.txt", "a")
    wizard = open("wizard.txt", "a")

    # bard, cleric, druid, paladin, ranger, sorcerer, warlock, wizard
    spellname = ""
    levschool = ""
    casttime = ""
    sprange= ""
    spcomp = ""
    spdur = ""
    spclass= ""
    spdef = ""
    definit = ""

    spellLevel = 0
    while spellLevel < 10:
        spells = open("level" + str(spellLevel) + "spells.txt", "r")
        if spellLevel == 0:
            bard.write("Cantrips:::\n")
            cleric.write("Cantrips:::\n")
            druid.write("Cantrips:::\n")
            paladin.write("Cantrips:::\n")
            ranger.write("Cantrips:::\n")
            sorcerer.write("Cantrips:::\n")
            warlock.write("Cantrips:::\n")
            wizard.write("Cantrips:::\n")        
        elif spellLevel == 1:
            bard.write("1st level:::\n")
            cleric.write("1st level:::\n")
            druid.write("1st level:::\n")
            paladin.write("1st level:::\n")
            ranger.write("1st level:::\n")
            sorcerer.write("1st level:::\n")
            warlock.write("1st level:::\n")
            wizard.write("1st level:::\n")
        elif spellLevel == 2:
            bard.write("2nd level:::\n")
            cleric.write("2nd level:::\n")
            druid.write("2nd level:::\n")
            paladin.write("2nd level:::\n")
            ranger.write("2nd level:::\n")
            sorcerer.write("2nd level:::\n")
            warlock.write("2nd level:::\n")
            wizard.write("2nd level:::\n")
        elif spellLevel == 3:
            bard.write("3rd level:::\n")
            cleric.write("3rd level:::\n")
            druid.write("3rd level:::\n")
            paladin.write("3rd level:::\n")
            ranger.write("3rd level:::\n")
            sorcerer.write("3rd level:::\n")
            warlock.write("3rd level:::\n")
            wizard.write("3rd level:::\n")
        elif spellLevel < 10:
            bard.write(str(spellLevel) + "th level:::\n")
            cleric.write(str(spellLevel) + "th level:::\n")
            druid.write(str(spellLevel) + "th level:::\n")
            paladin.write(str(spellLevel) + "th level:::\n")
            ranger.write(str(spellLevel) + "th level:::\n")
            sorcerer.write(str(spellLevel) + "th level:::\n")
            warlock.write(str(spellLevel) + "th level:::\n")
            wizard.write(str(spellLevel) + "th level:::\n")
        
        for line in spells:
            line = line.replace("'", "'") # fix encoding issue in json
            try:
                spellname = line
                levschool = ""
                casttime = ""
                sprange= ""
                spcomp = ""
                spdur = ""
                spclass= ""
                spdef = ""
                definit = ""
                levschool = next(spells)
                casttime = next(spells)
                sprange = next(spells)
                spcomp = next(spells)
                spdur = next(spells)
                spclass = next(spells)
                spdef = next(spells)
                definit = next(spells)
                while not definit.startswith("\n"):
                    definit = "   " + definit
                    spdef += definit
                    definit = next(spells)

            except StopIteration:
                spdef += "\n"
                pass
            strToWrite = spellname + levschool + casttime + sprange + spcomp + spdur + spclass + spdef + "\n"
            if spclass.find('Bard') > -1:
                bard.write(strToWrite)
            if spclass.find('Cleric') > -1:
                cleric.write(strToWrite)
            if spclass.find('Druid') > -1:
                druid.write(strToWrite)
            if spclass.find('Paladin') > -1:
                paladin.write(strToWrite)
            if spclass.find('Ranger') > -1:
                ranger.write(strToWrite)
            if spclass.find('Sorcerer') > -1:
                sorcerer.write(strToWrite)        
            if spclass.find('Warlock') > -1:
                warlock.write(strToWrite)        
            if spclass.find('Wizard') > -1:
                wizard.write(strToWrite)

            # jsonify content for future possible web/phone app development using these spells
            jsonifySpells(spellname, levschool, casttime, sprange, spcomp, spdur, spclass, spdef)
        spellLevel += 1
    bard.close()
    cleric.close()
    druid.close()
    paladin.close()
    ranger.close()
    sorcerer.close()
    warlock.close()
    wizard.close()

# sorts by level then alphabet
def jsonifySpells(spName, spLev, spCast, spRange, spComp, spDur, spClass, spDef):
    spName = spName.rstrip()
    spLev = spLev.rstrip()
    spCast = spCast.rstrip()
    spRange = spRange.rstrip()
    spComp = spComp.rstrip()
    spDur = spDur.rstrip()
    spClass = spClass.rstrip()
    spDef = spDef.rstrip()
    
    spellList = []
    data = {}
    data['Name'] = ftfy.fix_text(spName)
    data['School'] = ftfy.fix_text(spLev)
    data['Casting Time'] = ftfy.fix_text(spCast.replace("Casting Time: ", ""))
    data['Range'] = ftfy.fix_text(spRange.replace("Range: ", ""))
    data['Components'] = ftfy.fix_text(spComp.replace("Components : ", ""))
    data['Duration'] = ftfy.fix_text(spDur.replace("Duration: ", ""))
    data['Class'] = ftfy.fix_text(spClass.replace("Classes: ", ""))
    data['Definition'] = ftfy.fix_text(spDef)

    try: 
        with open('spells.json') as spellsin:
            spellList = json.load(spellsin)

    except FileNotFoundError: # first write, pass to next statement to create file
        pass

    spellList.append(data)
    with open('spells.json', 'w', encoding="utf-8") as spellsout:
        json.dump(spellList, spellsout)
        spellsout.close()

classDocCreate()

### basically, the product created from this is the final product, minus formatting
### and writing into .rtfs, which was done with spire.doc using C#
