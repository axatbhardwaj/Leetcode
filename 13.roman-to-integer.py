#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self,s: str) -> int:
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        result = 0
        prev_value = 0  

        for i in range(len(s)):
            current_value = roman_map[s[i]]

            if current_value > prev_value:  
                result += current_value - 2 * prev_value 
            else:
                result += current_value

            prev_value = current_value  

        return result


        
# @lc code=end

