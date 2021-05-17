import sys
from lib.util import *

def switchArg(option, arg):
  if (option == '-r' or option == '--regex'):
    return generateTextsFromRegex(arg[0])
  if (option == '-l' or option == '--list'):
    return arg

def main(args):
  # regex 표현식인지 먼저 filtering
  urls = switchArg(args[0], args[1:])
  
  triples = []
  for url in urls:
    # triples.extend(generateTripleFromUrl(url))

  # rdf = generateRdfFromTriples(triples)
  # knowledgeGraph = generateKnowledgeGraphFromRdf(rdf)


if __name__ == '__main__':
  args = sys.argv
  del args[0]
  main(args)