def solve(N, A, Q, operations):
    
    # for i in range(Q):
    #     for j in range(N):
    #         if operations[0] == 1:
    #             for k in range(operations[1], operations[3]):
    #                 print(k)


    for op in operations:
        type_op, L, R, X = op

        # Update array A according to the operation type
        for i in range(L - 1, R):
            if type_op == 1:
                A[i] += X
            else:
                A[i] -= X

    print(A)

    res = 0

    A.insert(0, 0)

    print(A)

    for i in range(1, N+1):
        for j in range(i+1, N+1):
            for k in range(j+1, N+1):
                if 1 <= i and i <= j and j <= k and k <= N:
                    res += (A[i] + A[j]) * (A[j] + A[k])
                    print(f' {A[i]} + {A[j]} * {A[j]} + {A[k]}  = {res}')

    
    return res


T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    operations = [list(map(int, input().split())) for i in range(Q)]

    out_ = solve(N, A, Q, operations)
    print (out_)
