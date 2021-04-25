from functools import wraps
## Decorators
def alertenv(func):
  @wraps(func)
  def wrapper(warning = True, env = env):
    print('#################################################')
    print('You are connected to:')
    print(env)
    print('#################################################')
    if warning:
      print('ANDA CON CUIDADO!! ES ESCRITURA')
    func(warning, env)
  return wrapper
  

def trycatch(returnvalue = None, exceptionfunc = lambda: None, log = True):
  def _outer(func):
    @wraps(func)
    def _wrapper(*args, **kwargs):
      try:
        return func(*args, **kwargs)
      except Exception as e:
        if log: print(f"Error in {func.__name__} function\n{e}")
        exceptionfunc()
        return returnvalue
    return _wrapper
  return _outer