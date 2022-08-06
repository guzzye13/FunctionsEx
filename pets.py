# PASSING ARGUMENTS
# POSITIONAL ARGUMENTS
# MULTIPLE FUNCTION CALLS
# DEFAULT VALUES
def describe_pet(pet_name='larry', animal_type='dog'):  # function with two arguments.
    # 'dog' is now set to default.
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(animal_type='hamster', pet_name='harry')  # function call stored with two arguments
describe_pet(pet_name='chip')  # function call stored with two arguments
# animal type is defaulted.
describe_pet()  # both arguments are set to be defaulted
