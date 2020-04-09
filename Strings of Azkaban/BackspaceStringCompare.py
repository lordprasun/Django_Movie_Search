"""
Given two strings S and T, 
return if they are equal when both are typed into empty text editors.
# means a backspace character.
"""
def backspaceCompare(self, S: str, T: str) -> bool:
        stackS = []
        stackT = []
        for k,in S:
            if k=='#':
                if len(stackS)>0:
                    stackS.pop()
            else:
                stackS.append(k)
        for v,in T :
            if v=='#':
                if len(stackT)>0:
                    stackT.pop()
            else:
                stackT.append(v)
        return stackS==stackT

def backspaceCompare_1(S,T):
        stackS = []
        stackT = []
        for k,in S:
            if k=='#' and len(stackS)>0:
                stackS.pop()
            else:
                stackS.append(k)            
        for v,in T :
            if v=='#' and len(stackT)>0:
                stackT.pop()
            else:
                stackT.append(v)            
        print(stackS)
        print(stackT)
        return stackS==stackT

res = backspaceCompare("y#fo##f","y#f#o##f")