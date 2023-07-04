from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # See discussion in cpp solution

        # we can count bits... i.e. if a number appears 3 times --> it's bits
        # are set a multiple of 3 times.
        # for the number that appears only once, the bits are set M3 + 1 times.

        # surprise: python has a weird way to handle numbers.

        # not used; the bit masks behave a bit different in python
        def does_not_work() -> int:
            res = 0
            positive = None

            for bit in range(31):
                counts_pos, counts_neg = 0, 0

                mask = 2**bit
                for num in nums:
                    if num > 0:
                        if mask == (num & mask):
                            counts_pos += 1
                    else:
                        if mask == (abs(num) & mask):
                            counts_neg += 1
                if counts_pos % 3 == 1:
                    res = res | mask
                    positive = True
                elif counts_neg % 3 == 1:
                    res = res | mask
                    positive = False

            return res if positive else -res

        INT_BASE = 33  # because of INT32_MIN
        # give python what it likes
        counts_nz = [0 for _ in range(INT_BASE)]
        vals_bit = ["0" for _ in range(INT_BASE)]

        for num in nums:
            # 33 because of INT32_MIN takes 33 bits to represent.
            bin_rep = f"{num:033b}"
            for idx, bin_val in enumerate(bin_rep):
                if bin_val != "0":
                    counts_nz[idx] += 1
                    vals_bit[idx] = bin_val

        bin_res = "".join(
            [
                vals_bit[idx] if count % 3 == 1 else "0"
                for idx, count in enumerate(counts_nz)
            ]
        )
        return int(bin_res, 2)


# TODO: add main + interesting test cases (e.g. INT32_MIN)
