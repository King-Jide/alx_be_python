while True:
    #1. Ask user to input the current weather.
    weather = input("What's the weather like today? (sunny/rainy/cold):").strip().lower()

    #2. Provide Clothing recommendations

    if weather == "sunny":
        print("Wear a t-shirt and sunglasses.")
    elif weather == "rainy":
        print("Don't forget your umbrella and a raincoat.")
    elif weather == "cold":
        print("Make sure to wear a warm coat and a scarf.")
    # else:
    #     print("Sorry, I don't have recommendations for this weather.")

    #Ask to try again
    play_again = input("Do you wish to get another recommendation? (y/n)").strip().lower()
    if play_again != 'y':
        print("Thanks for trying out our product")
        break


