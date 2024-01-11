import time, random, sys, os

def main():
    slow_type("Welcome to Russian Roulette")
    time.sleep(1)
    round_one()



def slow_type(str):
    for letter in str:
        print(letter, end='')
        sys.stdout.flush()
        time.sleep(random.uniform(0, 0.3))
    print('')

def round_one():
    os.system('clear')
    slow_type('4 blank and 2 live rounds')
    rounds = [0, 0, 0, 0, 0, 1]
    random.shuffle(rounds)
    player = False
    dealer = False
    round = 0
    slow_type('Shoot yourself (me) or the dealer (dealer)')
    while not (player and dealer):
        choice = input()
        if round < len(rounds):
            if rounds[round] == 1:
                if choice == "me":
                    player = True
                    print('You are dead')
                    break
                else:
                    dealer = True
                    print('Dealer is dead')
                    break
            else:
                print('Blank round')
            round += 1
        else:
            print('No more rounds')
            break


if __name__ == "__main__":
    main()