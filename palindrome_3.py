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
        #returns the longest palindrome
        #here I will use sliding window
        if len(s) == 1:
        	return s
        all_palins = [s[0]]
        for N in range(2,len(s)+1):
        	for i in range(len(s)-(N-1)):
        		if self.is_palin(s[i:i+N]):
        			all_palins.append(s[i:i+N])
        			break
        return max(all_palins,key = lambda x: len(x))


