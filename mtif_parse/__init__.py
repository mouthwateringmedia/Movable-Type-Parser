import codecs
import types

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
            
        else:
          entry.append(line)
          
      else:
        self.eof = True
        if entry:
          return self.parse_entry(entry)
          
        else:
          raise StopIteration
          
  def parse_entry (self, entry_list, multi=False, multi_key=None, allowed_keys=()):
    ret = {}
    multi_list = []
    cnt = 0
    
    for e in entry_list:
      if multi:
        if e == '-' * 5:
          if multi_key in ('COMMENT', 'PING'):
            if multi_key == 'COMMENT':
              akeys = ('AUTHOR', 'EMAIL', 'URL', 'IP', 'DATE')
              
            else:
              akeys = ('TITLE', 'URL', 'IP', 'BLOG NAME', 'DATE')
              
            mret = self.parse_entry(multi_list, multi_key='BODY', allowed_keys=akeys)
            self.listify(ret, multi_key, mret)
            
          else:
            self.listify(ret, multi_key, '\n'.join(multi_list))
            
          multi = False
            
        else:
          
          multi_list.append(e)
          if cnt + 1 >= len(entry_list):
            self.listify(ret, multi_key, '\n'.join(multi_list))
            
      else:
        elems = e.split(':', 1)
        key = elems[0]
        value = ''
        if not key or key == '-' * 5:
          continue
        
        elif allowed_keys and key not in allowed_keys:
          multi = True
          multi_list.append(e)
          if cnt + 1 >= len(entry_list):
            self.listify(ret, multi_key, '\n'.join(multi_list))
            
          cnt+= 1
          continue
        
        elif len(elems) > 1:
          value = elems[1].strip()
          
        if value:
          self.listify(ret, key, value)
            
        elif key in allowed_keys:
          pass
          
        elif key in ('AUTHOR', 'TITLE', 'BASENAME', 'DATE', 'PRIMARY CATEGORY',
                     'CATEGORY', 'TAGS', 'STATUS', 'ALLOW COMMENTS', 
                     'ALLOW PINGS', 'CONVERT BREAKS', 'NO ENTRY'
                     ):
          self.listify(ret, key, '')
          
        else:
          multi = True
          multi_list = []
          multi_key = key
          
      cnt+= 1
      
    return ret
    
  def listify (self, ret, key, value):
    if ret.has_key(key):
      if type(ret[key]) is types.ListType:
        ret[key].append(value)
        
      else:
        ret[key] = [ret[key], value]
        
      return None
      
    ret[key] = value
    