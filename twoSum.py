
def twoSum(self, nums, target):
    seen_number = set()
    target = int(input)
    nums = [int(input)]
    for i in nums:
        complenent = target - i
        if complenent in seen_number:
            print(f'({nums[i]}, {complenent})' if i < complenent else f'({complenent},{i})')
    seen_number.add(i)

    

    