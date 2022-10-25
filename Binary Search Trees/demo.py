from helper import Helper


class Node:
    def __init__(self, value):
        self.value = value
        self.left_value = None
        self.right_value = None


class BinarySearchTree:
    def __init__(self):
        self.__root = None
        self.__temp = self.__root

    def insert(self, value):
        if not self.__root:
            self.__root = Node(value)
            self.__temp = self.__root
            return print("Inserted value as root...")
        return self.__insert_node(self.__root, value)

    def __insert_node(self, node, value):
        if value < node.value:
            if node.left_value:
                return self.__insert_node(node.left_value, value)
            node.left_value = Node(value)
        else:
            if node.right_value:
                return self.__insert_node(node.right_value, value)
            node.right_value = Node(value)
            return

    def traverse(self):
        Helper.return_if_tree_is_empty(self.__root)
        self.__traverse_in_order(self.__root)

    def __traverse_in_order(self, node):
        if node.left_value:
            self.__traverse_in_order(node.left_value)

        print(node.value)

        if node.right_value:
            self.__traverse_in_order(node.right_value)

    def traverse_preorder(self):
        Helper.return_if_tree_is_empty(self.__root)
        return self.__traverse_preorder_by_node(self.__root)

    def __traverse_preorder_by_node(self, node):
        if node.value:
            print(node.value)
        if node.left_value:
            self.__traverse_preorder_by_node(node.left_value)
        if node.right_value:
            self.__traverse_preorder_by_node(node.right_value)

    def traverse_postorder(self):
        Helper.return_if_tree_is_empty(self.__root)
        return self.__traverse_postorder_by_node(self.__root)

    def __traverse_postorder_by_node(self, node):
        if node.left_value:
            self.__traverse_postorder_by_node(node.left_value)
        if node.right_value:
            self.__traverse_postorder_by_node(node.right_value)
        if node.value:
            print(node.value)

    def get_min(self):
        Helper.return_if_tree_is_empty(self.__root)
        return self.__get_min_value(self.__root)

    def __get_min_value(self, node):
        if node.left_value:
            return self.__get_min_value(node.left_value)
        return node.value

    def get_max(self):
        Helper.return_if_tree_is_empty(self.__root)
        return self.__get_max_value(self.__root)

    def __get_max_value(self, node):
        if node.right_value:
            return self.__get_max_value(node.right_value)
        return node.value

    def remove(self, value):
        if not self.__root:
            return
        self.remove_node(value, self.__root)

    def remove_node(self, value, node):
        if not node:
            return node

        if value < node.value:
            node.left_value = self.remove_node(value, node.left_value)
        elif value > node.value:
            node.right_value = self.remove_node(value, node.right_value)
        else:
            if not node.left_value and not node.right_value:
                print(f"Removed node with no children, value: {node.value}")
                del node
                return
            elif not node.left_value:
                print(f"Removed node with one child, value: {node.value}")
                node = node.right_value
                return
            elif not node.right_value:
                print(f"Removed node with one child, value: {node.value}")
                node = node.left_child
                return

            print(f"Removing node with two children: {node.value}")
            temp_node = self.__get_predecessor(node)
            node.data = temp_node.data
            node.left_value = self.remove_node(node.value, node.left_value)

        return node

    def __get_predecessor(self, node):
        if node.left_value:
            return self.__get_predecessor(node.left_value)
        return node

    def is_exists(self, value):
        while True:
            if not self.__temp.left_value and not self.__temp.right_value:
                return False

            if value < self.__temp.value:
                self.__temp = self.__temp.left_value
            elif value > self.__temp.value:
                self.__temp = self.__temp.right_value
            else:
                return True



