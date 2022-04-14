def is_valid(s):

    _dict = {  ']': '[', ')':'(', '}':'{'  }
    list_p = []
    
    for char in s:
        if char in _dict.values():
            list_p.append(char)
        elif char in _dict.keys():
            if list_p == [] or _dict[char] != list_p.pop():
                return False
        else:
            False
        
    
    return True if not len(list_p) else False


# is_valid_parentheses = is_valid(s='(())')
# print(is_valid_parentheses)



def is_valid_count(s):

    _dict = {  ']': '[', ')':'(', '}':'{'  }
    list_p = []
    count = 0
    
    for char in s:
        if char in _dict.values():
            list_p.append(char)
        elif char in _dict.keys():
            if list_p == [] or _dict[char] != list_p.pop():
                continue
            else:
                count += 1
        
    
    return count*2


is_valid_parentheses = is_valid_count(s='(())(')
print(is_valid_parentheses)