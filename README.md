


## $5 Tech Unlocked 2021!
[Buy and download this product for only $5 on PacktPub.com](https://www.packtpub.com/)
-----
*The $5 campaign         runs from __December 15th 2020__ to __January 13th 2021.__*

# Software Architecture with Python
This is the code repository for [Software Architecture with Python](https://www.packtpub.com/application-development/software-architecture-python?utm_source=github&utm_medium=repository&utm_campaign=9781786468529), published by [Packt](https://www.packtpub.com/?utm_source=github). It contains all the supporting project files necessary to work through the book from start to finish.
## About the Book
This book starts off by explaining how Python fits into an application architecture. As you move along, you will understand the architecturally significant demands and how to determine them. Later, you’ll get a complete understanding of the different architectural quality requirements that help an architect to build a product that satisfies business needs, such as maintainability/reusability, testability, scalability, performance, usability, and security.


## Instructions and Navigation
All of the code is organized into folders. Each folder starts with a number followed by the application name. For example, Chapter02.



The code will look like the following:
```
class PrototypeFactory(Borg):
    """ A Prototype factory/registry class """
    
    def __init__(self):
        """ Initializer """

        self._registry = {}

    def register(self, instance):
        """ Register a given instance """

        self._registry[instance.__class__] = instance

    def clone(self, klass):
        """ Return clone given class """

        instance = self._registry.get(klass)
        if instance == None:
            print('Error:',klass,'not registered')
        else:
            return instance.clone()

```

To follow the instructions given in this book, you need to have Python 3 installed on your system. The other prerequisites are mentioned at the respective instances.

## Related Products
* [Data Mining with Python: Implementing Classification and Regression](https://www.packtpub.com/big-data-and-business-intelligence/data-mining-python-implementing-classification-and-regression?utm_source=github&utm_medium=repository&utm_campaign=9781785885716)

* [Python Text Processing with NLTK 2.0 Cookbook: LITE](https://www.packtpub.com/application-development/python-text-processing-nltk-20-cookbook-lite?utm_source=github&utm_medium=repository&utm_campaign=9781849516389)
