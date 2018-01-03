
def isPalindrome(s):
	 s_rev=s[::-1]
	 r=len(s)
	 count=0
	 for i in range(0,r-1):
	 	if s[i] is s_rev[i]:
	 		return 0
	 	else:
	 		count+=1
	 		return count
print isPalindrome('abcdecba')