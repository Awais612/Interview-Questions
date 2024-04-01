# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getTargetCopy(original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    def dfs(node, target_val):
        if not node:
            return None
        if node.val == target_val:
            return node
        left = dfs(node.left, target_val)
        if left:
            return left
        return dfs(node.right, target_val)
    
    return dfs(cloned, target.val)
