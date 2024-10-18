# Moadel
moadeldict = {
    "ali" : 14,
    "reza" : 16,
    "sara" : 19,
    "milad" : 18,
    "javad" : 17,
    "atefeh" : 15,
    "faezeh" : 18,
    "bahar" : 17
}
# name
name = input("What is your name : ")
# score
score1 = int(input(f"what is your score in mathematic {name}: "))
score2 = int(input(f"what is your score in dini {name}: "))
score3 = int(input(f"what is your score in zist {name}: "))
score4 = int(input(f"what is your score in olum {name}: "))
score5 = int(input(f"what is your score in shimi {name}: "))
# moadel
moadel = (score1 + score2 + score3 + score4 + score5) / 5
# update
moadeldict.update({name: moadel})
print(moadeldict)