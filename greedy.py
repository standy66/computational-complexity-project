import math

def set_cover_greedy(universe, sets):
    set_cover = []
    while (universe):
        best_set = []
        best_set_coverage = 0
        for s in sets:
            coverage = 0
            for elem in s:
                if (elem in universe):
                    coverage = coverage + 1
            if (coverage >= best_set_coverage):
                best_set = s
        if (best_set == []):
            raise RuntimeError("no solution")
        for elem in best_set:
            if (elem in universe):
                universe.remove(elem)
        sets.remove(best_set)
        set_cover.append(best_set)
    return set_cover

a = [1,2,3,4,5,6,7,8,9]
b = [[1,2,3],[4,5,6],[7,8,9],[1,2,4,5,7,8]]
print(set_cover_greedy(a, b))
