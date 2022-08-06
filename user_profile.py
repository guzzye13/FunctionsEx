def build_profile(first, last, **user_info):  # ** is used to create an empty dictionary called user_info
    # and pack whatever name-value pairs it receives into this dictionary.
    """Build a dictionary containing everything we know about a user."""
    profile = {}  # empty dictionary 'profile'
    profile['first_name'] = first  # add first and last names to this dictionary
    profile['last_name'] = last
    for key, value in user_info.items():  # Loop through the additional key-value pairs in the dictionary
        # user_info and add each pair to the profile dictionary
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)