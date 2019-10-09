def reflex_vacuum(loc, status):
    ret = ''
    if status == 'clean' or status == 'dirty':
        if loc != 'A' and loc != 'B':
            ret = 'invalid'
        elif status == 'dirty':
            ret = 'suck'
        else:
            if loc == 'A':
                ret = 'right'
            elif loc == 'B':
                ret = 'left'
            else:
                ret = 'invalid'
    else:
        ret = 'invalid'

    return ret


if __name__ == '__main__':
    print(reflex_vacuum('C', 'dirty'))
    print(reflex_vacuum('A', 'clean'))
    print(reflex_vacuum('B', 'clean'))


