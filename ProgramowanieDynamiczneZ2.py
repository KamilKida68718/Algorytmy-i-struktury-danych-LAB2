"""Korzystając z techniki programowania dynamicznego wyznacz wartość wyrażenia:"""

def P(i, j):
    if i > 0 and j == 0:
        return 0 
    elif i ==0 and j > 0:
        return 1
    elif i> 0 and j > 0:
        return (P(i-1,j)+P(i,j-1))/2
    


a = P(5,5)

print("Wartość wyrażenia: ",a)