class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)

        if s_len != t_len:
            return False
        


        s = "".join(sorted(s))
        t = "".join(sorted(t))

        print(f"s sorted {s} and t sorted {t}")

        if s == t:
            return True
        else:
            return False

        counter = max(s_len, t_len)

        registry = dict()

        for i in range(counter):
            if i < s_len:
                s_value = registry.get(s[i])
    
                if s_value != None:
                    registry.update({s[i]: s_value - 1})
                else:
                    registry.update({s[i]: 1})
            
            if i < t_len:
                t_value = registry.get(t[i])
            
                if t_value != None:
                    # print(f"inside current value {value}")
                    registry.update({t[i]: t_value - 1})
                else:            
                    registry.update({t[i]: 1})
        
        for i in registry.values():
            if i > 0:
                return False
        
        return True
