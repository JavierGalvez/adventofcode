f = open('data.txt', 'r')
stream = f.readline().replace('\n','')

score = 0
totalScore = 0

garbage = False

garbageCharacters = 0
totalGarbageCharacters = 0

i = 0
while i < len(stream):
    if(garbage):
        garbageCharacters += 1
    if(stream[i] == '{' and not garbage):
        score += 1
    elif(stream[i] == '}' and not garbage):
        totalScore += score
        score -= 1
    elif(stream[i] == '!'):
        i += 1
        garbageCharacters -= 1
    elif(stream[i] == '<'):
        garbage = True
    elif(stream[i] == '>'):
        garbage = False
        totalGarbageCharacters += garbageCharacters - 1
        garbageCharacters = 0
    i += 1

print('First part:',totalScore)
print('Second part:',totalGarbageCharacters)
