class UnionFind:
    def __init__(self, n):
        # 0..n-1
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        """
        Find the representative (root) of the set containing x,
        with path compression.
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """
        Union the sets containing x and y using union by rank.
        Returns True if a merge happened, False if they were
        already in the same set.
        """
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return False

        # attach smaller-rank tree under larger-rank tree
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
        return True

    def connected(self, x, y):
        """
        Check if x and y are in the same set.
        """
        return self.find(x) == self.find(y)
