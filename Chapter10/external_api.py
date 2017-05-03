# Code Listing #6

"""

Showing how to debug programs with external dependencies such as an API
Note: This code is only for illustrative purposes and is not executable.

"""

import external_api

def process(json_data, skey='suspect_key',svalue='suspect_value'):
    """ Fake the external API except for the suspect key & value """

    # Assume each JSON element maps to a Python dictionary

    for json_elem in json_data:
        skip = False
        
        for key in json_elem:
            if key == skey:
                if json_elem[key] == svalue:
                    # Suspect key,value combination - dont process
                    # this JSON element
                    skip = True
                    break
                
        # Pass on to the API
        if not skip:
            external_api.process(json_elem)
                
    
def process_data(data):
    """ Process data using external API """

    # Clean up data - local function
    data = clean_up(data)
    # Drop duplicates from data - local function
    data = drop_duplicates(data)

    # Process line by line JSON
    for json_elem in data:
        external_api.process(json_elem)
