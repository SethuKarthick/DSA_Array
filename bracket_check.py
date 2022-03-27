def is_valid_parentheses(s):

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


res = is_valid_parentheses(s='([])')
print(res)