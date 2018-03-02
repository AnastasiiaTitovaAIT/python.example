# ya.algorithms.qualification
def strToint(s):
    res=s.split()
    res=map(int,res)
    return res

def main():
    with open("input.txt","r") as infile:
        n = eval(infile.readline())
        total = [strToint(infile.readline()) for x in xrange(2*n)] #reading data from input
        first = list([x[0] for x in total]) #list of first elements in lines in order to find first row
        print first
        fs = {first.count(x): x for x in first}
        fst_elem = fs[2]
        ref = list([x for x in total if x[0]==fst_elem])
        print ref
        total.remove(ref[1])
        print total
        with open("output.txt","w") as outfile:
            for i in xrange(n):
                for row in total:
                    if row[0]==ref[1][i]:
                        outfile.write( ' '.join(str(e) for e in row)+'\n')

if __name__ == '__main__':
	main()
