# Code listing #26

# Note: This contains a fix only for the find_optimal_route_to_my_office_from_home function
# Since this is a fixed module, we will call it metrictest_fix1.py

import random

def find_optimal_route_to_my_office_from_home(start_time,
                                              expected_time,
                                              favorite_route='SBS1K',
                                              favorite_option='bus'):
                                                 
        # If I am very late, always drive.
        d = (expected_time - start_time).total_seconds()/60.0

        if d<=30:
            return 'car'
        elif d<45:
            return ('car', 'metro')
        elif d<60:
            # First volvo,then connecting bus
            return ('bus:335E','bus:connector')
        elif d>80:
            # Might as well go by normal bus
            return random.choice(('bus:330','bus:331',':'.join((favorite_option,
                        favorite_route))))
        # Relax and choose favorite route
        return ':'.join((favorite_option, favorite_route))
