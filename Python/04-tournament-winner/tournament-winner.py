def tournamentWinner(competitions, results):
    lst = []
    for v in range(len(results)):
        if results[v] == 0: # away team
            lst.append(competitions[v][1])
        elif results[v] == 1: # home team
            lst.append(competitions[v][0])

    d = {}
    for elem in lst:
        if elem in d:
            d[elem] += 1
        else:
            d[elem] = 1
    print(d)
    
    max_count = -1
    winner = None
    for key, value in d.items():
        if value > max_count:
            max_count = value
            winner = key        
    return winner
