class Solution:
    def countAndSay(self, n: int) -> str:
        def evaluate(s):#evaluate function declare
            i = 0;res = []#variables and resultant array declare
            while i < len(s):#iterating the indx <len(s) 
                number= s[i];count = 1#nums's string 's indxing and counter's declare
                while (i+1) < len(s) and s[i] == s[i+1]:#iterating string's length
                    i += 1;count += 1#incrementing  both the indx and counter 
                res.append((str(count), number))#appending the resultant 's string 
                i += 1#incrementign idx pos
            
            for i in range(len(res)):res[i] = res[i][0] + res[i][1]#iterating the resultant length
            
            return "".join(res)#printing the joined result 
        
        def solution(n):#solution fucnt declare
            if n == 1:return "1"#assigning n to 1 and printing 1
            else:return evaluate(solution(n-1)) #callign the evaluate funct for n-1 count's
        
        return solution(n)#printing solution
        
