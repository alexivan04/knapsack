class Poz:
    def __init__(self, g, c):
        self.g = g
        self.c = c

def dinamica(n, G, a):
    # Initialize the DP table with zeros
    C = [[0] * (G + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, G + 1):
            if a[i - 1].g <= j and a[i - 1].c + C[i - 1][j - a[i - 1].g] > C[i - 1][j]:
                C[i][j] = a[i - 1].c + C[i - 1][j - a[i - 1].g]
            else:
                C[i][j] = C[i - 1][j]
    
    return C

def main():
    # Input
    n, G = map(int, input().split())
    a = []
    for _ in range(n):
        g, c = map(int, input().split())
        a.append(Poz(g, c))
    
    # Solve using dynamic programming
    C = dinamica(n, G, a)
    
    # Output the result
    print(C[n][G])

if __name__ == "__main__":
    main()
