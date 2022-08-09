from itertools import permutations
from typing import Dict
import operator


def find_min(dict: Dict[str, int], removed):
    stats = {}
    for (key, value) in dict.items():
        temp: str = str(key)
        for c in removed:
            temp = temp.replace(c, '')

        vote_for = temp[0]

        stats[vote_for] = stats.get(vote_for, 0) + dict[key]

    # print result
    print(f'    *{stats}')
    min_candidate = min(stats.items(), key=operator.itemgetter(1))[0]
    print(f'    *Arg min: {min_candidate}')
    return min_candidate


def run_simulation(candidates, data):
    perm = list(map(lambda x: ''.join(x), permutations(candidates)))
    dict = {}
    for i in range(len(perm)):
        dict[perm[i]] = data[i]
    print(f'Data: {dict}')
    removed = []

    iteration = 1
    while len(removed) < len(candidates) - 1:
        print(f'Iteration: {iteration}')
        k = find_min(dict, removed)
        removed.append(k)
        iteration += 1

    # print final result
    winner = set(candidates) - set(removed)
    print(f'Winner: {winner}')


if __name__ == '__main__':
    candidates = ['A', 'B', 'C']
    data = [11, 13, 17, 10, 20, 5]
    run_simulation(candidates, data)

    candidates = ['A', 'B', 'C']
    data = [20, 13, 17, 10, 20, 5]
    run_simulation(candidates, data)

    candidates = ['A', 'B', 'C', 'D']
    data = [i for i in range(24)]
    run_simulation(candidates, data)
