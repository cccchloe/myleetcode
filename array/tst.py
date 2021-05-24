def kthGrammar( N, K):
    if N == 1: return 0
    prevK = kthGrammar(N - 1, (K + 1) // 2)
    print("1-" + str(K) + "%2 = " + str(1 - K % 2)  + "^ " + str(prevK))
    return (1 - K % 2) ^ prevK

print(kthGrammar(3,3))
print(str(0^1))
