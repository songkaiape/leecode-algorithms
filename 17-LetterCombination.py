
#Given a digit string, return all possible letter combinations that the number could represent.

#A mapping of digit to letters (just like on the telephone buttons) is given below.
#Input:Digit string "23"
#Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

class solution(object):
  #use while loop
  def letterCombinations(self,digits):
    mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    if len(digits)==0:
      return []
    result=list(mapping[digits[0]])
    while len(digits)>1:
      additional=list(mapping[digits[1]])
      result=[r+a for r in result for a in additional]
      digits=digits[1:]
    return result
  #recursive 
  def letterCombinations_v2(self,digits):
    mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    if len(digits)==0:
      return []
    if len(digits)==1:
      return list(mapping[digits[0]])
    prev=self.letterCombinations_v2(digits[:-1])
    additional=mapping[digits[-1]]
    return [s+c for s in prev for c in additional]
  
