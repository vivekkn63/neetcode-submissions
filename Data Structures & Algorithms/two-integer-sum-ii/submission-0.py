class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        firstPointer, secondPointer = 0, len(numbers)-1
        final_list = []
        while firstPointer < secondPointer:
            total = numbers[firstPointer] + numbers[secondPointer]
            if total == target:
                final_list.append(firstPointer+1)
                final_list.append(secondPointer+1)
                break
            else:
                if total > target:
                    secondPointer-=1
                else:
                    firstPointer+=1
        return final_list
        