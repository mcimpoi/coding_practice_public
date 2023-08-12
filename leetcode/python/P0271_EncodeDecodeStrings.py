# https://leetcode.com/problems/encode-and-decode-strings

from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        prefix = ",".join([str(len(s)) for s in strs])
        return prefix + ";;" + "".join(strs)

    def decode(self, encoded: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        prefix = encoded.split(";;")[0]
        rest = encoded[len(prefix) + 2 :]

        lengths = [int(x) for x in prefix.split(",")]
        res = []
        total_len = 0

        for crt_len in lengths:
            res.append(rest[total_len : total_len + crt_len])
            total_len += crt_len
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
