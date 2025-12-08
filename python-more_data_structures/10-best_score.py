#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    
    bk = None
    mv = -float('inf')

    for key, value in a_dictionary.items():
        
        if value > mv:
            mv = value
            bk = key
            
    return bk
