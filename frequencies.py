"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    

    for i in range(0, len(items)):
        element = items[i]
        if type(element) != str:
           element = str(element)
        if frequencies.get(element) is None:
          frequencies[element] = 1
        else:
          frequencies[element] += 1 
      
        
                   
    # Your code goes here
    return frequencies
