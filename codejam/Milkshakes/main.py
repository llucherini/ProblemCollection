from functools import reduce

def solve(n_flavors, customers):
    flavors = [0]*n_flavors
    print(customers)
    l = unsatisfied_customers(customers, flavors)
    while l:
        #print(list(unsatisfied_customers))
        #if not is_satisfied(customers[customer], flavors):
        for customer in l:
            malted_flavors = list(filter(lambda x: x[1], customers[customer].items()))
            # Only likes unmalted flavors?
            if not malted_flavors:
                return []
            else:
                flavors[malted_flavors[0][0]] = True
       
        l = unsatisfied_customers(customers, flavors)
        
    return flavors

def unsatisfied_customers(customers, flavors):
    return list(filter(lambda x: not is_satisfied(customers[x], flavors), customers))

def is_satisfied(customer, flavors):
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
            for t in range(1,likes+2,2):
                flavor = int(data[t])-1
                malted = bool(int(data[t+1]))
                customers[m][flavor] = malted
        
        flavors = [int(x) for x in solve(n_flavors, customers)]
        ret = "Case #{:d}: ".format(c+1)
        if flavors:
            ret += ' '.join(str(x) for x in flavors)
        else:
            ret += "IMPOSSIBLE"
        print(ret)

