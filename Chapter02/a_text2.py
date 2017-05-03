# Code listing #15

""" Module A (a.py) - Provides string processing functions """

# Note - This is the rewritten version of a_text.py so called a_text2.py

def ntimes(string, char):
    """ Return number of times character 'char' 
    occurs in string """

    return string.count(char)

def common(string1, string2):
    """ Return common words across strings1 1 & 2 """
    
    s1 = set(string1.lower().split())
    s2 = set(string2.lower().split())
    return s1.intersection(s2)  

def common_words(text1, text2):
    """ Return common words across text1 and text2 """
    
    # A text is a collection of strings split using newlines
    strings1 = text1.split("\n")
    strings2 = text2.split("\n")
    
    common_w = []
    for string1 in strings1:
        for string2 in strings2:
            common_w += common(string1, string2)

    return list(set(common_w))
