class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_tree_from_array(input):
    if len(input) == 0:
        return

    nodes = list(map(lambda x: None if x is None else TreeNode(x), input))
    for i in range(1, len(nodes)):
        if nodes[i] is None:
            continue

        parent_index = (i -1) // 2
        if i % 2 == 1:
            nodes[parent_index].left = nodes[i]
        else:
            nodes[parent_index].right = nodes[i]

    return nodes[0]
