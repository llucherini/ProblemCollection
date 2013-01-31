def solve(credit, items):
    """Looks for the two matching integers that add up to the credit provided, and returns their position.
    Visit http://code.google.com/codejam/contest/351101/dashboard for more information"""

    # By knowing the target credit, for each integer i already know what i need to look for.
    # Keeping track of them with a dictionary allows me to quickly recognise if i have found
    # the pair i am looking for, without any search or sorting involved.
    needed = {}
    for index,item in enumerate(items):
        if item in needed:
            return needed[item], index
        needed[credit-item] = index


# Some plumbing to parse the input files from stdin
if __name__ == "__main__":
    import sys
    
    n_tests = int(sys.stdin.readline().strip())
    for n in xrange(n_tests):
        credit = int(sys.stdin.readline().strip())
        n_items = int(sys.stdin.readline().strip())
        items = [int(x) for x in sys.stdin.readline().strip().split(' ')]

        assert n_items == len(items)
        p1, p2 = solve(credit, items)
        print "Case #%d: %d %d" % (n+1, p1+1, p2+1)
        
