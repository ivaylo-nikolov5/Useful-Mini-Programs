class Node(object):
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class BinarySearchTree(object):
    def __init__(self):
        self.__root = None

    def insert(self, data):
        if not self.__root:
            self.__root = Node(data)
        else:
            self.insert_node(data, self.__root)

    def insert_node(self, data, node):
        if data < node.data:
            if node.left_child:
                self.insert_node(data, node.left_child)
            else:
                node.left_child = Node(data)
        else:
            if node.right_child:
                self.insert_node(data, node.right_child)
            else:
                node.right_child = Node(data)

    def get_min_value(self):
        if not self.__root:
            return
        return self.get_min(self.__root)

    def get_min(self, node):
        if not node.left_child:
            return node.data
        else:
            return self.get_min(node.left_child)

    def get_max_value(self):
        if not self.__root:
            return
        return self.get_max(self.__root)

    def get_max(self, node):
        if not node.right_child:
            return node.data
        return self.get_max(node.right_child)

    def traverse(self):
        if not self.__root:
            return
        self.traverse_in_order(self.__root)

    def traverse_in_order(self, data):
        if data.left_child:
            self.traverse_in_order(data.left_child)

        print(data.data)

        if data.right_child:
            self.traverse_in_order(data.right_child)

    def remove(self, data):
        if not self.__root:
            return
        self.remove_node(data, self.__root)

    def remove_node(self, data, node):
        if not node:
            return node

        if data < node.data:
            node.left_child = self.remove_node(data, node.left_child)
        elif data > node.data:
            node.right_child = self.remove_node(data, node.right_child)
        else:
            if not node.left_child and not node.right_child:
                print("Deleting a leaf node...")
                del node
                return
            elif not node.left_child:
                print("Removing node with single right child...")
                temp_node = node.right_child
                del node
                return temp_node
            elif not node.right_child:
                print("Removing node with single left child...")
                temp_node = node.left_child
                del node
                return temp_node

            print("Removing node with two children...")
            temp_node = self.get_predeccor(node.left_child)
            node.data = temp_node.data
            node.left_child = self.remove_node(temp_node.data, node.left_child)
        return node

    def get_predeccor(self, node):
        if node.right_child:
            return self.get_predeccor(node.right_child)
        return node

