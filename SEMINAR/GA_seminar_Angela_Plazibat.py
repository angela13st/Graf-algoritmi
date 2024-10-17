def winners(N, votes):
    strength = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if i != j:
                strength[i][j] = votes[i * N + j] - votes[j * N + i]


    # Floyd-Warshall algoritam za izračunavanje jačina svih argumenata
    for k in range(N):
        for i in range(N):
            for j in range(N):
                strength[i][j] = max(strength[i][j], min(strength[i][k], strength[k][j]))

    potential_winners = []

    for i in range(N):
        is_potential_winner = all(strength[i][j] >= strength[j][i] for j in range(N) if i != j)
        if is_potential_winner:
            potential_winners.append(i)


    return sorted(potential_winners)

# Primjer korištenja, očekivani rezultat [4]
result = winners(5, [0, 20, 26, 30, 22, 25, 0, 16, 33, 18, 19, 29, 0, 17, 24, 15, 12, 28, 0, 14, 23, 27, 21, 31, 0])
print(result)
