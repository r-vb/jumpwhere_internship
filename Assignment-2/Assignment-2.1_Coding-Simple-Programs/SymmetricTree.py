def aresymmetric(root1,root2):
    if root1 is None and root2 is None:
        return True
    elif ((root1 is None) != (root2 is None)) or root1.val != root2.val:
        return False
    else:
        return (aresymmetric(root1.left, root2.right) and aresymmetric(root1.right, root2.left))
def issymmetric(root):
    if root is None:
        return True
    return aresymmetric(root.left, root.right)
# T: O(n)
# S: O(logn)