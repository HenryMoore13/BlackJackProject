from random import shuffle


def make_deck():
    deck = []
    for _suit in range(4):
        for i in range(2, 11):
            deck.append(i)
        # for _facecard in range(3):
        #     deck.append(10)
        deck.extend(['King', 'Queen', 'Jack'])
        deck.append('Ace')
    shuffle(deck)
    return deck


def hand_value(hand):
    ''' list(cards) -> int

    >>> hand_value([4, 'Ace'])
    15
    '''
    hand_total = 0
    aces = 0
    for card in hand:
        if card == 'Ace':
            aces += 1
        elif card == 'King' or card == 'Queen' or card == 'Jack':
            hand_total += 10
        else:
            hand_total = hand_total + card

    if aces == 0:
        return hand_total
    else:
        gap = 11 + (aces - 1)
        if hand_total + gap <= 21:
            return hand_total + gap
        else:
            return hand_total + aces


def choice(hand, deck):
    print('You:    {} ({})'.format(hand, hand_value(hand)))
    while True:
        print('\n(Hit)           (Stay)')
        choice = input('Would You Like To Hit Or Stay?? ').strip().upper()
        if choice == 'HIT':
            card = deck.pop()
            hand.append(card)
            print('\nDrew an {}'.format(card))
            print('You:    {} ({})'.format(hand, hand_value(hand)))
            total = hand_value(hand)

            if total > 21:
                print('BUST')
                break
            elif total == 21:
                print('BLACKJACK!!')
                break
            continue
        elif choice == 'STAY':
            print('\nStayed at {} ({})'.format(hand, hand_value(hand)))
            break
        else:
            print('invalid choice')


def dealer_choice(hand, deck):
    while True:
        print('Dealer:    {} ({})'.format(hand, hand_value(hand)), end='')
        dealer_value = hand_value(hand)
        input()
        if dealer_value < 17:
            card = deck.pop()
            print('dealer draws {}'.format(card))
            hand.append(card)
            total = hand_value(hand)
            if total > 21:
                print('Dealer bust at {} ({})'.format(hand, hand_value(hand)))
                print('BUST')
                break
            elif total == 21:
                print('Dealer 21 at {} ({})'.format(hand, hand_value(hand)))
                print('BLACKJACK!!')
                break
            continue
        else:
            print('Dealer stops at {} ({})'.format(hand, hand_value(hand)))
            break


def show_hands(hand, dealer):
    print('\nYou have {} @ {} points'.format(hand, hand_value(hand)))
    print('Dealer has {} @ {} points'.format(dealer, hand_value(dealer)))


def winner(hand, Dealer):
    player_value = hand_value(hand)
    dealer_value = hand_value(Dealer)
    if player_value > 21 or dealer_value > 21:
        if player_value > 21:
            print('\nBUST - dealer wins')
        else:
            print('\nplayer wins!!')
    elif player_value == dealer_value:
        print('\nPUSH!')
    elif player_value > dealer_value:
        print('\nThe BlackJack King!!')
    else:
        print('\nDealer takes your money')


def black_jack():
    deck = make_deck()

    Dealer = []
    Dealer.append(deck.pop())
    Dealer.append(deck.pop())
    print('Dealer:[{}, ?]'.format(Dealer[0]))
    Henry = []
    Henry.append(deck.pop())
    Henry.append(deck.pop())
    print('\nPLAYER PLAYER PLAYER')
    choice(Henry, deck)
    print('\nDEALER DEALER DEALER')
    dealer_choice(Dealer, deck)
    show_hands(Henry, Dealer)
    winner(Henry, Dealer)


def main():
    black_jack()


if __name__ == '__main__':
    main()
