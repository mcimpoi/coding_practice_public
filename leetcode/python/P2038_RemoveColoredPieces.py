# https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        # turns don't matter, only the length of continuous
        # sequences of A and B
        # count the current length of A and B;
        # add to numA / numB this length -2 --> because
        # neither alice nor bob can remove the edges
        # AAAAAABABBA --> AXXXXABABBA
        # if numA > numB -> Alice can win
        def countClusters(colors: str) -> bool:
            idx, numA, numB = 0, 0, 0
            while idx < len(colors):
                crtA, crtB = 0, 0
                while idx < len(colors) and colors[idx] == "A":
                    crtA += 1
                    idx += 1
                while idx < len(colors) and colors[idx] == "B":
                    crtB += 1
                    idx += 1
                numA += max(0, crtA - 2)
                numB += max(0, crtB - 2)
            return numA > numB

        def countAsWeGo(colors: str) -> bool:
            numA, numB = 0, 0
            print(colors[1:-1])
            for idx, ch in enumerate(colors[1:-1]):
                # idx is 0, 1... len(colors - 2)
                if ch == colors[idx] and ch == colors[idx + 2]:
                    if ch == "A":
                        numA += 1
                    else:
                        print(idx, ch, numB)
                        numB += 1
            print(numA, numB)
            return numA > numB

        return countAsWeGo(colors)


if __name__ == "__main__":
    s = Solution()
    colors = "AAABABB"
    print(f"input: {colors} Expected: {1} Actual: {s.winnerOfGame(colors)}")
