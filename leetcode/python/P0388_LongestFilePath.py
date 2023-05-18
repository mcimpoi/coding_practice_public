# https://leetcode.com/problems/longest-absolute-file-path/


class Solution(object):
    def lengthLongestPath(self, input_path: str) -> int:
        is_file = False
        max_length, crt_filename_length, crt_level = 0, 0, 0
        lengths = {}
        filename = ""

        for ch in input_path + "\n":
            if ch.isalnum() or ch == ".":
                crt_filename_length += 1
                filename += ch
            if ch == ".":
                is_file = True
            if ch == "\n":
                if is_file:
                    total_length = crt_filename_length
                    for level in range(crt_level):
                        # one for slash
                        total_length += lengths[level] + 1
                    max_length = max(total_length, max_length)
                else:
                    lengths[crt_level] = crt_filename_length
                crt_level = 0
                is_file = False
                crt_filename_length = 0
                filename = ""
            if ch == "\t":
                crt_level += 1

        return max_length


if __name__ == "__main__":
    a = Solution()
    print(
        a.lengthLongestPath(
            "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
        )
    )
