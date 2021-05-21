import sys
from lib.util import *

def main(args):
  urls2rdf(args)

if __name__ == '__main__':
  args = sys.argv
  del args[0]
  main(args)