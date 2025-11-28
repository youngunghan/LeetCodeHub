from typing import List
from functools import lru_cache

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Use memoization to store results of sub-expressions to avoid redundant calculations.
        @lru_cache(maxsize=None)
        def compute(exp: str) -> List[int]:
            # Base case: if the expression contains only a number, return it as a list of integer.
            if exp.isdigit():
                return [int(exp)]
            # end if
            
            result: List[int] = []
            
            # Iterate through each character to find operators.
            for i, char in enumerate(exp):
                if char in '-+*':
                    # Divide the expression into left and right parts at the operator.
                    # Recursively compute all possible results for both parts.
                    left_results: List[int] = compute(exp[:i])
                    right_results: List[int] = compute(exp[i + 1:])
                    
                    # Combine every result from the left part with every result from the right part using the current operator.
                    for left_val in left_results:
                        for right_val in right_results:
                            if char == '+':
                                result.append(left_val + right_val)
                            elif char == '-':
                                result.append(left_val - right_val)
                            else:  # char == '*'
                                result.append(left_val * right_val)
                            # end if
                        # end for
                    # end for
                # end if
            # end for
            
            return result
        # end def
        
        return compute(expression)
    # end def
