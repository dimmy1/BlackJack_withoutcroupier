import random
from Deck import deck


random.shuffle(deck)


print("Let's play?")
count = 0


while True:
    choice = input('Will you take a card? Yes/No\n')
    if choice == 'Yes':
        current = deck.pop()
        print("You got a card of value: %d" %current)
        count += current
        if count > 21:
            print('Sorry, but you lose!')
            break
        elif count == 21:
            print('Congratulations, you scored 21!')
            break
        else:
            print('You score %d points.' %count)
    elif choise == "No":
        print('You score %d points and you finish the game!' %count)
        break


print("See you soon!")