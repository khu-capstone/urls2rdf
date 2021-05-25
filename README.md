# Generate RDF from URLs

### Description

url pattern을 regex로 입력받거나 리스트로 데이터를 입력받아 이를 rdf로 변환합니다.

1. regex url를 url list로 변경합니다.
2. 각 url의 html 문서를 불러옵니다.
3. html 문서에서 li, ul tag에서 의미를 추출하여 triple을 생성합니다.
4. html의 text를 추출하여, 이 안에서 의미를 추출합니다.
5. 추출한 triple을 이용하여 RDF를 생성합니다.
6. RDF를 기반으로 하여 Knowledge Graph를 생성합니다.


### Requirement

python 3.9 를 기반으로 합니다.
기타 요구 사항은 requirement.txt에 담겨있습니다.

- 설치

```bash
$ pip install -r requirements.txt
```

### CMD Run

```bash
$ python3 main.py [option] [pattern]
```

- option

  - -r, --regex : input이 regex pattern임을 알립니다.
  - -l, --list : input이 list임을 알립니다.


- example

```bash
$ python3 main.py -r https://en\.wikipedia\.org/wiki/[A-C]

$ python3 main.py -l https://en.wikipedia.org/wiki/A https://en.wikipedia.org/wiki/B https://en.wikipedia.org/wiki/C
```

### Server Run

<div align="center">
  <img width="1747" alt="스크린샷 2021-05-25 오후 4 19 33" src="https://user-images.githubusercontent.com/48043626/119456026-31d81480-bd75-11eb-8b0a-5ab3262f3c25.png">
</div>

```bash
$ python server/index.py
```
