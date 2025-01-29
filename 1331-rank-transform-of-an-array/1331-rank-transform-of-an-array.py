class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        unique_sorted = sorted(set(arr))
        rank_map = {num : rank + 1 for rank,num in enumerate(unique_sorted)}
        return [rank_map[num] for num in arr]