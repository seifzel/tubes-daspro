def Konso(e, L):
    return [e] + L

def Konsi(L, e):
    return L + [e]

def FirstElmt(L):
    return L[0]

def Tail(L):
    return L[1:] 

def LastElmt(L):
    return L[-1]

def Head(L):
    return L[:-1]

def IsEmpty(L):
    return L == []

def IsOneElmt(L):
    if IsEmpty(L):
        return False
    else:
        return Tail(L) == [] and Head(L) == []
    
def IsMember(X, L):
    if IsEmpty(L):
        return False
    else:
        return IsMember(X, Tail(L)) or X == FirstElmt(L)

def IsEqual(L1, L2):
    if IsEmpty(L1) and IsEmpty(L2):
        return True
    elif IsEmpty(L1):
        return False
    elif IsEmpty(L2):
        return False
    elif FirstElmt(L1) == FirstElmt(L2):
        return IsEqual(Tail(L1), Tail(L2))
    else:
        return False

def NbElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return 1 + NbElmt(Tail(L))
    
def sumelmt(L):
    if IsEmpty(L):
        return 0
    else:
        return FirstElmt(L) + sumelmt(Tail(L)) 