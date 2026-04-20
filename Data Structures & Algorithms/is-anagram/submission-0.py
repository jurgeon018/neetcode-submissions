class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_counter = {}
        t_counter = {}
        for char in s:
            if char not in s_counter:
                s_counter[char] = 0

            s_counter[char] += 1

        for char in t:
            if char not in t_counter:
                t_counter[char] = 0

            t_counter[char] += 1
        
        for k, s_value in s_counter.items():
            t_value = t_counter.get(k)
            if not t_value:
                return False
            if s_value != t_value:
                return False
        return True
