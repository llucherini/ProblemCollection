# Google Code Jam - Reverse Words
# http://code.google.com/codejam/contest/351101/dashboard

# Some plumbing to parse the input files from stdin
if __name__ == "__main__":
    import sys
    
    n_tests = int(sys.stdin.readline().strip())
    for n in range(n_tests):
        words = sys.stdin.readline().strip().split(' ')

        print("Case #{:d}: {}".format(n+1, ' '.join(reversed(words))))
        
