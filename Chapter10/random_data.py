# Code Listing #8

"""

Generating random data for applications - Generates random patient data

"""

import string
import random
import itertools

from schematics.models import Model
from schematics.types import BaseType, BooleanType, StringType, IntType, DecimalType, DateTimeType


class AgeType(IntType):
    """ An age type for schematics """
    
    def __init__(self, **kwargs):
        kwargs['default'] = 18
        IntType.__init__(self, **kwargs)
        
    def to_primitive(self, value, context=None):
        return random.randrange(18, 80)

class NameType(StringType):
    """ A schematics custom name type """
    
    vowels='aeiou'
    consonants = ''.join(set(string.ascii_lowercase) - set(vowels))

    def __init__(self, **kwargs):
        kwargs['default'] = ''
        StringType.__init__(self, **kwargs)
        
    def get_name(self):
        """ A random name generator which generates
        names by clever placing of vowels and consontants """

        items = ['']*4

        items[0] = random.choice(self.consonants)
        items[2] = random.choice(self.consonants)

        for i in (1, 3):
            items[i] = random.choice(self.vowels)            


        return ''.join(items).capitalize()

    def to_primitive(self, value, context=None):
        return self.get_name()

class GenderType(BaseType):
    """A gender type for schematics """
    
    def __init__(self, **kwargs):
        kwargs['choices'] = ['male','female']
        kwargs['default'] = 'male'
        BaseType.__init__(self, **kwargs)

class ConditionType(StringType):
    """ A gender type for a health condition """

    def __init__(self, **kwargs):
        kwargs['default'] = 'cardiac'
        StringType.__init__(self, **kwargs)     
        
    def to_primitive(self, value, context=None):
        return random.choice(('cardiac',
                              'respiratory',
                              'nasal',
                              'gynec',
                              'urinal',
                              'lungs',
                              'thyroid',
                              'tumour'))

class BloodGroupType(StringType):
    """ A blood group type for schematics  """

    def __init__(self, **kwargs):
        kwargs['default'] = 'AB+'
        StringType.__init__(self, **kwargs)
        
    def to_primitive(self, value, context=None):
        return ''.join(random.choice(list(itertools.product(['AB','A','O','B'],['+','-']))))        

    
class Patient(Model):
    """ A model class for patients """
    
    name = NameType() 
    age = AgeType()
    gender = GenderType()
    condition = ConditionType()
    doctor = NameType()
    blood_group = BloodGroupType()
    insured = BooleanType(default=True)
    last_visit = DateTimeType(default='2000-01-01T13:30:30')

if __name__ == "__main__":
     patients = list(map(lambda x: Patient.get_mock_object().to_primitive(), range(100)))
     for patient in patients:
         print(patient)
