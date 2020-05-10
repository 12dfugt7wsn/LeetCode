def findMedianSortedArrays(A,B) -> float:
    m, n = len(A),len(B)

    if n<m:
        A, B, m, n = B, A, n, m

    imin, imax, halfLen = 0, m, (m+n+1)/2
    while(imin <= imax):
        i = int((imin+imax)/2)
        j = int(halfLen)-i
        if i > 0 and A[i-1] > B[j]:
            imax = i - 1
        elif i < m and A[i] < B[j-1]:
            imin = i + 1
        else:
            # i is perfect
            if i==0:
                maxLeft = B[j-1]
            elif j==0:
                maxLeft = A[i-1]
            else:
                maxLeft = max(A[i-1], B[j-1])

            if (m+n) % 2 == 1:
                return maxLeft
            else:
                if i==m:
                    minRight = B[j]
                elif j==n:
                    minRight = A[i]
                else:
                    minRight = min(B[j],A[i])
            return (maxLeft+minRight)/2



def longestPalindrome(self, s: str) -> str:
    result = ''
    for i in range(0,len(s)):
        j = i + 1
        while j<= len(s) and len(result) <= len(s[i:]):
            if s[i:j] == s[j:i][::-1] and len(s[i:j]) > len(res):
                res = s[i:j]
            j += 1
    return result

def zigzag(s: str, numRows: int):
    lin = 0
    pl = 1
    outp = [""] * numRows
    for i in range(len(s)):
        outp[lin] += s[i]
        if numRows > 1:
            lin += pl
            if lin == 0 or lin == numRows -1:
                pl *= -1
    print(outp)
    outputStr = ""
    for j in range(numRows):
        outputStr += outp[j]
    return outputStr

print(zigzag('qwertyasdfg',4))