
"""
QUINE-MCKLUSKEY MINIMIZER OF BOOLEAN FUNCTIONS

MAY 26, 2020

"""

from converter import get_function


class QM_Minimizer:

  def __init__(self, min_terms, N):

    
    self.min_terms = sorted([int(x) for x in min_terms.split(",")]) #initialize minterm from given function
    self.no_of_variables = N  #set maximum number of variables in function
    self.s1_implicants = [] #to store size 2 implicants
    self.s2_implicants = [] #to store size 4 implicants
    self.prime_implicants = []  #to store prime implicants


  #Converts a given minterm integer into binary format with length of no of variables
  def to_binary(self, n):
    N = self.no_of_variables
    bin_string = ""
    while n != 0:
      rem = n % 2
      n = n // 2
      bin_string += str(rem)

    bin_string = bin_string[::-1]

    L = len(bin_string)
    if L < N:
      bin_string = "0" * (N - L) + bin_string

    return bin_string


  def generate_column_1(self):
    bin_column = []
    no_of_terms = len(self.min_terms)

    for i in range(self.no_of_variables + 1):
      for _m in self.min_terms:

        bin_eq = self.to_binary(_m)
        if (bin_eq.count("1") == i):
          bin_column.append((_m, bin_eq))

    return bin_column


  def position_of(self, string, key):
    pos = []
    for k in range(len(string)):
      if string[k] == key:
        pos.append(k)
    
    return pos

  def is_next_gray(self, bin_1, bin_2):
    bit = "1"
    changed_bit_pos = ""
    for k in range(len(bin_1)):
      if (bin_1[k] == bit and bin_2[k] != bit):
        return (False, -1)

      if bin_1[k] != bit and bin_2[k] == bit:
        changed_bit_pos += str(k)

    if bin_1.count(bit) + 1 == bin_2.count(bit):
      return (True, changed_bit_pos)

    return (False, -1)  


  def replace_all(self, string, x, y):
    return y.join(string.split(x))

  def replace_pos(self, string, p, y):
    x = list(string)
    x[p] = y
    return "".join(x)
    

  def generate_column_2(self):
    self.s1_implicants = self.generate_column_1()

    for x in range(len(self.s1_implicants) - 1):
      for y in range(x + 1, len(self.s1_implicants)):

        imp_1 = self.s1_implicants[x]
        imp_2 = self.s1_implicants[y]

        gray_result = self.is_next_gray(imp_1[1], imp_2[1])

        if gray_result[0]:

          changed_pos = gray_result[1]

          bit_str = self.replace_pos(imp_1[1], int(changed_pos), "_")

          self.s2_implicants.append([(imp_1[0], imp_2[0]), bit_str])

    self.update_prime_implicants(self.s2_implicants)

    return self.s2_implicants


  def same_changed_pos(self, bit_str_1, bit_str_2):
    first_pos = bit_str_1.index("_")
    
    for k in range(len(bit_str_1)):
      if bit_str_1[k] == "_" and bit_str_2[k] != "_":
        return (False, first_pos)

    return (True, first_pos)


  def update_prime_implicants(self, current_column):

    for x in range(len(current_column)):
      c_imp_1 = current_column[x]
      is_match = False
      for y in range(len(current_column)):
        c_imp_2 = current_column[y]

        if x != y:

          is_match = self.same_changed_pos(c_imp_1[1], c_imp_2[1])

          if is_match[0]:
            break
      
      if not is_match[0]:
        if c_imp_1 not in self.prime_implicants:
          self.prime_implicants.append(c_imp_1)

   
    return self.prime_implicants
          
          
          

  def get_next_column_and_results(self, current_column, _last_reached):

    if _last_reached:
      return self.prime_implicants

    is_last_column = False
    next_column = []

    for x in range(len(current_column) - 1):
      for y in range(x + 1, len(current_column)):

        c_imp_1 = current_column[x]
        c_imp_2 = current_column[y]

        bit_compare_result = self.same_changed_pos(c_imp_1[1], c_imp_2[1])
        fp = bit_compare_result[1]
        changed_bit = self.is_next_gray(c_imp_1[1][:fp], c_imp_2[1][:fp])

        if bit_compare_result[0] and changed_bit[0]:

          # last_pos = len(c_imp_1[1]) - 1 - c_imp_1[1][::-1].index("_")

          if c_imp_1[1][fp + 1:] == c_imp_2[1][fp + 1:]:
            terms = c_imp_1[0] + c_imp_2[0]
            bit_str = self.replace_pos(c_imp_1[1], int(changed_bit[1]), "_")
            next_column.append([terms, bit_str])

    self.update_prime_implicants(current_column)
    
    if len(next_column) == 0:
      is_last_column = True
    
    #recursively generate new columns
    return self.get_next_column_and_results(next_column, is_last_column)




  def minimize(self):
    prime_imps = self.get_next_column_and_results(self.generate_column_2(), False)

    return get_function(prime_imps, self.no_of_variables)

  


  

  
