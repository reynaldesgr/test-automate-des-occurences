
# Construit un automate des occurrences (automate définit par un pattern.)

def alphabet(p):
    return { letter for letter in p}

def is_suffix(p, x):
    if(p == x):
        return True
    for i in range(len(p)):
        if p[i:] == x:
            return True
    return False

def is_prefix(p, x):
    if(p == x):
        return True
    for i in range(len(p)):
        if p[:i] == x:
            return True
    return False

def calcul_fonction_delta(pattern, alpha):
    m = len(pattern)
    delta = {}
    for q in range(m):
        for label in alpha:
            k = min(m, q + 1)
            i = k
            j = 0
            p_suffix = pattern[:k-1]+label
            while not is_prefix(pattern[:i], p_suffix) and k  > 0:
                k-=1
                j+=1
                p_suffix = p_suffix[1:]
            delta[(q, label)] = k
    return delta

p = "ababaca"
print("== Alphabet ==")
alpha = sorted(alphabet(p))
print(alpha)

print("== Calcul préfixe delta ==")
d = calcul_fonction_delta(p, alpha)
print(d)
print(is_prefix("ab", "ab"))