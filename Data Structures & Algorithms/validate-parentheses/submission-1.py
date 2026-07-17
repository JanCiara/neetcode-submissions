class Solution:
    def isValid(self, s: str) -> bool:
        mp = {'(' : ')',
            '{' : '}',
            '[' : ']'}

        stack = []

        for c in s:
            if c in mp.keys():
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack[-1]
                if c == mp[top]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0