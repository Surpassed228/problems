class Solution:
    def is_palin(self,s:str) -> bool:
        #checks whether a given string is a palindrom
        #the assumption is that the mininum length of a string is 1
        if len(s) == 1:
            return True
        else:
            forward = []
            backward = []

            for ind in range(len(s)):
                forward.append(s[ind])
            for back_ind in range(-1,-(len(s)+1),-1):
                backward.append(s[back_ind])
            
            return True if backward == forward else False

    def longestPalindrome(self, s: str) -> str:
        #returns the longest palindrom
        if len(s) == 1:
            return s
        all_palinds = []
        for ind in range(len(s)-1):
            sub_palinds = []
            cur_substr = s[ind]
            sub_palinds.append(cur_substr)
            for sub_ind in range(ind+1,len(s)):
                if not self.is_palin(cur_substr + s[sub_ind]):
                    cur_substr += s[sub_ind]
                else:
                    cur_substr += s[sub_ind]
                    sub_palinds.append(cur_substr)
            all_palinds.append(max(sub_palinds,key = lambda x: len(x)))
        return max(all_palinds,key = lambda x: len(x))


