import random

print('''💎💎💎💎💎💎💎💎💎💎
Hello, and welcome to Diamond Slots.
A fun and exciting game where you can win MILLIONS!
💎💎💎💎💎💎💎💎💎💎\n''')
def pull():
    ascii_shapes = [
    "🍒",  
    "🔔",    
    "💎", 
    "🍋",   
    "🍉", 
    "⭐",     
    "🍀",   
    "🥥",  
    "💰",
    "🎰"]

    deposit_amount = int(input('How much money would you like to deposit to begin playing? '))
    while deposit_amount <= 0:
        print("Deposit must be greater than 0.")
        deposit_amount = int(input('Please enter a valid deposit amount: '))

    keep_playing = True
    while keep_playing:
        # Placing a bet
        bet = int(input(f'Your current balance is £{deposit_amount}. How much would you like to bet? '))
        while bet <= 0 or bet > deposit_amount:
            print(f"Invalid bet! It must be between 1 and your current balance (£{deposit_amount}).")
            bet = int(input('Please enter a valid bet amount: '))

        deposit_amount -= bet

        # Spin the slots
        slots1 = [random.choice(ascii_shapes) for _ in range(3)]
        slots2 = [random.choice(ascii_shapes) for _ in range(3)]
        slots3 = [random.choice(ascii_shapes) for _ in range(3)]
        print(f"Slots result:\n{slots1}\n{slots2}\n{slots3}")

        # Check results
        if len(set(slots2)) == 3:
            print(f'Unlucky, you lost £{bet}\nCash in account: £{deposit_amount}')
        elif len(set(slots2)) == 2:
            deposit_amount += 2 * bet
            print(f'Congratulations! You doubled your bet.\nCash in account: £{deposit_amount}')
        elif slots2 == ["💎","💎","💎"]:
            print('YOU WON THE JACKPOT!')
            deposit_amount += 1000000
        else:
            deposit_amount += 3 * bet
            print(f'Jackpot! You tripled your bet.\nCash in account: £{deposit_amount}')

        # Check if player wants to continue
        if deposit_amount <= 0:
            print("You're out of money. Game over!")
            break

        keep_playing = input('Do you want to keep playing? (yes/no): ').strip().lower() == 'yes'


    print("Thanks for playing! Final balance: £{}".format(deposit_amount))




print(pull())