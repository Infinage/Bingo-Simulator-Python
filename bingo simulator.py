"""
Bingo program using python.
Developed by :
Naresh J, Btech - IT 'A'
"""

import random

def winn(player_name):
    print (player_name, "has hit BINGO!!")
    return True

class bingo(object):

    def __init__(self, name):
        bingolst = [[0 for _ in range(5)] for _ in range(5)]
        l = [i for i in range(1, 26)]
        for i in range(5):
            for j in range(5):
                bingolst[i][j] = random.choice(l)
                l.remove(bingolst[i][j])

        self.bingolst = bingolst
        self.BINGO = 0
        self.name = name

    def strikeno(self, n):
        for i in range(5):
            if n in self.bingolst[i]:
                pos = self.bingolst[i].index(n)
                self.bingolst[i][pos] = -self.bingolst[i][pos]

    def check(self):
        self.BINGO = 0

        if all([self.bingolst[i][i] < 0 for i in range(5)]):
            self.BINGO += 1
            if self.BINGO >= 5: return winn(self.name)

        if all([self.bingolst[i][i] < 0 for i in range(-1, -6, -1)]):
            self.BINGO += 1
            if self.BINGO >= 5: return winn(self.name)
            
        for i in range(5):
            if all([self.bingolst[i][j] < 0 for j in range(5)]):
                self.BINGO += 1
                if self.BINGO >= 5: return winn(self.name)

        for i in range(5):
            if all([self.bingolst[j][i] < 0 for j in range(5)]):
                self.BINGO += 1
                if self.BINGO >= 5: return winn(self.name)
        
    @staticmethod
    def strike(text):
        result = ''
        for i in text:
            result += i + '\u0336'
        return result

    def __str__(self):
        bingostr = '\n| '
        for i in range(5):
            for j in range(5):
                if self.bingolst[i][j] < 0:
                    bingostr += bingo.strike(str(-self.bingolst[i][j]).zfill(2)) + ' | '
                else:
                    bingostr += str(self.bingolst[i][j]).zfill(2) + ' | '
            bingostr += '\n| '
        return bingostr.rstrip("| ")

bot_name = random.choice(["Chang bot", "Wibur Bot", "Maverick Bot", "Chan Bot", "Genghis Bot"])
bot = bingo(bot_name)
player = bingo(input("Enter your name : "))
print ("You are playing against ", bot_name, ". Good Luck!", sep = '')
print(player)

l = [i for i in range(1, 26)]

while not(bot.check() or player.check()):
    n = int(input("Enter your choice : "))
    if n in l:
        bot.strikeno(n)
        player.strikeno(n)
        l.remove(n)
        
    else:
        print ("Please enter a valid choice.\n")
        continue
    
    n = random.choice(l)
    bot.strikeno(n)
    player.strikeno(n)
    l.remove(n)
    print (bot_name, " has striked the no '", n, "'", sep = '')
    print (player)

input("Thank you for playing. Hit enter to Exit.. ")
