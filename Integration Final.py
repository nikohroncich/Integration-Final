#Programmer: Niko Hroncich
#Description: Gathering together football statistics for a quarterback
#Date: 12/11/2022
#Source for stats: https://www.espn.com/nfl/player/gamelog/_/id/3916387/type/nfl/year/2019

print("Hello!")
print("We will be gathering together football statistics for a quarterback that plays on either the college level or NFL!")
print("Ready? Let's begin!")

name = input("Enter the name of the quarterback: ")

#Week 1 Stats
passYards1 = input("Enter the passing yards for week 1: ")
rushYards1 = input("Enter the rushing yards for week 1: ")
passingAttempts1 = input("Enter the passing attempts for week 1: ")
passingCompletions1 = input("Enter the passing completions for week 1: ")
passTouchdown1 = input("Enter the number of passing touchdowns for week 1: ")
passInt1 = input("Enter the number of passing interceptions for week 1: ")
rushTouchdown1 = input("Enter the number of rushing touchdowns for week 1: ")
pYard1 = int(passYards1)
rYard1 = int(rushYards1)
pAtt1 = int(passingAttempts1)
pComp1 = int(passingCompletions1)
pTouchdown1 = int(passTouchdown1)
pInt1 = int(passInt1)
rTouchdown1 = int(rushTouchdown1)

#Week 2 Stats
passYards2 = input("Enter the passing yards for week 2: ")
rushYards2 = input("Enter the rushing yards for week 2: ")
passingAttempts2 = input("Enter the passing attempts for week 2: ")
passingCompletions2 = input("Enter the passing completions for week 2: ")
passTouchdown2 = input("Enter the number of passing touchdowns for week 2: ")
passInt2 = input("Enter the number of passing interceptions for week 2: ")
rushTouchdown2 = input("Enter the number of rushing touchdowns for week 2: ")
pYard2 = int(passYards2)
rYard2 = int(rushYards2)
pAtt2 = int(passingAttempts2)
pComp2 = int(passingCompletions2)
pTouchdown2 = int(passTouchdown2)
pInt2 = int(passInt2)
rTouchdown2 = int(rushTouchdown2)
                   
#Week 3 Stats
passYards3 = input("Enter the passing yards for week 3: ")
rushYards3 = input("Enter the rushing yards for week 3: ")
passingAttempts3 = input("Enter the passing attempts for week 3: ")
passingCompletions3 = input("Enter the passing completions for week 3: ")
passTouchdown3 = input("Enter the number of passing touchdowns for week 3: ")
passInt3 = input("Enter the number of passing interceptions for week 3: ")
rushTouchdown3 = input("Enter the number of rushing touchdowns for week 3: ")
pYard3 = int(passYards3)
rYard3 = int(rushYards3)
pAtt3 = int(passingAttempts3)
pComp3 = int(passingCompletions3)
pTouchdown3 = int(passTouchdown3)
pInt3 = int(passInt3)
rTouchdown3 = int(rushTouchdown3)

#Stats through the first 3 weeks of football
totalPassing = (pYard1 + pYard2 + pYard3)
totalRushing = (rYard1 + rYard2 + rYard3)
totalAttempts = (pAtt1 + pAtt2 + pAtt3)
totalCompletions = (pComp1 + pComp2 + pComp3)
totalPassTouchdown = (pTouchdown1 + pTouchdown2 + pTouchdown3)
totalPassInt = (pInt1 + pInt2 + pInt3)
totalRushTouchdown = (rTouchdown1 + rTouchdown2 + rTouchdown3)

print("Here are the stats through the first 3 weeks of football for", name)
print("Total passing yards through the first 3 weeks =", totalPassing)
print("Total rushing yards through the first 3 weeks =", totalRushing)
print("Total passing attempts through the first 3 weeks =", totalAttempts)
print("Total passing completions through the first 3 weeks =", totalCompletions)
print("Total passing touchdowns through the first 3 weeks =", totalPassTouchdown)
print("Total passing interceptions through the first 3 weeks =", totalPassInt)
print("Total rushing touchdowns through the first 3 weeks =", totalRushTouchdown)

print("Here are the average stats per game for", name)

#Averages through the first 3 weeks
avgPassing = (totalPassing / 3)
avgRushing = (totalRushing / 3)
compPercent = (totalCompletions / totalAttempts)
avgPassTouchdown = (totalPassTouchdown / 3)
avgPassInt = (totalPassInt / 3)
avgRushTouchdown = (totalRushTouchdown / 3)

print("Average passing yards per game =", format(avgPassing,'.1f'))
print("Average rushing yards per game =", format(avgRushing,'.1f'))
print("Completion percentage per game = %", format(compPercent,'.0f'))
print("Average passing touchdowns per game =", format(avgPassTouchdown,'.1f'))
print("Average passing interceptions per game =", format(avgPassInt,'.1f'))
print("Average rushing touchdowns per game =", format(avgRushTouchdown,'.1f'))

if avgPassing >= 250:
    print(name,"had an above average passing yards per game!")
else:
    if avgPassing >= 200:
        print(name,"had an average passing yards per game!")
    else:
        print(name,"had a below average passing yards per game!")
if avgPassing > avgRushing:
    print(name,"was a better passer than a runner!")
else:
    if avgPassing < avgRushing:
        print(name,"was a better runner than a passer!")
    
            
        
    
