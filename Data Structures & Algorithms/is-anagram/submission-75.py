class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)

        if s_len != t_len:
            return False

        print("Before")
        print(f"s: {s} - t: {t}")

        s = "".join(sorted(s))
        t = "".join(sorted(t))

        print("After")
        print(f"s: {s} - t: {t}")

        if s == t:
            return True
        else:
            return False

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
        
#         return sorted(s) == sorted(t)