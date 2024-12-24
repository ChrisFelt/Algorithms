class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # time complexity for this solution: 2n + n = O(n)
        # construct dictionaries for each word with number of times each letter appears
        s_count = self.count_char(s)
        t_count = self.count_char(t)

        # compare counts in place 
        # (converting to lists and comparing the lists would be O(n^2) since list append has a time complexity of O(n) in Python)
        for i in range(len(s)):
            # if count of char count for the string at i is not the same for s and t, they are not isomorphs
            if s_count[s[i]] != t_count[t[i]]:
                return False
        
        return True
        

    def count_char(self, a_string: str) -> dict:
        """Counts each character in a string and returns result as a dictionary"""

        # construct dictionary to count number of character occurences
        string_dict = {}
        for i in a_string:
            # add 1 to count if char exists
            if i in string_dict:
                string_dict[i] += 1
            
            # add new entry if char not in dictionary
            else:
                string_dict[i] = 1
        
        return string_dict
        
