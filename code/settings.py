'''
Created on Nov 11, 2013

@author: nicodjimenez

List of special characters that will be treated differently than others.  
'''

import cPickle 

# maps symbols with special components to the number of strokes they contain
mult_comp_symbols = {
                '=':2,
                'i':2,
                '\tan':4,
                '\cos':3,
                '\sin':4, 
                '\geq':2,
                '\leq':2,
                '\log':3,
                '\div':3,
                '\lim':4,
                '!':2,
                '\ldots':3,
                }

def load_data():
    with open("../pickle_files/clean_symbols.p",'rb') as f: 
        data = cPickle.load(f)
        
    return data
    