import sys
import time
try:
    correct = sys.argv[1]
    letter = sys.argv[2]
except IndexError:
    print("You must write two arguments for this program")
    sys.exit()

dictionary = {}
with open(correct, encoding="utf-8") as file:
    for line in file.readlines():
        line = line.replace("\n", "")
        line = line.replace("İ", "i")
        line = line.replace("I", "ı")
        line = line.lower()
        line = line.replace(":", ",")
        key, *value = line.split(",")
        dictionary[key] = value

dictionary1 = {}
with open(letter, encoding="utf-8") as file:
    for line in file.readlines():
        line = line.replace("İ", "i")
        line = line.replace("I", "ı")
        line = line.lower()
        key, value = line.split(":")
        dictionary1[key] = int(value)

def shuffled():
    with open(correct, encoding="utf-8") as file:
        for i in dictionary.keys():
            print("Shuffled letters are: ", i, " Please guess words for these letters with minimum three letters")
            list2 = list()
            time1 = 30
            while time1 > 0:
                start = time.time()
                word = input("Guessed Word: ")
                end1 = time.time()
                if time1-(end1-start) <= 0:
                    print("You have 0 time")
                    break
                elif word not in [z for i in dictionary.values() for z in i]:
                    print("your guessed word is not a valid word")
                elif word in list2:
                    print("This word is guessed before")
                else:
                    list2.append(word)
                    pass
                end = time.time()
                time1 -= end-start
                print("You have {} time".format(int(time1)))
            sum = 0
            for x in list2:
                for z in x:
                    sum += dictionary1[z] * len(x)
            if sum == 0:
                print("Score for  {}  is  0 and no words were guessed correctly".format(i))
            else:
                print("Score for  {}  is  {} and guessed words are: ".format(i, sum), end="")
                list2 = '-'.join(list2)
                print(list2)
shuffled()

