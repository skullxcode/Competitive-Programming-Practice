import sys

def solve():
    # Use fast I/O
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    iterator = iter(data)
    try:
        t_str = next(iterator)
        t = int(t_str)
    except StopIteration:
        return

    results = []
    
    for _ in range(t):
        try:
            X = int(next(iterator))
        except StopIteration:
            break
            
        N = 1
        
        while True:
            S = N * (N + 1) // 2
            
            # Check basic conditions
            possible = True
            
            # 1. Magnitude constraints: Sum must be large enough to reach X (positive or negative)
            if S < X: possible = False
            if S < 2 - X: possible = False # Equivalent to ensuring we can reach negative X
            
            if possible:
                diff = S - X
                
                # 2. Parity Check: Difference must be even
                if diff % 2 == 0:
                    target = diff // 2
                    
                    # 3. Subset Sum Check on {2, 3, ... N}
                    # We need to find a subset of {2..N} that sums to 'target'.
                    # Impossible sums for {2..N} are:
                    # - 1 (smallest element is 2)
                    # - (Sum of set) - 1 => (S - 1) - 1 = S - 2
                    if target != 1 and target != S - 2:
                        break # Found valid N
            
            N += 1
            
        results.append(str(N))
        
        # Reconstruct the expression
        # target is the sum we need to subtract
        target = (S - X) // 2
        
        # 'signs' array to store operations. + is default.
        signs = ['+'] * (N + 1)
        
        # Greedy approach: subtract largest possible values first
        for i in range(N, 1, -1):
            if target >= i:
                target -= i
                signs[i] = '-'
        
        # Build the output string
        # 1 is always positive
        expression = ["1"]
        for i in range(2, N + 1):
            expression.append(signs[i])
            expression.append(str(i))
            
        results.append("".join(expression))

    print("\n".join(results))

if __name__ == "__main__":
    solve()