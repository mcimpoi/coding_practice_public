class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        # we need to maximize value at index (0 <= index < n)
        # while keeping the sum of elements in array less than maxsum;
        #
        # numbers in array are positive integers (i.e. >= 1)
        # we can increment and decrement by 1 or keep the same value (since we need to keep the sum <= maxsum,
        # doesn't make sense to keep the same value)
        #
        # first idea: we can fix a value at index, and while the sum of elements in array
        # is greater than maxsum --> keep decrementing nums[idx] and re-generate array.
        # complexity: time: O(n^2) -- n possible values * n length of array; space: O(n)
        #
        # improvement 1: we can compute the sum, instead of re-generating array
        # improvement 2: binary search for the maximum value at index (from 0 to max sum)

        # improvement 3: closed form solution might be possible (i.e. O(1) time, TODO: revisit the idea)

        # max_n = 1e9 --> nlogn not sufficient ==> compute sum in O(1); search for max in log(n) --> log(n) time complexity

        # n = 7 maxsum = 5 idx = 0
        # n-1 n-2 4  ?  ? --> 6 --> ok

        # 0, 1, 2, .. index --> index + 1 values; index values before index;
        # index + 1 ... n - 1 --> n - index - 1 values remaining.

        # n == 7
        # index = 3
        # ? ? ? 11 ? ? ? --> last value == 6 - 3 --> max(0, max_val - (n - index - 1))
        # max(0, (max_val - index))

        # we don't need to store array; just compute the sum
        # for a given max value, the array would look like:
        # [1, 1, 1, ... 1, 2, 3, ... max_val, max_val - 1, ... 1]
        # or [left_val, left_val + 1, ... max_val, max_val - 1, ... righ_val + 1, right_val]

        # to avoid counting the number of 1s padding the aray to the left and right, subtract 1 from all elems
        # and n from max_sum;

        # now we search for max_val - 1 in the new array

        def getSum(value: int) -> int:
            # find the first value in array that is not 0;
            left_val = max(1, value - index)
            # sum of elements from left_val to max_val candidate.
            # sum of range a, a + 1, ... b == (a + b) * (b - a + 1) // 2
            left_sum = (left_val + value) * (value - left_val + 1) // 2

            # similar idea for right
            right_val = max(1, value - (n - 1 - index))
            right_sum = (value + right_val) * (value - right_val + 1) // 2

            # note: we added value twice.
            return left_sum + right_sum - value

        # make the array look like:
        #   0, 0, ....,1, 2...max_val, max_val - 1, ... 1, 0, 0 (*or left/right values)
        maxSum -= n
        left, right = 0, maxSum

        while left < right:
            mid = (left + right + 1) // 2
            if getSum(mid) <= maxSum:
                left = mid
            else:
                right = mid - 1

        # because we subtracted 1 from everything
        return left + 1


if __name__ == "__main__":
    solution = Solution()
    for testcase, expected in (
        ([8257285, 4828516, 850015631], 29014),
        ([4, 2, 6], 2),
    ):
        print(
            f"Testcase:\n{testcase}\nExpected: {expected}\nResult: {solution.maxValue(*testcase)}\n"
        )
