class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        combined_number = int("".join(map(str,digits)))
        new_combined_number = combined_number + 1
        result = list(map(int,str(new_combined_number)))
        return result