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
        	for sub_ind in range(-1,ind-len(s)-1,-1): # this backward trick is useful 
        		if s[ind] == s[sub_ind]:
        			check_string = s[ind:] if sub_ind == -1 else s[ind:sub_ind+1]
        			if self.is_palin(check_string): # the problem with adding to negative index
        				all_palinds.append(check_string)
        				break
        return max(all_palinds,key = lambda x: len(x))

sol = Solution()
for_testing = ['aababakdjf','a','ab','abb','colosojoso','perepoffjs','sssssssssskokokok','sjjjsox','aporopavengenceecnegnev']
for one_item in for_testing:
    print(one_item)
    print(f'longest palindrome: {sol.longestPalindrome(one_item)}',end = '\n\n')