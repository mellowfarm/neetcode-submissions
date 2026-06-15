class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = 0
        for pile in piles:
            max_pile = max(max_pile, pile)
        
        start = 1
        end = max_pile
        curr_min = float('inf')
        while True: 
            mid = int((end+start)/2)
            num_hours = 0
            if start > end or mid <= 0:
                break
            for pile in piles:
                num_hours += math.ceil(pile/mid)
            if num_hours > h:
                start = mid + 1
            else:
                curr_min = min(curr_min, mid)
                end = mid - 1

        return curr_min


                    

    