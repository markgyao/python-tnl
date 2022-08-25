from dataclasses import dataclass
from scipy.stats import norm
import sys

def main():
    # print command line arguments
    for arg in sys.argv[1:]:
        print(arg)
    x=32
    mus=[10,15,28,30,32,40,45]
    cgs=[1,2,3,4,5]
    for mu in mus:
        print("{},{:.8f}".format(mu,norm(mu,cgs[0]).pdf(x)))
    print("\n\n")
    for cg in cgs:
        print("{},{:.8f}".format(cg,norm(mus[4],cg).pdf(x)))

if __name__ == "__main__":
    main()


