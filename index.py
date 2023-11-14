import appJar as aj
import pandas as pd

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

total_orders = 0
orders = pd.DataFrame(columns=["Name", "Flavor", "Scoops", "Toppings", "Total Price"])

# Function to serve ice cream by: Adam Sabry, Bryan Phu, Nyan Win Moe, Brandon Ngo
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
        message = f"Here is your {flavor} ice cream with {', '.join(chosen_toppings)}. Enjoy!\n Now enter the number 4 to view your total cost."
    elif scoops == 2:
        message = f"Here are your two scoops of {flavor} ice cream with {', '.join(chosen_toppings[:-1])} and {chosen_toppings[-1]}. Enjoy!\n Now press the number 4 to view, and pay your total cost."
    elif scoops == 3:
        toppings_except_last = ', '.join(chosen_toppings[:-1])
        last_topping = chosen_toppings[-1]
        message = f"Here are your three scoops of {flavor} ice cream with {toppings_except_last}, and {last_topping}. Enjoy!\n Now press the number 4 to view, and pay your total cost."

    return message

# Initialize the AppJar GUI
app = aj.gui("Spartans Ice Cream Shop", "400x400")

# Set background colors
app.setBg("lightblue")

#App additions by Bryan Phu
# Add labels and widgets to the GUI
app.addLabel("lbl_name", "1. Please enter your name:")
app.addLabelEntry("Name")
app.addLabel("lbl_flavor", "2. Select flavor:")
app.addOptionBox("Flavor", ice_cream_flavors)
app.setOptionBoxBg("Flavor", "white")  # Set background color for the option box
app.addLabel("lbl_scoops", "3. Select amount of scoops (1-3):")
app.addSpinBox("Scoops", [1, 2, 3])
app.addLabel("lbl_toppings", "4. Select Toppings: \n(FYI press the ctrl key as you select them in order to select multiple toppings)")
app.addListBox("Toppings", toppings)
app.setListBoxMulti("Toppings")

# Function to handle button clicks: By Brandon Ngo
def button_click(button):
    if button == "Order Ice Cream":
        customer_name = app.getEntry("Name")
        flavor = app.getOptionBox("Flavor")
        topping_indices = app.getListItems("Toppings")
        scoops = int(app.getSpinBox("Scoops"))

        if not customer_name:
            app.errorBox("Error", "Please enter your name.")
        elif not flavor:
            app.errorBox("Error", "Please select a flavor.")
        elif not 1 <= scoops <= 3:
            app.errorBox("Error", "Please select 1 to 3 scoops.")
        else:
            if len(topping_indices) != len(set(topping_indices)):
                app.errorBox("Error", "Please choose each topping only once.")
            else:
                # Calculate the total price
                flavor_price = 3.00
                topping_price = 0.50
                total_price = (flavor_price + len(topping_indices) * topping_price) * scoops

                # Serve ice cream and display the order
                message = serve_ice_cream(flavor, topping_indices, scoops)

                # Add the order to the orders DataFrame by: Nyan Win Moe 
                global orders
                orders = orders.append({
                    "Name": customer_name,
                    "Flavor": flavor,
                    "Scoops": scoops,
                    "Toppings": ', '.join(topping_indices),
                    "Total Price": total_price
                }, ignore_index=True)

                app.clearAllEntries()  # Clear input fields
                app.infoBox("Order Placed", message)  # Display the order message

    # Add the rest of your button handlers here...

# Add the buttons, including "Order Ice Cream": By Adam Sabry, Nyan Win Moe, Bryan Phu
app.addButtons(["Order Ice Cream", "View Menu", "Calculate Total Price", "View Total Orders", "Exit"], button_click)

# Start the GUI
app.go()
