
## A toolkit for natural language processing

### Installation

```shell script
pip install sonlp
```

### Automatic Abbreviation for Text

#### **Usage** 

* Method 1 (Python API)

```python
from sonlp import abbr
abbr.get_abbreviation(query='China Central Television')
abbr.get_fullname(query='CCTV')
```

* Method 2 (Command Line)

```shell script
abbr China Central Television
abbr -i CCTV
```

