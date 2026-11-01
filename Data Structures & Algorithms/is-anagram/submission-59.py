class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        
        if s_len != t_len:
            return False

        counter = max(s_len, t_len)

        s_dict = dict()
        t_dict = dict()

        for i in range(counter):
            if i < s_len:
                s_value = s_dict.get(s[i])
    
                if s_value != None:
                    s_dict.update({s[i]: s_value + 1})
                else:
                    s_dict.update({s[i]: 1})
            
            if i < t_len:
                t_value = t_dict.get(t[i])
            
                if t_value != None:
                    # print(f"inside current value {value}")
                    t_dict.update({t[i]: t_value + 1})
                else:            
                    t_dict.update({t[i]: 1})
        
        return t_dict == s_dict
