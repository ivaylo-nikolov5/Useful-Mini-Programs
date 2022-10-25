class Helper:
    @staticmethod
    def return_if_tree_is_empty(root):
        if not root:
            raise Exception("The binary search tree is empty!")