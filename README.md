Movable-Type-Parser
===================

Library for parsing Movable type export text files.


Usage
-----

```python
import mtif_parse

fh = open('path/to/som/file.txt', 'r')

for entry in mtif_parse.MTIF(fh):
  do something with entry ...
  
```

Notes
-----

1. MTIF will also accept string data.
2. MTIF is an iterator class so that you process a big file without using a lot of memory up.
