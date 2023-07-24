# https://leetcode.com/problems/sort-vowels-in-a-string/


class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = [x for x in s if x in "aeiouAEIOU"]
        sorted_vowels = list(sorted(vowels))

        t = ""
        vowel_idx = 0
        for x in s:
            if x in "aeiouAEIOU":
                t += sorted_vowels[vowel_idx]
                vowel_idx += 1
            else:
                t += x

        return t
