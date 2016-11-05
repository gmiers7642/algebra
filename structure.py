import numpy as np

class Structure(object):
    def __init__(self, s, table):
        try:
            table.shape[0] == table.shape[1]
        except ValueError:
            print "Error, this is not a proper table!"
        self.table = table
        self.st = set(s)


    def __repr__(self):
        output = 'Set:\n' + str('{' + ''.join(self.st) + '}' + "\n") + "\nTable:\n"
        for row in range(self.table.shape[0]):
            output += ( str(" ".join(self.table[row,:] ) ) ) + "\n"
        return output

    def has_closure(self):
        return set(self.st) == set(np.unique(self.table))

    def is_associative(self):
        pass

    def has_identity(self):
        pass

    def has_inverse(self):
        pass

# To test input, and printing
def unit001():
    g1 = np.array( [['a', 'b'], ['b', 'a']] )
    s1 = Structure(set('ab'), g1)
    print "Structure 1:"
    print s1

# To test closure
def unit002():
    g1 = np.array( [['a', 'b'], ['b', 'a']] )
    s1 = Structure(set('ab'), g1)
    if s1.has_closure():
        print "s1 has closure"
    else:
        print "s1 does not have closure"

    g2 = np.array( [['a', 'c'], ['b', 'a']] )
    s1 = Structure(set('ab'), g2)
    if s1.has_closure():
        print "s1 has closure"
    else:
        print "s1 does not have closure"

if __name__ == '__main__':
    # To test input, and printing
    #unit001()

    # To test has_closure() function
    unit002()
