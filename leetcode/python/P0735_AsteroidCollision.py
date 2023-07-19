# https://leetcode.com/problems/asteroid-collision/

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # when two asteroids of different signs are next to each other,
        # one or both explode.
        # we can put them in a queue (to keep order, i.e. vs stack)
        # when the signs differ --> explode (pop from queue, add remaining)

        # pay attention to:
        # - element in queue < 0; crt_elem > 0 --> doesn't collide
        # - when popping from queue, need variable to store the remaining asteroid
        # - stack (list) works as well; we don't need deque

        q = []

        for a in asteroids:
            if len(q) == 0:
                q.append(a)
            else:
                if len(q) > 0 and q[-1] * a > 0:
                    q.append(a)
                else:
                    crt = a
                    while len(q) > 0 and q[-1] > 0 and crt < 0:
                        prev_ = q.pop()
                        if abs(prev_) > abs(crt):
                            crt = prev_
                        elif abs(prev_) == abs(crt):
                            crt = 0

                    if crt != 0:
                        q.append(crt)

        return q
