from random import shuffle
from time import sleep


def war_game():
    cards = [
        2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7,
        8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12,
        13, 13, 13, 13, 14, 14, 14, 14
    ]
    ply1pile = []
    ply2pile = []
    shuffle(cards)
    player1 = cards[:26]
    player2 = cards[26:]
    cards_on_table = []
    game_number = 0
    while len(player1) > 0 and len(player2) > 0:
        print('Draw Card!!!')
        game_number += 1
        player1card = player1.pop()
        cards_on_table.append(player1card)
        player2card = player2.pop()
        cards_on_table.append(player2card)
        print(
            'you: ({}), computer: ({})'.format(player1card, player2card),
            end='       ')
        if player1card > player2card:
            ply1pile.extend(cards_on_table[:])
            cards_on_table.clear()
            print('you win! ({})Cards\n'.format(len(player1) + len(ply1pile)))
        elif player2card > player1card:
            ply2pile.extend(cards_on_table[:])
            cards_on_table.clear()
            print('you lose! ({})Cards\n'.format(len(player1) + len(ply1pile)))
        else:
            phrase = ['\n\nI.', 'Declare.', 'WAR!']
            for i in range(3):
                sleep(.5)
                print(phrase[i],
                      ('({})Cards').format(len(player1) + len(ply1pile)))
                if len(player1) == 0:
                    player1 = ply1pile[:]
                    ply1pile = []
                    shuffle(player1)
                    print('\nYOU Shuffled')
                if len(player2) == 0:
                    player2 = ply2pile[:]
                    ply2pile = []
                    shuffle(player2)
                if len(player1) == 0 or len(player2) == 0:
                    break

                tie_card_1 = player1.pop()
                cards_on_table.append(tie_card_1)
                tie_card_2 = player2.pop()
                cards_on_table.append(tie_card_2)
        print()

        if len(player1) == 0:
            player1 = ply1pile[:]
            ply1pile = []
            shuffle(player1)
            print('YOU Shuffled\n')
        if len(player2) == 0:
            player2 = ply2pile[:]
            ply2pile = []
            shuffle(player2)
    sleep(1)
    print(['YOU', 'Computer'][len(player2) > len(player1)], 'Win!!')
    print('{} hands played'.format(game_number))


def main():
    war_game()


if __name__ == '__main__':
    main()
