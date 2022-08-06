# PASSING A LIST
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


usernames = ['eddy', 'oscar', 'alex', 'lupita']  # function loops through the list
# it receives and prints a greeting to each user. We defined a list of users and then
# pass the list usernames to greet_users().
greet_users(usernames)

