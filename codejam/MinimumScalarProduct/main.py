def solve(v1, v2):
    """Returns the minimum scalar product of two vectors
    by permutating the coordinates"""
    v1 = sorted(v1)
    v2 = sorted(v2, reverse=True)
    
    return sum(x*y for x,y in zip(v1,v2))


# Some plumbing to parse the input files from stdin
if __name__ == "__main__":
    import sys
    
    n_tests = int(sys.stdin.readline().strip('\n'))
    for t in range(n_tests):
        n = int(sys.stdin.readline().strip('\n'))
        v1 = [int(x) for x in sys.stdin.readline().strip('\n').split()]
        assert len(v1) == n
        v2 = [int(x) for x in sys.stdin.readline().strip('\n').split()]
        assert len(v2) == n
        
        print("Case #{:d}: {:d}".format(t+1, solve(v1, v2)))
