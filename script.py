# At The Nile our biggest concern is our consumers, and our biggest cost is
# delivering their goods to them. We want to develop a program that will help
# us minimize these costs so we can continue making everyone happy.

# --- IMPORTS --- #

from nile import get_distance, format_price, SHIPPING_PRICES
from test import test_function

# --- FUNCTIONS --- #


# Define a function to calculate these costs
def calculate_shipping_cost(from_coords, to_coords, shipping_type="Overnight"):
    # Get the distance between the two coords points.
    distance = get_distance(*from_coords, *to_coords)
    # Getting the shipping rate related to the shipping type
    shipping_rate = SHIPPING_PRICES[shipping_type]
    # Calculate the price
    price = distance * shipping_rate
    # Return the formated price
    return format_price(price)


# At The Nile, we have a joke. Without our fantastic drivers, who fulfill
# orders every day, we’d just be sitting with millions of toys, electronics,
# and clothing in warehouses to ourselves. Our team is important, and we want
# to make sure the hardest workers find their home in our careers. In order
# to do that, we need to figure out who the best person is for each job.


# Define a function to find the cheapest driver
def calculate_driver_cost(distance, *drivers):
    # Define and set two variables to None in order to find the cheapest driver
    cheapest_driver = None
    cheapest_driver_price = None
    # Loop through each driver
    for driver in drivers:
        # Calculate each driver's delivery time
        driver_time = driver.speed * distance
        # Calculate each driver's cost
        price_for_driver = driver.salary * driver_time
        if cheapest_driver is None:  # Check if it is the first driver
            # Assign the first driver to cheapest_driver
            cheapest_driver = driver
            # Assign the first driver price to cheapest_driver_price
            cheapest_driver_price = price_for_driver
        # Check if the current driver cost is less than the actual cheapest
        elif price_for_driver < cheapest_driver_price:
            # Assign the current driver to cheapest_driver
            cheapest_driver = driver
            # Assign the current price_for_driver to the cheapest_driver_price
            cheapest_driver_price = price_for_driver
    # Return the cheapest driver cost and the cheapest driver
    return cheapest_driver_price, cheapest_driver

# Great first day, friend! Let’s try and figure out all the money you’ve
# saved us today.


# Define a function to calculate the money made today
def calculate_money_made(**trips):
    total_money_made = 0  # Setting a counter variable to 0
    for trip_id, trip in trips.items():  # Loop through each trip
        # Calculate the trip revenue
        trip_revenue = trip.cost - trip.driver.cost
        # Add it to the total_money_made counter
        total_money_made += trip_revenue
    # Return the total
    return total_money_made


# --- TESTS --- #

# Test the calculate_shipping_cost function
test_function(calculate_shipping_cost)  # PASSED

# Test the calculate_driver_cost function
test_function(calculate_driver_cost)  # PASSED

# Test the calculate_money_made function
test_function(calculate_money_made)  # PASSED
