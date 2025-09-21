class AVLNode:
    """
    Node representation for an AVL Tree.

    Attributes
    ----------
    key : int or comparable
        The value stored in the node, used for ordering in the binary search tree.
    height : int
        The height of the node in the tree, used to maintain AVL balance property.
    left : AVLNode or None
        Reference to the left child node.
    right : AVLNode or None
        Reference to the right child node.
    """
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.key) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret


class AVLTree:
    """Implementation of an AVL Tree (self-balancing binary search tree)."""

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def rotate_left(self, pivot_node):
        new_root = pivot_node.right
        moved_subtree = new_root.left

        new_root.left = pivot_node
        pivot_node.right = moved_subtree

        pivot_node.height = 1 + max(self.get_height(pivot_node.left), self.get_height(pivot_node.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root

    def rotate_right(self, pivot_node):
        new_root = pivot_node.left
        moved_subtree = new_root.right

        new_root.right = pivot_node
        pivot_node.left = moved_subtree

        pivot_node.height = 1 + max(self.get_height(pivot_node.left), self.get_height(pivot_node.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def insert(self, root, key):
        if not root:
            return AVLNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1:
            if key < root.left.key:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)

        if balance < -1:
            if key > root.right.key:
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root

    def delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if root is None:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1:
            if self.get_balance(root.left) >= 0:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)

        if balance < -1:
            if self.get_balance(root.right) <= 0:
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root

    def sum_tree(self, node):
        if node is None:
            return 0
        return node.key + self.sum_tree(node.left) + self.sum_tree(node.right)


if __name__ == "__main__":
    tree = AVLTree()
    root = None

    keys = [10, 20, 30, 25, 28, 27, -1]
    for key in keys:
        root = tree.insert(root, key)
        print("Inserted:", key)
        print("AVL Tree:")
        print(root)

    print("Sum:", tree.sum_tree(root))

    keys_to_delete = [10, 27]
    for key in keys_to_delete:
        root = tree.delete(root, key)
        print("Deleted:", key)
        print("AVL Tree:")
        print(root)

    print("Sum:", tree.sum_tree(root))
