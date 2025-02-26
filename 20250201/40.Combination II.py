# ✅ Approach (코딩하기 전 10분 동안 작성)

### 1. Edge cases

empty candidates

### 2. Brainstorm

backtracking

### 3. Plan

- create list
- sort the candidates
- backtracking
    - If `totalLeft` is less than 0, return immediately (invalid path).
    - If `totalLeft` equals 0:
        - Add a copy of `tempList` to `answer` (valid combination found).
    - 
    - Otherwise:
        - Iterate over `candidates` starting from `index`:
            - Skip duplicate numbers by checking if `candidates[i] == candidates[i - 1]` for `i > index`.
            - Add `candidates[i]` to `tempList`.
            - Recursively call `backtrack` with:
                - Updated `totalLeft` reduced by `candidates[i]`.
                - Updated `index` as `i + 1` to avoid reusing the same element.
            - Remove the last element from `tempList` to backtrack and explore other possibilities.
    - Return `list` containing all unique combinations after the recursive calls complete.

### 4. TC & SC (이유도 함께 작성)

- TC :O(2^N)
- SC : O(N)

# ✅ Github URL

: 

```python
class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        n = len(candidates)
        ans = []

        def backtrack(idx, curr_sum, elem):
            if curr_sum == target:
                ans.append(elem[:])
                return
            
            if idx == n or curr_sum > target:
                return
            
            elem.append(candidates[idx])
            backtrack(idx + 1, curr_sum + candidates[idx], elem)
            elem.pop()
            # skipping the duplicates
            while idx + 1 < n and candidates[idx] == candidates[idx+1]:
                idx += 1
            backtrack(idx + 1, curr_sum, elem)
        backtrack(0, 0, [])
        return ans
```

# ✅ 문제 분석

### 1. 문제에서 구해야 하는 것

Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`.

### 2. 다른 풀이

```java
class Solution:
    def __init__(self):
        self.result = []  # Resultant list to store combinations

    # Recursive function to find combinations
    def solve(self, nums, target, index, lst):
        # Base case: if target is achieved
        if target == 0:
            self.result.append(lst[:])  # Add current combination to result
            return

        # Base case: if index exceeds array bounds or target is less than current element
        if index == len(nums) or target < nums[index]:
            return

        temp = nums[index]
        lst.append(nums[index])  # Choose current element
        self.solve(nums, target - nums[index], index + 1, lst)  # Recur with reduced target and move to next index
        lst.pop()  # Backtrack: remove last element

        i = 1
        while index + i < len(nums) and nums[index + i] == temp:
            i += 1  # Skip duplicates
        self.solve(nums, target, index + i, lst)  # Recur without choosing current element

    # Main function to find combination sum
    def combinationSum2(self, candidates, target):
        candidates.sort()  # Sort candidates array
        self.solve(candidates, target, 0, [])  # Call recursive function
        return self.result  # Return result
```

### 3. 틀린 이유

ex) 접근방식이 틀림, 시간초과, 메모리초과 

### 4. 느낀점 or 기억할정보