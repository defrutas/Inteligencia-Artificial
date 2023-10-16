class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        
        return level

    def print_tree(self):
        
        spaces = ' ' * self.get_level() * 5   #adiciona espacos de acordo com o nivel do node
        prefix = spaces + "|__" if self.parent else ""

        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_product_tree():
    root = TreeNode("Inicio")
    
    nodeA = TreeNode("A")
    nodeA.add_child(TreeNode("A1"))
    nodeA.add_child(TreeNode("A2"))
    nodeA.add_child(TreeNode("A3"))
    nodeA11 = TreeNode("A11")
    
    nodeB = TreeNode("B")
    nodeB.add_child(TreeNode("B1"))
    nodeB.add_child(TreeNode("B2"))
    nodeB.add_child(TreeNode("B3"))

    nodeC = TreeNode("C")
    nodeC.add_child(TreeNode("C1"))
    nodeC.add_child(TreeNode("C2"))

    root.add_child(nodeA)
    root.add_child(nodeB)
    root.add_child(nodeC)
    
    return root

if __name__ == '__main__':
   root = build_product_tree()
   root.print_tree()
   pass



# def depth_first_search(node, target_value):
#     if node is None:
#         return None

#     if node.data == target_value:
#         return node

#     for child in node.children:
#         result = depth_first_search(child, target_value)
#         if result:
#             return result

#     return None

# # Example usage:
# # Create a sample tree
# root = TreeNode("A")
# root.add_child(TreeNode("B"))
# root.add_child(TreeNode("C"))
# root.children[0].add_child(TreeNode("D"))
# root.children[0].add_child(TreeNode("E"))
# root.children[1].add_child(TreeNode("F"))

# # Explore the tree using depth-first search
# target_node = depth_first_search(root, "F")
# if target_node:
#     print(f"Found target node with data: {target_node.data}")
# else:
#     print("Target node not found")
