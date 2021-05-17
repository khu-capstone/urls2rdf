from bs4 import BeautifulSoup
import requests
import sre_yield

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
   return requests.get(url).text 
  except:
    return None

"""
Desc: 
  HTML 문서에서 triple을 추출합니다.

Args:
  html

Returns:
  전처리를 수행한 HTML문서를 리턴합니다.
"""
def extractTriplesFromHTML(html):
  # TODO: 구현
  return html

"""
Desc: 
  HTML 문서로 부터 text를 생성합니다.

Args:
  regex : 정규 표현식 형태의 데이터.

Returns:
  regex를 통해서 생성된 text map을 리턴합니다.
"""
def generateTextFromHTML(html):
  soup = BeautifulSoup(html)
  script_tag = soup.find_all(['script', 'style', 'header', 'footer', 'form'])

  for script in script_tag:
    script.extract()
  content = soup.get_text('\n', strip=True)
  return content

"""
Desc: 
  Text로 부터 Triple을 추출합니다.

Args:
  text: 정규 표현식 형태의 데이터.

Returns:
  text로 부터 triple들을 추출합니다..
"""
def extractTriplesFromText(text):
  # TODO: 구현
  return text

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

  html = crawlHTMLFromUrl(url)
  if html != None:
    # 1. html로부터 triple을 추출
    trples.append(extractTriplesFromHTML(html))

    # 2. text로부터 triple을 추출
    text = generateTextFromHTML(html)
    prtmtText = preprocessText(text)
    triples.append(extractTriplesFromText(prtmtText))
  return triples

"""
Desc: 
  단순 triple들을 이용하여, RDF를 생성합니다.

Args:
  triples: [['subject', 'predicate', 'object'], ...]

Returns:
  turtle 형태의 RDF
"""
def generateRdfFromTriples(triples):
  # TODO: 구현
  return triples


"""
Desc: 
  RDF를 기반으로 knowledge graph를 생성합니다.

Args:
  rdf: turtle 형태로 작성된 RDF

Returns:
  knowledge graph
"""
def generateKnowledgeGraphFromRdf(rdf):
  # TODO: 구현
  return rdf
