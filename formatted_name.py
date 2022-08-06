# RETURNING A SIMPLE VALUE
# MAKING AN ARGUMENT OPTIONAL

def get_formatted_name(first_name, last_name, middle_name = ''):  # function combines two names.
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name  # full_name is converted to title case.
    else:
        full_name = first_name + ' ' + last_name  # full_name is converted to title case.
    return full_name.title()  # returned to the calling line
# When you call a function that returns a value, you need to provide a
# variable where the return value can be stored.


musician = get_formatted_name('jimi', 'hendrix', 'lee')   # returned value is stored in the variable musician.
print(musician)

musician = get_formatted_name('eddy', 'guzman')
print(musician)
