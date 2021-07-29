import hangman_art as h_art
import requests
from lxml import html
#from replit import clear

# request the page
page = requests.get('https://randomword.com/')
# parsing the page
tree = html.fromstring(page.content)

chosen_word = str(
    list.pop(tree.xpath('/html/body/div[4]/div[1]/div[1]/text()')))
hint = hint = str(
    list.pop(tree.xpath('/html/body/div[4]/div[1]/div[2]/text()')))
word_length = len(chosen_word)
end_of_game = False
lives = 6

#INTRO
print(h_art.logo)

#TESTER'S SOLUTION :
#print(f'Pssst, the solution is {chosen_word}.')

#DECLARATIONS
display = []
guessed_letters = []
for _ in range(word_length):
    display += "_"

#the main game
while not end_of_game:
    print(f"{' '.join(display)}\n \nPsst, Hint : {hint} \n")
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print(f"\nYou've already guessed '{guess}'\n")
        continue
    else:
        guessed_letters += guess

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            
    #clear()

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"{' '.join(display)}")
            print(h_art.stages[0])
            print(f"The word was {chosen_word}.\nYou lose. ")
            break

    print(h_art.stages[lives])
    if "_" not in display:
        end_of_game = True
        print("You win.")
