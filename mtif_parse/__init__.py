import codecs
try:
  from cStringIO import StringIO
  
except:
  from StringIO import StringIO
  
class MTIF (object):
  def __init__ (self, stuff):
    if hasattr(stuff, 'readline'):
      self.fobj = stuff
      
    else:
      self.fobj = StringIO(stuff)
      
    self.eof = False
    self.current = 0
    
  def __iter__ (self):
    return self
    
  def next (self):
    entry = []
    
    if self.eof:
      raise StopIteration
      
    while 1:
      line = self.fobj.readline()
      if line:
        line = line.strip().lstrip(codecs.BOM_UTF8)
        if line == '-' * 8:
          if entry:
            return self.parse_entry(entry)
            
          else:
            entry = []
            
        elif line:
          entry.append(line)
          
      else:
        self.eof = True
        if entry:
          return self.parse_entry(entry)
          
        else:
          raise StopIteration
          
  def self.parse_entry (entry_list):
    return entry_list[0]
    