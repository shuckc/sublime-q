from .aiokdb.aiokdb import KException


def format_mem(mem):
    if mem > 1000000000:
        return '{0:.2f}'.format(mem/1000000000) + 'GB'
    elif mem > 1000000:
        return '{0:.0f}'.format(mem/1000000) + 'MB'
    elif mem > 1000:
        return '{0:.0f}'.format(mem/1000) + 'KB'
    else:
        return '{0:.0f}'.format(mem) + 'B'

def decode(s):
  if type(s) is bytes:
      return s.decode('utf-8')
  elif type(s) is KException:
      return str(s)
  else:
      return str(s)
