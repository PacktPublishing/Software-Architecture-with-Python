# Code listing #27

# Note: This contains a second fix only for the find_optimal_route_to_my_office_from_home function
# Since this is a fixed module, and its second version, we will call it metrictest_fix2.py.

import random

def find_optimal_route_to_my_office_from_home(start_time,
                                              expected_time,
                                              favorite_route='SBS1K',
                                              favorite_option='bus'):
    """ Find optimal route for me to go from home to office.
    First two inputs should be datetime instances.
    
    """
    
    # Convert to minutes
    tdiff = (expected_time - start_time).total_seconds()/60.0

    options = {range(0, 30): 'car',
               range(30, 45): ('car', 'metro'),
               range(45, 60): ('bus:335E', 'bus:connector')}


    if tdiff < 80:
        # Pick the range it falls into
        for drange in options:
            if tdiff in drange:
                return drange[tdiff]
            
    # Might as well go by normal bus
    return random.choice(('bus:330', 'bus:331',':'.join((favorite_option,
                                                         favorite_route))))
