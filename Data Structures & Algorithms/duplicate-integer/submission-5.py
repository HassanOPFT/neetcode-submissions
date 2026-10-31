class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        registry = dict()

        for n in nums:
            # exist add +1
            if(registry.get(n, 0)):
                print(f"value {n} exists, adding 1 to it")
                registry.update({n : registry[n] + 1})
                continue
            
            # doesn't exist add to dict
            registry.update({n : 1});

        for c in registry.values():
            if(c > 1):
                print(f"found duplicate, existing with True")
                return True

        return False
        