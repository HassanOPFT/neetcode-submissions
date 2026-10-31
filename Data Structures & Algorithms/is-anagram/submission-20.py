class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        val_len = len(s)
        print(val_len)
        s_registry = dict()
        t_registry = dict()

        for i in s:
            value = s_registry.get(i, 0)
            # print(f"current value {value} for key {i}")

            if value:
                # print(f"inside current value {value}")
                s_registry.update({i: value + 1})
                continue
            
            s_registry.update({i: 1})
        
        for i in t:
            value = t_registry.get(i, 0)
            # print(f"current value {value} for key {i}")

            if value:
                # print(f"inside current value {value}")
                t_registry.update({i: value + 1})
                continue
            
            t_registry.update({i: 1})

        return t_registry == s_registry
