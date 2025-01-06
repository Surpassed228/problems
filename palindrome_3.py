class Solution:
    def is_palin(self,s:str) -> bool:
    	#maybe the the check should be rewritten
    	#I will use recursion here, this should help
    	if len(s) == 1 or len(s) == 0:
    		return True
    	else:
    		if s[0] == s[-1] and self.is_palin(s[1:-1]):
    			return True
    		else:
    			return False


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
 