Movable-Type-Parser
===================

Library for parsing Movable type export text files.


##Usage##

```python
import mtif_parse

fh = open('path/to/some/file.txt', 'r')

for entry in mtif_parse.MTIF(fh):
  do something with entry ...
  
```

##Notes##

1. MTIF will also accept string data.
2. MTIF is an iterator class so that you process a big file with a small memory footprint.


##Example entry##
```python
{
  'ALLOW COMMENTS': '1',
  'ALLOW PINGS': '0',
  'AUTHOR': 'cvilletomorrow',
  'BASENAME': 'chloramines',
  'BODY': 'HTML Content......',
  'CATEGORY': ['Albemarle County', 'Charlottesville', 'Chloramines', 'Daily Progress Partnership', 'Water Supply'],
  'COMMENT': [
    {
      'AUTHOR': 'John Doe',
      'BODY': 'Comment content......',
      'DATE': '06/18/2012 12:42:23 AM',
      'EMAIL': 'nobody@example.com',
      'IP': '174.63.92.164',
      'URL': 'http://www.example.com/narf.html'
    },
    
    #...... Addition Comments
  ],
  
  'CONVERT BREAKS': 'wysiwyg',
  'DATE': '06/18/2012 12:01:00 AM',
  'EXCERPT': 'Excerpt content.......',
  'EXTENDED BODY': 'Extended body ......',
  'KEYWORDS': '',
  'STATUS': 'Publish',
  'TITLE': 'Water authority and activists preparing for chloramines information session'
}
```

Additional info on the format and possible data that may be parsed can be found at http://www.movabletype.org/documentation/appendices/import-export-format.html
