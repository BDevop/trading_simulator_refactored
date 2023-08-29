import random

from data import strategies, ticker
from art import logo

isStrategy = False
isPlaying = False

print(logo)
print("Welcome! The goal of this simulator is to ingrain a simple yet important concept in trading. Risk Management.\n"
      "You will choose a profitable strategy, and you must walk away with as much profit as possible. Good luck!\n")

index = 1
for i in strategies:
    print(f"{index}. {i.upper()}")
    index += 1

while isStrategy is False:

    strategy = input("\nWhich strategy would you like to choose? Type 'exit' to quit. ").lower()

    if strategy in strategies:
        isPlaying = True
        isStrategy = True
        startBalance = random.randint(2000, 8000)
        balance = startBalance
        tradeCount = 0
        totalRisk = 0

        while isPlaying:

            price = random.randint(30, 150)
            print(f"\nOPPORTUNITY PRESENTED:\n"
                  f"Stock: {random.choice(ticker)}\n"
                  f"Price: ${price}\n"
                  f"Balance: ${balance}\n")

            risk = input("How much would you like to risk on this trade? ")

            if risk.isdigit() and int(risk) <= balance:
                outcome = int(random.choice(strategies[strategy]['numbers']))
                balance += int(risk) * outcome
                totalRisk += int(risk)
                tradeCount += 1

                print(f"\nTrading Result: {outcome}x Risk\n"
                      f"Dollar Result: ${int(risk) * outcome}\n"
                      f"Account Balance: ${balance}\n\n"
                      f"Trade Count: {tradeCount}\n")
            else:
                print("Invalid Input.\n")

            if balance <= 0:
                break

            playing = input("Do you want to place another trade? Y/N ").lower()

            if playing == "n" or playing == "no" or balance <= 0:
                isPlaying = False

        winRate = strategies[strategy]['win rate']
        lossRate = strategies[strategy]['loss rate']
        expectancy = strategies[strategy]['expectancy']
        expectedDollar = round(startBalance + totalRisk * expectancy)

        print(f"\nEXPECTED STATISTICS:\n"
              f"Strategy Win Rate: {winRate}%\n"
              f"Strategy Loss Rate: {lossRate}%\n"
              f"Strategy Expectancy: {expectancy}\n\n"
              f"Expected Account Value: ${expectedDollar}\n"
              f"Actual Account Value: ${balance}\n")

        if balance <= expectedDollar:
            print("YOU UNDER-PERFORMED THE STRATEGY!\n")
        else:
            print("YOU OUT-PERFORMED THE STRATEGY!\n")

        print(f"* With an expectation of {expectancy}, we expect to make ${expectancy} for every $1 at risk.")

    elif strategy == 'exit':
        break
    else:
        print("Invalid Input.")
