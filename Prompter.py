import json
import string
import names
import random

with open('skills.json','r') as skills:
    skillsList = json.load(skills)

outputText = open('prompts.txt','a+')

GenderOptions = ['man','woman']
hairOptions = ['long', 'medium-length','short','no']
hairType = ['hair','beard','moustache']
colours = ['red','green','blue','yellow','brown','black','white']
clothes = ['suit','dress','tie','hat','shirt']
settlement = ['city','town','village','port','outpost','fort']

#  Also from the town name generator
first = ["Chelm", "Elm", "El", "Bur", "En", "Eg", "Pem", "Pen", "Edg", "Sud", "Sod", "Hors", "Dur", "Sun", "Nort", "Brad", "Farn", "Barn", "Dart", "Hart", "South", "Shaft", "Blan", "Rock", "Alf", "Wy", "Marl", "Staf", "Wet", "Cas", "Stain", "Whit", "Stap", "Brom", "Wych", "Watch", "Win", "Horn", "Mel", "Cook", "Hurst", "Ald", "Shriv", "Kings", "Clere", "Maiden", "Leather", "Brack","Brain", "Walt", "Prest", "Wen", "Flit", "Ash"]
doubles = ["Bass", "Chipp", "Sodd", "Sudd", "Ell", "Burr", "Egg", "Emm", "Hamm", "Hann", "Cann", "Camm", "Camb", "Sund", "Pend", "End", "Warr", "Worr", "Hamp", "Roth", "Both", "Sir", "Cir", "Redd", "Wolv", "Mill", "Kett", "Ribb", "Dribb", "Fald", "Skell", "Chedd", "Chill", "Tipp", "Full", "Todd", "Abb", "Booth"]
postdoubles = ["ing", "en", "er"]
mid = ["bas", "ber", "stan", "ring", "den", "-under-", " on ", "en", "re", "rens", "comp", "mer", "sey", "mans"]
last = ["ford", "stoke", "ley", "ney",  "don", "den", "ton", "bury", "well", "beck", "ham", "borough", "side", "wick", "hampton", "wich", "cester", "chester", "ling", "moor", "wood", "brook", "port", "wold", "mere", "castle", "hall", "bridge", "combe", "smith", "field", "ditch", "wang", "over", "worth", "by", "brough", "low", "grove", "avon", "sted", "bourne", "borne", "thorne", "lake", "shot", "bage", "head", "ey", "nell", "tree", "down"]

#  THIS TOWN GENERATOR WAS POSTED TO REDDIT BY U/WURSTGEIST HERE https://www.reddit.com/r/proceduralgeneration/comments/4ra0cz/english_place_name_generator_in_python/
def townName():
    finished_name = ""
    pd = 0
    if(random.random()  > 0.4):
        finished_name = finished_name + random.choice(doubles)
        if(random.random()  > 0.6):
            finished_name = finished_name + random.choice(postdoubles)
            pd = 1
        else:
            finished_name = finished_name[0:len(finished_name) - 1]
    else:
        finished_name = finished_name + random.choice(first)

    if(random.random()  > 0.5 and not pd):
        if(finished_name.endswith("r") or finished_name.endswith("b")):
            if(random.random()  > 0.4):
                finished_name = finished_name + "ble"
            else:
                finished_name = finished_name + "gle"
        elif(finished_name.endswith("n") or finished_name.endswith("d")):
            finished_name = finished_name + "dle"
        elif(finished_name.endswith("s")):
            finished_name = finished_name + "tle"

    if(random.random()  > 0.7 and finished_name.endswith("le")):
        finished_name = finished_name + "s"

    elif(random.random()  > 0.5):
        if(finished_name.endswith("n")):
            if(random.random()  > 0.5):
                finished_name = finished_name + "s"
            else:
                finished_name = finished_name + "d"
        elif(finished_name.endswith("m")):
            finished_name = finished_name + "s"

    if(random.random()  > 0.7):
        finished_name = finished_name + random.choice(mid)
    finished_name = finished_name + random.choice(last)

    fix = finished_name.rpartition(' ')
    if(fix[1] == ' '):
        finished_name = fix[0] + ' ' + fix[2].capitalize()

    fix = finished_name.rpartition('-')
    if(fix[1] == '-'):
        finished_name = fix[0] + '-' + fix[2].capitalize()
    return finished_name

def describer(gender,length,hairtype,color,clothing):
    look = ["see", "make out", "discern"]
    looknum = random.randint(0,2)
    obscurity = ["in this light","at this distance","through the fog","through the smoke"]
    obnum = random.randint(0,3)
    starter = 'a {} with {} {} wearing a {} {} - is all the party can {} {}. '.format(gender,length,hairtype,color,clothing,look[looknum],obscurity[obnum])
    return starter

def namegen(gender):
    if gender == 0:
        name = names.get_full_name(gender='male')
    else:
        name = name = names.get_full_name(gender='female')
    return name

def skillsAndWeaknesses():
    listOfSkills = skillsList['skills']
    skillsandweaknesses = random.choices(listOfSkills,k=4)
    return skillsandweaknesses

def quirkfinder():
    listOfSkills = skillsList['quirks']
    quirk = random.choices(listOfSkills,k=1)
    return quirk[0]


def promptbuilder():
    randomarray = [random.randint(0,1),random.randint(0,3),random.randint(0,2),random.randint(0,6),random.randint(0,4)]
    gender_options = GenderOptions[randomarray[0]]
    hair_options = hairOptions[randomarray[1]]
    hair_type = hairType[randomarray[2]]
    clothes_color = colours[randomarray[3]]
    clothes_type = clothes[randomarray[4]]
    startingline = describer(gender_options,hair_options,hair_type,clothes_color,clothes_type)
    newname = namegen(randomarray[0])
    classnumber = randomarray[3]+randomarray[4]
    classlist = skillsList['classes']
    characterClass = classlist[classnumber]
    town = townName()
    settlementType = settlement[random.randint(0,5)]
    skillses = skillsAndWeaknesses()
    funquirk = quirkfinder()
    # print(startingline)
    string = "\nCalled {}, they are a {} from the {} known as {}.\nThey are known for their expertise in the field of {}, they wish they were more knowledegable about {} and are truly terrible at both {} and {}. Interestingly {} {} \n\n".format(newname,characterClass,settlementType,town,skillses[0],skillses[1],skillses[2],skillses[3], newname,funquirk)
    outputText.write(startingline+string)

for n in range(1000):
    promptbuilder()

