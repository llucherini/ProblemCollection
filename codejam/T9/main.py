# Google Code Jam - T9
# http://code.google.com/codejam/contest/351101/dashboard#s=p2

translation_table = {
    'a' : '2',
    'b' : '22',
    'c' : '222',
    'd' : '3',
    'e' : '33',
    'f' : '333',
    'g' : '4',
    'h' : '44',
    'i' : '444',
    'j' : '5',
    'k' : '55',
    'l' : '555',
    'm' : '6',
    'n' : '66',
    'o' : '666',
    'p' : '7',
    'q' : '77',
    'r' : '777',
    's' : '7777',
    't' : '8',
    'u' : '88',
    'v' : '888',
    'w' : '9',
    'x' : '99',
    'y' : '999',
    'z' : '9999',
    ' ' : '0'
}

def solve(text):
    """Converts text into its T9 representation.
    Spaces are inserted when a pause between keypresses is needed"""
    ret = ''
    for char in text:
        digits = translation_table[char]
        # If the previous keypress is the same as the next one
        # i need to insert a pause to differentiate them
        if ret != '' and ret[-1] == digits[0]:
            ret += ' '
        ret += digits
    return ret

# Some plumbing to parse the input files from stdin
if __name__ == "__main__":
    import sys
    
    n_tests = int(sys.stdin.readline().strip('\n'))
    for n in range(n_tests):
        line = sys.stdin.readline().strip('\n')
        print("Case #{:d}: {}".format(n+1, solve(line)))
