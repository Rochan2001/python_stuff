'''
Given two arrays of integers nums and index. Your task is to create target array under the following rules:

Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array.

It is guaranteed that the insertion operations will be valid.

 
input =0 1 2 3 4
0 1 2 2 1
output =0 4 1 3 2

Explanation:
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]



input = 1 2 3 4 0
0 1 2 3 0
output =0 1 2 3 4

Explanation:
nums       index     target
1            0        [1]
2            1        [1,2]
3            2        [1,2,3]
4            3        [1,2,3,4]
0            0        [0,1,2,3,4]


input =1
0
output =1

 nums   index
  1        0 


output  [1]
 

Constraints:

1 <= nums.length, index.length <= 100
nums.length == index.length
0 <= nums[i] <= 100
0 <= index[i] <= i
'''


def target(nums, index):
    t = []
    for index, value in zip(nums, index):
        t.insert(value, index)
    return t


nums = [int(x) for x in input().split()]
index = [int(x) for x in input().split()]
res = target(nums, index)
print(*res)
