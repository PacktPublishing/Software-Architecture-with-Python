# Code Listing #8

"""

Serialization exploit using JSON

"""


# test_serialize_json.py
import os
import json
import datetime

class ExploitEncoder(json.JSONEncoder):
    def default(self, obj):
        if any(isinstance(obj, x) for x in (datetime.datetime, datetime.date)):
            return str(obj)
        
        # this will list contents of root / folder.
        return (os.system, ('ls -al /',))

def serialize():
    shellcode = json.dumps([range(10),
                            datetime.datetime.now()],
                           cls=ExploitEncoder)
    print(shellcode)
    return shellcode


def deserialize(exploit_code):
    print(json.loads(exploit_code))


if __name__ == '__main__':
    shellcode = serialize()
    deserialize(shellcode)
