# ya.algorithms.qualification
def strToint(s):
    res=s.split()
    res=map(int,res)
    return res
  
def main():
    with open("input.txt","r") as infile:
        refset = strToint(infile.readline())
        n=eval(infile.readline())
        for i in xrange(n):
            ticket=strToint(infile.readline())
            with open("output.txt","w") as outfile:
                if (len(list(set(refset).intersection(ticket)))>2):
                    outfile.write("Lucky\n")
                else:
                    outfile.write("Unlucky\n")
    return 0

if __name__ == '__main__':
	main()
