class solution(object):
    def longestValidParentheses(self,s):
        d={')':'('}
        maxlen=0
        for i in range(1,len(s)):
            l,r=i-1,i
            while l>=0 and r<len(s) and s[l]==d.get(s[r]):
                if r-l+1>maxlen:
                    maxlen=r-l+1
                l-=1
                r+=1
        return maxlen
    #another more efficent version
    def v2(self,s):
        stack=[-1]
        maxlen=0
        for i in range(len(s)):
            t=stack[-1]
            if t!=-1 and s[i]==')' and s[t]=='(':
                stack.pop()
                maxlen=max(maxlen,i-stack[-1])
            else:
                stack.append(i)
        return maxlen
    
