# class Solution(object):
#     def letterCombinations(self, digits):
#         """
#         :type digits: str
#         :rtype: List[str]
#         """
# dmap = {'2': 'abc',
#         '3': 'def',
#         '4': 'ghi',
#         '5': 'jkl',
#         '6': 'mno',
#         '7': 'pqrs',
#         '8': 'tuv',
#         '9': 'wxyz',
#         '0': ' ',
#         None: None}

# class Solution(object):
#     def letterCombinations(self, digits):
#         # DFS
#         result = []
#         ls = len(digits)
#         if ls == 0:
#             return result
#         current = digits[0]
#         posfix = self.letterCombinations(digits[1:])
#         for t in dmap[current]:
#             if len(posfix) > 0:
#                 for p in posfix:
#                     temp = t + p
#                     result.append(temp)
#             else:
#                 result.append(t)
#         return result


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        import itertools
        if not digits: return []
        dicti = {"2":["a","b","c"],
                "3": ["d","e","f"],
                "4": ["g","h","i"],
                "5": ["j","k","l"],
                "6":["m","o","n"],
                "7":["p","q","r","s"],
                "8":["t","u","v"],
                "9":["w","z","y","x"]}
        return [ ''.join(i) for i in itertools.product(*[dicti[n] for n in digits])]
