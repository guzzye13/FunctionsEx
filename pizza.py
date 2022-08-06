# PASSING AN ARBITRARY NUMBER OF ARGUMENTS
# Python allows a function to collect an arbitrary number of arguments from the calling statement.
# MIXING POSITIONAL AND ARBITRARY ARGUMENTS

def make_pizza(size, *toppings):  # * tells python to make an empty tuple called toppings
    # and pack whatever values it receives into this tuple.
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


#make_pizza(16, 'pepperoni')
#make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')