from random import shuffle


def choice(hand, deck):
    print('\n(Hit)           (Stay)')

    while True:
        print('You:    {}'.format(hand))
        choice = input('Would You Like To Hit Or Stay??').strip().upper()
        if choice == 'HIT':
            hand.append(deck.pop())
            continue
        elif choice == 'STAY':
            break
        else:
            print('invalid choice')


def black_jack():
    Ace = 11
    K = 10
    Q = 10
    J = 10
    deck = [
        2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7,
        8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, J, J, J, J, Q, Q, Q, Q, K, K,
        K, K, Ace, Ace, Ace, Ace
    ]
    shuffle(deck)
    Dealer = []
    Dealer.append(deck.pop())
    print('Dealer: {} ?'.format(Dealer))
    Henry = []
    Henry.append(deck.pop())
    Henry.append(deck.pop())

    choice(Henry, deck)

    if sum(Henry) > 21:
        print('You Bust')

    if sum(Dealer) > 21:
        print('You Bust')

    print('You:    {}'.format(Henry))


def main():
    black_jack()


if __name__ == '__main__':
    main()
