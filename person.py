# RETURNING A DICTIONARY
def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}  # value of first_name is stored
    # with the key first.
    if age:
        person['age'] = age
    return person  # entire dictionary is returned.


musician = build_person('eddy', 'guzman', age=27)
print(musician)  # Return value is printed.