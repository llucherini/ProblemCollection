from functools import reduce

def solve(n_flavors, customers):
    """Finds the minimum number of malted flavors needed to satisfy all customers.
    Takes as input the number of flavors, and list of customers, each represented with
    a dictionary in which each key holds a flavor number (0 <= n < n_flavors) they like, 
    and each value is a boolean that signals whether they like it malted (True) or not."""
    
    flavors = [0]*n_flavors
    unsatisfied_customers = find_unsatisfied_customers(customers, flavors)
    while unsatistied_customers:
        for customer in unsatisfied_customers:
            malted_flavor = get_favorite_malted_flavor(customers[customer])
            # If we have an unsatisfied customer which doesn't like any malted flavor
            # there is no solution because the flavors have been malted to satisfy
            # other customers. On the contrary, if he likes a malted flavor, we are
            # forced to malt it.
            if malted_flavor == -1:
                return []
            else:
                flavors[malted_flavor] = True
        # We might have generated new unsatisfied customers by malting flavors
        unsatisfied_customers = find_unsatisfied_customers(customers, flavors)
        
    return flavors

def get_favorite_malted_flavor(customer):
    """Returns the flavor number of the favorite malted flavor of the customer, -1 otherwise."""
    for flavor, malted in customer.items():
        if malted:
            return flavor

    return -1

def find_unsatisfied_customers(customers, flavors):
    """Filters the list of customers, leaving only the unsatisfied ones"""
    return list(filter(lambda x: not is_satisfied(customers[x], flavors), customers))

def is_satisfied(customer, flavors):
    """Returns a boolean signaling whether the customer is satisfied or not"""
    ret = False
    for flavor in customer:
        ret = ret or (customer[flavor] == flavors[flavor])

    return ret
    

# Some plumbing to parse the input files from stdin
if __name__ == "__main__":
    import sys
    
    n_tests = int(sys.stdin.readline().strip('\n'))
    for c in range(n_tests):
        n_flavors = int(sys.stdin.readline().strip('\n'))
        n_customers = int(sys.stdin.readline().strip('\n'))
        customers = {}
        for m in range(n_customers):
            customers[m] = {}
            data = sys.stdin.readline().strip('\n').split()
            likes = int(data[0])
            for t in range(1,(likes*2)+1,2):
                flavor = int(data[t])-1
                malted = bool(int(data[t+1]))
                customers[m][flavor] = malted
            
            assert len(customers[m]) == likes
            
        flavors = [int(x) for x in solve(n_flavors, customers)]
        ret = "Case #{:d}: ".format(c+1)
        if flavors:
            ret += ' '.join(str(x) for x in flavors)
        else:
            ret += "IMPOSSIBLE"
        print(ret)

