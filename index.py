# List of available ice cream flavors
ice_cream_flavors = [
    "Vanilla",
    "Chocolate",
    "Strawberry",
    "Mint Chocolate Chip",
    "Cookies and Cream",
    "Butter Pecan",
    "Rocky Road",
    "Coffee",
    "Cookie Dough",
    "Pistachio",
]

# List of available toppings
toppings = [
    "Chocolate Sauce",
    "Caramel Sauce",
    "Whipped Cream",
    "Sprinkles",
    "Nuts",
    "Maraschino Cherries",
    "Crushed Oreo Cookies",
    "Chocolate Chips",
    "Mini Marshmallows",
    "Gummy Bears",
]

def serve_ice_cream(flavor, chosen_toppings, scoops):
    """Serve ice cream with the specified flavor, toppings, and number of scoops."""
    if scoops < 1:
        return "Sorry, we can't serve less than 1 scoop of ice cream."
    elif scoops > 3:
        return "Sorry, we can't serve more than 3 scoops of ice cream."

    if len(chosen_toppings) != len(set(chosen_toppings)):
        return "Sorry, you can't choose the same topping more than once."

    if scoops == 1:
        message = f"Here is your {flavor} ice cream with {', '.join(chosen_toppings)}. Enjoy!"
    elif scoops == 2:
        # Use 'and' to separate the last two toppings
        message = f"Here are your two scoops of {flavor} ice cream with {', '.join(chosen_toppings[:-1])} and {chosen_toppings[-1]}. Enjoy!"
    else:
        # Use 'and' to separate the last two toppings
        toppings_except_last = ', '.join(chosen_toppings[:-1])
        last_topping = chosen_toppings[-1]
        message = f"Here are your three scoops of {flavor} ice cream with {toppings_except_last}, and {last_topping}. Enjoy!"

    return message



def main():
    customer_name = input('Welcome to Spartans Ice Cream Shop! Please enter your name: ')
    print(f'Hello {customer_name}! Here is our menu:')

    while True:
        print('1. Order Ice Cream')
        print('2. Exit')

        choice = input('Enter your choice: ')
        if choice == '1':
            # Option 1: Order ice cream
            print("Available ice cream flavors:")
            for index, flavor in enumerate(ice_cream_flavors, start=1):
                print(f"{index}. {flavor}")

            try:
                flavor_choice = int(input("Enter the number of the ice cream flavor you'd like: "))
                if 1 <= flavor_choice <= len(ice_cream_flavors):
                    flavor = ice_cream_flavors[flavor_choice - 1]
                else:
                    print("Invalid flavor choice. Please select a valid flavor between 1-10.")
                    continue  # Continue the loop to re-enter the choice
            except ValueError:
                print("Invalid input format. Please enter a number.")
                continue  # Continue the loop to re-enter the choice

            print("Available toppings:")
            for index, topping in enumerate(toppings, start=1):
                print(f"{index}. {topping}")

            try:
                topping_choices = input("Enter topping numbers separated by spaces: ")
                topping_indices = [int(choice) for choice in topping_choices.split()]
                invalid_indices = [i for i in topping_indices if i < 1 or i > len(toppings)]
                if invalid_indices:
                    print("Invalid topping choice(s). Please select valid topping numbers.")
                    continue  # Continue the loop to re-enter the choice
                chosen_toppings = [toppings[i - 1] for i in topping_indices]
            except (ValueError, IndexError):
                print("Invalid input format. Please enter topping numbers separated by spaces.")
                continue  # Continue the loop to re-enter the toppings

            scoops = int(input("How many scoops would you like (1-3): "))
            if scoops < 1 or scoops > 3:
                print("Invalid number of scoops. Please select 1, 2, or 3.")
                continue  # Continue the loop to re-enter the choice

            message = serve_ice_cream(flavor, chosen_toppings, scoops)
            print(message)

        elif choice == '2':
            print(f"Thank you, {customer_name}, for visiting Spartans Ice Cream Shop. Have a great day!")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2).")

if __name__ == "__main__":
    main()
