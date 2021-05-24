from bs4 import BeautifulSoup
import requests
import json
import sre_yield
from lib.article import Article
from lib.broker import SentenceBroker
from graphviz import Digraph

def switchArg(option, arg):
  if (option == '-r' or option == '--regex'):
    return generateTextsFromRegex(arg[0])
  if (option == '-l' or option == '--list'):
    return arg

def urls2rdf(args):
  # regex 표현식인지 먼저 filtering
  urls = switchArg(args[0], args[1:])
  
  triples = []
  for url in urls:
    print(url)
    triples.extend(generateTripleFromUrl(url))
  print(triples)

  rdf = generateRdfFromTriples(triples, urls[0])

  f = open('out/rdf.ttl', 'w')
  f.write(rdf)

  knowledgeGraph = generateKnowledgeGraphFromTriples(triples)\

"""
Desc: 
  정규포현식으로 표현된 데이터를 각 각의 text로 생성합니다.

Args:
  regex: 정규 표현식 형태의 데이터.

Returns:
  regex를 통해서 생성된 text map을 리턴합니다.
"""
def generateTextsFromRegex(regex):
  return sre_yield.AllStrings(regex)

"""
Desc: 
  URL을 입력받아 해당하는 site의 HTML 문서를 긁어옵니다.

Args:
  url: HTML url을 의미합니다.

Returns:
  HTML 문서
"""
def crawlHTMLFromUrl(url):
  try:
    article = Article(url)
    return article.html 
  except:
    return None

"""
Desc: 
  HTML 문서에서 triple을 추출합니다.

Args:
  html

Returns:
  HTML 문서에서 ul 또는 li 에 해당하는 트리플만 추출합니다.
"""
def extractTriplesFromHTML(html):
  sb = SentenceBroker(html)
  text = ''
  text += sb.getListText('ul') # get ul tag
  text += sb.getListText('ol') # get ol tag
  if not text:
    return ''

  api_url = 'http://localhost:8001/api/text2triple'

  headers = {'Content-Type': 'multipart/form-data; charset=utf-8'} 
  res = requests.post(api_url, files=[('text', text)], headers=headers)
  return res.json()
"""
Desc: 
  HTML 문서로 부터 text를 생성합니다.

Args:
  regex : 정규 표현식 형태의 데이터.

Returns:
  regex를 통해서 생성된 text map을 리턴합니다.
"""
def crawlTextFromUrl(url):
  try:
    article = Article(url)
    return article.text
  except:
    return None

"""
Desc: 
  Text로 부터 Triple을 추출합니다.

Args:
  text: 정규 표현식 형태의 데이터.

Returns:
  text로 부터 triple들을 추출합니다..
"""
def generateTriplesFromText(text):
  api_url = 'http://localhost:8001/api/text2triple'

  headers = {'Content-Type': 'multipart/form-data; charset=utf-8'} 
  res = requests.post(api_url, files=[('text', text)], headers=headers)
  return res.json()

"""
Desc: 
  URL로 부터 Triple 리스트를 추출합니다.

Args:
  url

Returns:
  생성된 triple 리스트를 출력합니다.
"""
def generateTripleFromUrl(url):
  triples = []

  # 1. html로부터 triple을 추출
  html = crawlHTMLFromUrl(url)
  if html != None:
    triples.extend(extractTriplesFromHTML(html))
  
  # 2. text로부터 triple을 추출
  text = crawlTextFromUrl(url)
  if text != None:
    triples.extend(generateTriplesFromText(text))
  return triples

"""
Desc: 
  단순 triple들을 이용하여, RDF를 생성합니다.

Args:
  triples: [['subject', 'predicate', 'object'], ...]

Returns:
  turtle 형태의 RDF
"""
def generateRdfFromTriples(triples, url):
  api_url = 'http://localhost:8001/api/triple2rdf'

  headers = {'Content-Type': 'multipart/form-data; charset=utf-8'} 
  
  tripleString = "["
  for i in triples:
    tripleString += "[\"" + "\",\"".join(i) + "\"]"
  tripleString += "]"

  res = requests.post(api_url, files=[('triple',tripleString), ('url', url)], headers=headers)
  
  return res.text

"""
Desc: 
  RDF를 기반으로 knowledge graph를 생성합니다.

Args:
  rdf: turtle 형태로 작성된 RDF

Returns:
  knowledge graph
"""
def generateKnowledgeGraphFromTriples(triples):
  prd = "predicate:"

  triples = list(map(lambda x: [x[0], prd+x[1], x[2]], triples))

  # 너무 많으면 그래프가 안 그려져서 100개씩 끊어서 저장
  triple100List = []
  cnt = 0
  hundred = []
  for ts in triples:
    if cnt < 100:
      hundred.append(ts)
      cnt += 1
    else:
      triple100List.append(hundred[:])
      hundred = []
      cnt = 0

  # 그래프 매핑
  num = 0
  sbjList = []
  for t100 in triple100List:
    f = Digraph('finite_state_machine', filename='out/kg/fsm.gv'+str(num), format='png')
    f.attr(rankdir='LR', size='300,300')
    for triple in t100:
      if url+triple[0] not in sbjList:
        sbjList.append(triple[0])
        f.attr('node', shape='doublecircle')
        f.node(triple[0])
        f.attr('node', shape='circle')
        f.edge(triple[0], triple[2], label=triple[1])
      else:
        f.attr('node', shape='circle')
        f.edge(triple[0], triple[2], label=triple[1])
    f.view()
    num += 1
