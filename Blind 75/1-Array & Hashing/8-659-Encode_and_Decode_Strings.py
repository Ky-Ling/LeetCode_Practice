

class Solution:

    # Time: O(n)

    """
    "neet", "co#de"

    4#neet 5#co#de
    """
    
    def encode(self, strs):
        # write your code here
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res


    def decode(self, str):
        """
        4#neet5#co#de
        
        "neet", "co#de"
        """

        # i tells us which position we are at in this input string
        res, i = [], 0

        while i < len(str):
            j = i

            while str[j] != "#":
                j += 1

            # This length variable tells us how many following characters we have to read after j in order to  
            #   get every character of the string
            length = int(str[i:j])
            print(str[0:1])

            # It will give us the entire string
            res.append(str[j + 1:j + 1 + length])

            # The beginning of next string
            i = j + 1 + length

        return res

s = Solution()
print(s.encode(["neet", "co#de"]))
print(s.decode("4#neet5#co#de"))