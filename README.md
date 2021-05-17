# Generate RDF from URLs

### Description

url pattern을 regex로 입력받거나 리스트로 데이터를 입력받아 이를 rdf로 변환합니다.

### Requirement

python 3.9 를 기반으로 합니다.
기타 요구 사항은 requirement.txt에 담겨있습니다.

- 설치

```bash
$ pip install -r requirements.txt
```

### Run

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
