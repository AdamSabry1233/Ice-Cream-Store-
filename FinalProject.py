
import pandas as pd
from appJar import gui


# List of available ice cream flavors: By Adam Sabry
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

# List of available toppings: By Adam Sabry
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

total_orders = 0
# Ice cream serving funciton by: Adam Sabry
def serve_ice_cream(flavor, chosen_toppings, scoops):
    global total_orders
    total_orders += 1
    if scoops < 1:
        return "Sorry, we can't serve less than 1 scoop of ice cream."
    elif scoops > 3:
        return "Sorry, we can't serve more than 3 scoops of ice cream."

    if len(chosen_toppings) != len(set(chosen_toppings)):
        return "Sorry, you can't choose the same topping more than once."

    if scoops == 1:
        message = f"Here is your {flavor} ice cream with {', '.join(chosen_toppings)}. Enjoy!"
    elif scoops == 2:
        message = f"Here are your two scoops of {flavor} ice cream with {', '.join(chosen_toppings[:-1])} and {chosen_toppings[-1]}. Enjoy!"
    elif scoops == 3:
        toppings_except_last = ', '.join(chosen_toppings[:-1])
        last_topping = chosen_toppings[-1]
        message = f"Here are your three scoops of {flavor} ice cream with {toppings_except_last}, and {last_topping}. Enjoy!"

    return message
#Displaying order function by: Bryan Phu
def display_total_orders():
    global total_orders
    if total_orders == 1:
        return "We've served a total of 1 order here at Spartans Ice Cream Shop."
    else:
        return f"We've served a total of {total_orders} orders here at Spartans Ice Cream Shop."

#View menu function by: Nyan Win Moe
def view_menu():
    print("Available ice cream flavors:")
    for index, flavor in enumerate(ice_cream_flavors, start=1):
        print(f"{index}. {flavor}")
    print("\n Available toppings:")
    for index, topping in enumerate(toppings, start=1):
        print(f"{index}. {topping}")
#This function calculates the total price by: Brandon Ngo
def calculate_total_price(flavor, chosen_toppings, scoops):
    flavor_price = 3.00
    topping_price = 0.50
    total_price = (flavor_price + len(chosen_toppings) * topping_price) * scoops
    return total_price

# Initialize an empty DataFrame to store orders by: Bryan Phu
orders = pd.DataFrame(columns=["Customer Name", "Flavor", "Toppings", "Scoops", "Total Price"])

# Add the function to save orders to Excel by: Adam Sabry
def save_orders_to_excel():
    global orders
    try:
        existing_orders = pd.read_excel("Inventory.xlsx", engine='openpyxl')
        updated_orders = pd.concat([existing_orders, orders], ignore_index=True)
        updated_orders.to_excel("Inventory.xlsx", index=False, engine='openpyxl')
        print("Orders have been saved to the 'Inventory.xlsx' file.")
    except FileNotFoundError:
        # If the file is not found, create a new Excel file
        orders.to_excel("Inventory.xlsx", index=False, engine='openpyxl')
        print("Orders have been saved to the 'Inventory.xlsx' file.")

# Replace the original save_orders_to_excel() function with this modified one by: Brandon Ngo 

def is_name_valid(name):
    return all(char.isalpha() or char.isspace() for char in name)

#Main Function by: Adam Sabry, Bryan Phu, Brandon Ngo, and Nyan Win Moe
#Bryan
def main():
    global orders  # Declare 'orders' as a global variable
    
    try:
       orders = pd.read_excel("Inventory.xlsx", engine='openpyxl')
    except FileNotFoundError:
       # If the file is not found, create an empty DataFrame
       orders = pd.DataFrame(columns=["Customer Name", "Flavor", "Toppings", "Scoops", "Total Price"])
    


    customer_name = input('Welcome to Spartans Ice Cream Shop! Please enter your name: ')
    while not is_name_valid(customer_name):
        print("Invalid name. Please enter in a name containing letters.")
        customer_name = input("Please re-enter in your name: ")
    
    print(f'Hello {customer_name}! Here is our menu:')
    
    # Initialize a flag to track whether an order has been placed
    order_placed = False
#Brandon
    while True:
        print('1. Order Ice Cream')
        print('2. Exit')
        print('3. View Menu')
        print('4. Calculate Total Price')
        print('5. View the total number of orders placed')

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
#Moe
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

            # Set the flag to True after placing an order
            order_placed = True

            # Calculate the total price
            total_price = calculate_total_price(flavor, chosen_toppings, scoops)

            # Get order details
            order_data = {
                "Customer Name": customer_name,
                "Flavor": flavor,
                "Toppings": ", ".join(chosen_toppings),
                "Scoops": scoops,
                "Total Price": total_price
            }

            # Append the order to the DataFrame
            orders = pd.concat([orders, pd.DataFrame(order_data, index=[0])], ignore_index=True)

            message = serve_ice_cream(flavor, chosen_toppings, scoops)
            print(message)
#Adam
        elif choice == '2':
            print(f"Thank you, {customer_name}, for visiting Spartans Ice Cream Shop. Have a great day!")
            save_orders_to_excel()  # Save orders when exiting
            break
        elif choice == '3':
            view_menu()
        elif choice == '4':
            if order_placed:
                total_price = calculate_total_price(flavor, chosen_toppings, scoops)
                print(f"Your total price is ${total_price:.2f}")
            else:
                print("Please order your ice cream first before you attempt to calculate your total price.")
        elif choice == '5':
            display_total_orders()
        else:
            print("Invalid choice. Please select a valid option from the selection: (1/2/3/4/5).")
            
 #Adam           
app = gui("Spartans Ice Cream Shop", "400x300")

def order_ice_cream():
    global orders, customer_name, order_placed, flavor, chosen_toppings, scoops

    # Retrieve information from the GUI widgets
    customer_name = app.getEntry("Name")
    flavor = app.getOptionBox("Flavor")
    scoops = int(app.getSpinBox("Scoops"))
    
    #Bryan Get the selected indices of the toppings
    selected_indices = app.getListBoxPos("Toppings")

    if not customer_name:
        app.warningBox("Please enter in your name!")
        return
    
    if not flavor:
        app.warningBox("Please pick a flavor!")
        return
    
    if not scoops:
        app.warningBox("Please enter in the amount of scoops you would like!")
        return
    
    if not selected_indices:
        app.warningBox("No Toppings", "Please select at least one topping.")
        return
    
    # Moe Retrieve the values of the selected toppings using the indices
    chosen_toppings = [toppings[i] for i in selected_indices]

    # (Your existing order logic)
    message = serve_ice_cream(flavor, chosen_toppings, scoops)
    app.infoBox("Order Summary", message)
    order_placed = True
    
    # Get order details
    order_data = {
       "Customer Name": customer_name,
       "Flavor": flavor,
       "Toppings": ", ".join(chosen_toppings),
       "Scoops": scoops,
       "Total Price": calculate_total_price(flavor, chosen_toppings, scoops)
   }

   # Append the order to the DataFrame
    orders = pd.concat([orders, pd.DataFrame(order_data, index=[0])], ignore_index=True)


def press(button):
    global orders, customer_name, order_placed, flavor, chosen_toppings, scoops

    print("Button clicked:", button)  # Line for debugging

    if button == "Order Ice Cream":
        order_ice_cream()
    elif button == "Exit":
        app.infoBox("Thank You", f"Thank you, {customer_name}, for visiting Spartans Ice Cream Shop. Have a great day!")
        save_orders_to_excel()
        app.stop()
    elif button == "View Menu":
        app.infoBox("Menu", "Available ice cream flavors:\n" + "\n".join(ice_cream_flavors) +
                    "\n\nAvailable toppings:\n" + "\n".join(toppings))
    elif button == "Calculate Total Price":
        if order_placed:
            total_price = calculate_total_price(flavor, chosen_toppings, scoops)
            app.infoBox("Total Price", f"Your total price is ${total_price:.2f}")
        else:
            app.warningBox("No Order", "Please order your ice cream first before calculating the total price.")
    elif button == "View Total Orders":
        app.infoBox("Total Orders", display_total_orders())
        

# Brandon Add buttons and labels to the GUI
app.setBg("lightblue")

# App additions by Moe
# Add labels and widgets to the GUI
app.addLabel("lbl_title", "Spartans Ice Cream Shop")
app.addImage("decor","giphy.gif")
app.setFont(18)
app.addLabel("lbl_name", "1. Please enter your name:")
app.addLabelEntry("Name")
app.addLabel("lbl_flavor", "2. Select flavor: (price per flavor $3.00)")
app.addOptionBox("Flavor", ice_cream_flavors)
app.setOptionBoxBg("Flavor", "white")  # Set background color for the option box
app.addLabel("lbl_scoops", "3. Select amount of scoops (1-3): (price is multiplied by total scoops)")
app.addSpinBox("Scoops", [1, 2, 3])
app.addLabel("lbl_toppings", "4. Select Toppings: ($0.50 per topping) \n(Press the ctrl key as you select them in order to select multiple toppings)")
app.addListBox("Toppings", toppings)
app.setListBoxMulti("Toppings")

# Add buttons to trigger functions
app.addButtons(["Order Ice Cream", "Exit", "View Menu", "Calculate Total Price", "View Total Orders"], press)

# Run the GUI
app.go()

if __name__ == "__main__":
    # Print the content of the Excel file
    print(orders)
    main()
