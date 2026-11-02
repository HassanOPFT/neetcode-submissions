class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)

        if s_len != t_len:
            return False

        s = "".join(sorted(s))
        t = "".join(sorted(t))

        if s == t:
            return True
        else:
            return False