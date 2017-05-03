# Code Listing #13

"""

Printing using %s vs printing using .format

"""

def display_safe(employee):
    """ Display details of the employee instance """

    print("Employee: {name}, Age: {age}, profession: {job}".format(**employee))

def display_unsafe(employee):
    """ Display details of employee instance """

    print("Employee: %s, Age: %d, profession: %s" % (employee['name'],
                                                     employee['age'],
                                                     employee['job']))

if __name__ == "__main__":
    employee={'age': 25, 'job': 'software engineer', 'name': 'Jack'}
    display_safe(employee)
    display_unsafe(employee)    
