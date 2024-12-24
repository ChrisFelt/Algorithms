class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Time complexity of this solution: O(n)
        # use dictionary to track whether the same chars were at the same indices or not
        s_dict = {}
        t_dict = {}
        
        # iterate over both strings simultaneously
        for i in range(len(s)):
            # add character to the dictionary if it does not yet exist
            # hash map lookup time complexity in Python: average case O(1), worst case O(n)
            if s[i] not in s_dict:
                s_dict[s[i]] = i
            if t[i] not in t_dict:
                t_dict[t[i]] = i
            
            # characters should always appear at the same index across strings
            # if character already exists in the dictionary but has a different index, then the strings are not isomorphs
            if s_dict[s[i]] != t_dict[t[i]]:
                return False
        
        return True
        
        
