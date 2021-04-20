import random
import os
import sys

print('''
1-)English
2-)Turkish
''')
lang = int(input("Choose Language:"))

if lang == 2:
    word_pool=["hava","hayvan","cevap","elma","bebek","çanta","banka","güzellik","inanç","kuş","vücut","kitap","kutu","oğlan","ekmek","erkek","bina","otobüs","araba","kart","kap","kedi","sandalye","peynir","çocuk","şehir","kahve","şirket","bilgisayar","ülke","zarar","kız","gün","doktor","köpek","kapı","göz","yüz","gerçek","aile","baba","korku","his","balık","çiçek","yiyecek","orman","özgürlük","arkadaş","eğlence","oyun","bahçe","kız","bardak"]

else:
    word_pool=["abruptly","absurd","abyss","affix","askew","avenue","awkward","axiom","azure","bagpipes","bandwagon","banjo","bayou","beekeeper","bikini","blitz","blizzard","boggle","bookworm","boxcar","boxful","buckaroo","buffalo","buffoon","buxom","buzzard","buzzing","buzzwords","caliph","cobweb","cockiness","croquet","crypt","curacao","cycle","daiquiri","dirndl","disavow","dizzying","duplex","dwarves","embezzle","equip","espionage","euouae","exodus","faking","fishhook","fixable","fjord","flapjack","flopping","fluffiness","flyby","foxglove","frazzled","frizzled","fuchsia","funny","gabby","galaxy","galvanize","gazebo","giaour","gizmo","glowworm","glyph","gnarly","gnostic","gossip","grogginess","haiku","haphazard","hyphen","iatrogenic","icebox","injury","ivory","ivy","jackpot","jaundice","jawbreaker","jaywalk","jazziest","jazzy","jelly","jigsaw","jinx","jiujitsu","jockey","jogging","joking","jovial","joyful","juicy","jukebox","jumbo","kayak","kazoo","keyhole","khaki","kilobyte","kiosk","kitsch","kiwifruit","klutz","knapsack","larynx","lengths","lucky","luxury","lymph","marquis","matrix","megahertz","microwave","mnemonic","mystify","naphtha","nightclub","nowadays","numbskull","nymph","onyx","ovary","oxidize","oxygen","pajama","peekaboo","phlegm","pixel","pizazz","pneumonia","polka","pshaw","psyche","puppy","puzzling","quartz","queue","quips","quixotic","quiz","quizzes","quorum","razzmatazz","rhubarb","rhythm","rickshaw","schnapps","scratch","shiv","snazzy","sphinx","spritz","squawk","staff","strength","strengths","stretch","stronghold","stymied","subway","swivel","syndrome","thriftless","thumbscrew","topaz","transcript","transgress","transplant","triphthong","twelfth","twelfths","unknown","unworthy","unzip","uptown","vaporize","vixen","vodka","voodoo","vortex","voyeurism","walkway","waltz","wave","wavy","waxy","wellspring","wheezy","whiskey","whizzing","whomever","wimpy","witchcraft","wizard","woozy","wristwatch","wyvern","xylophone","yachtsman","yippee","yoked","youthful","yummy","zephyr","zigzag","zigzagging","zilch","zipper","zodiac","zombie"]


#for 3 list
index=random.randint(0,len(word_pool)-1)

#game end
game_end=word_pool[index]

#backend
chosen_word=list(word_pool[index])

#fronted
index_word=list(word_pool[index])

for i in range(0,len(index_word)):
    index_word[i]="_"


# banner

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
os.system("cls")
health=0
game_win=0
print(HANGMANPICS[health])
print(index_word)

while not health == 6:
    
    char = str(input("Give a char:"))

    if char in chosen_word:   
        while char in chosen_word:
            a = chosen_word.index(char)
            chosen_word[a]=1
            index_word[a]=char

        #Check all done
            for index_of_char in range(0,len(chosen_word)):
                if index_of_char == 1:
                    game_win+=1
            
            if game_win == len(chosen_word):
                print("You win!")
                sys.exit()
        os.system("cls")
        print(HANGMANPICS[health])
        print(index_word)

    else:
        health +=1
        os.system("cls")
        print(HANGMANPICS[health])
        print(index_word)
print("Game Over!")
print(f"Word was:{game_end}")