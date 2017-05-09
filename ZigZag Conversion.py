class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        pointer_list  = [2*(numRows-1)*i for i in range(len(s)/numRows)]
        ans=s[::2*(numRows-1)]
        for i in range(1,numRows):
            for pointer in pointer_list:
                if (pointer-i) > 0 :
                    if (i!=numRows-1):
                        ans+=s[(pointer-i)]
                if (pointer + i) < len(s):
                    ans+=s[(pointer+i)]
        return ans
