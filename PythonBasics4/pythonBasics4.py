# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.

# # Part A.
def array_2_dict(emails, contacts):
    # YOUR CODE HERE\
    if len(emails) != 0:
        counter = 0
        for key, i in contacts.items():
            contacts[key] = emails[counter]
            counter += 1
        return contacts
    else:
        return contacts

# # Part B.
def array2d_2_dict(contact_info, contacts):
    # YOUR CODE HERE

    return

# # Part C.
def dict_2_array(contacts):
    # YOUR CODE HERE

    return

