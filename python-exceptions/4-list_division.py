#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    nl = []
    for i in range(0, list_length):
        try:
            div = my_list_1 / my_list_2
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            nl.append(div)
    return nl
