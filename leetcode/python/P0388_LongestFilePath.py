class Solution(object):
    def lengthLongestPath(self, _input):
        """
        :type input: str
        :rtype: int
        """
        _input += '\n'
        crt_level = 0
        is_file = False
        max_length = 0
        crt_filename_length = 0
        lengths = {}
        filename = ''
        for ii, ch in enumerate(_input):
            if ch.isalnum() or ch == '.':
                crt_filename_length += 1
                filename += ch
            if ch == '.':
                is_file = True
            if ch == '\n':
                if is_file:
                    total_length = crt_filename_length;
                    for level in range(crt_level):
                        # one for slash
                        total_length += (lengths[level] + 1)
                    if total_length > max_length:
                        max_length = total_length
                        print(filename)
                else:
                    lengths[crt_level] = crt_filename_length 
                crt_level = 0
                is_file = False
                crt_filename_length = 0
                filename = ''
            if ch == '\t':
                crt_level += 1
                
        return max_length

if __name__ == "__main__":
    a = Solution()
    res = a.lengthLongestPath(
        "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")
    print(res)
