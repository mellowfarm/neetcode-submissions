class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        max = numbers[len(numbers)-1]

        def search(start, end, numbers, target):
            mid = (start+end)//2    

            if target == numbers[mid]:
                return mid
            elif start == end:
                return None
            elif target > numbers[mid]:
                return search(mid+1, end, numbers, target)
            else:
                return search(start, mid-1, numbers, target)

        for i in range(0, len(numbers)):
            if target - numbers[i] > max:
                continue
            else:
                res = search(i+1, len(numbers)-1, numbers, target - numbers[i])
                if res is None:
                    continue
                else:
                    return [i + 1, res + 1]
        
    
            
