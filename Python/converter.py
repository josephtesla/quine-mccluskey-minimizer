"""
Converts prime implicants into final minimized function
"""

def get_term(_bit_string):

  _ascii = 97

  term = ""
  for x in range(len(_bit_string)):
    ch = chr(_ascii + x)
    if _bit_string[x] != '_':
      term = term + ch if _bit_string[x] == '1' else term + ch + "'"

  return term.upper()


def get_function(prime_implicants, no_of_variables):

  bit_strings = list(map(lambda x: x[1], prime_implicants))

  func = " + ".join([get_term(x) for x in bit_strings])
  
  return func




  