from collections import Counter


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # strings have different length --> impossible --> false;
        # strings are equal --> need one char with frequency >= 2

        # we need to keep number of positions on which s and goal are different
        # if 2 distinct --> check if we can swap

        if len(s) != len(goal):
            return False

        distinct = []
        for idx in range(len(s)):
            if s[idx] != goal[idx]:
                distinct.append(idx)
                if len(distinct) > 2:
                    return False

        if len(distinct) == 1:
            return False
        elif len(distinct) == 2:
            first, second = distinct
            return s[first] == goal[second] and s[second] == goal[first]
        else:
            c = Counter(goal)
            for _, val in c.items():
                if val >= 2:
                    return True

        return False


# TODO add main + basic tests
