class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        # print(f"len of s is {s_len} and len of t is {t_len}")

        counter = max(s_len, t_len)

        s_registry = dict()
        t_registry = dict()

        for i in range(counter):
            # print(f"i is {i} and counter is {counter}")
            if i < s_len:
                s_value = s_registry.get(s[i], 0)
    
                if s_value:
                    # print(f"inside current value {value}")
                    s_registry.update({s[i]: s_value + 1})
                else:
                    s_registry.update({s[i]: 1})

            
            if i < t_len:
                # print(f"t[i] is {i}")
                t_value = t_registry.get(t[i], 0)
            
                if t_value:
                    # print(f"inside current value {value}")
                    t_registry.update({t[i]: t_value + 1})
                else:            
                    t_registry.update({t[i]: 1})
        
        return t_registry == s_registry
