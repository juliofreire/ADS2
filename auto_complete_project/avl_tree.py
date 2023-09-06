class Node:


    def __init__(self, value):

        self.value = value
        self.left_child = None
        self.right_child = None


class BST:

    def __init__(self):

        self.root = None

    def add(self, value):

        if self.root is None:
            self.root = Node(value)
        else:
            self._add_recursive(self.root, value)

    def _add_recursive(self, current_node, value):

        if value <= current_node.value:
            if current_node.left_child is None:
                current_node.left_child = Node(value)
            else:
                self._add_recursive(current_node.left_child, value)
        else:
            if current_node.right_child is None:
                current_node.right_child = Node(value)
            else:
                self._add_recursive(current_node.right_child, value)

    def _contains(self, current_node, value):

        if current_node is None:
            return False
        if current_node.value == value:
            return True
        if value < current_node.value:
            return self._contains(current_node.left_child, value)
        return self._contains(current_node.right_child, value)

    def contains(self, value):
        return self._contains(self.root, value)

class AVLNode(Node):

    def __init__(self, value):
        super().__init__(value)
        self.height = 1
        self.imbalance = 0

    def calculate_height_and_imbalance(self):
        # Calculate the height of the left child subtree
        left_height = 0
        if self.left_child is not None:
            left_height = self.left_child.height

        # Calculate the height of the right child subtree
        right_height = 0
        if self.right_child is not None:
            right_height = self.right_child.height

        # Update the height of this node
        self.height = 1 + max(left_height, right_height)

        # Calculate and update the imbalance factor for this node
        self.imbalance = left_height - right_height

class AVLTree(BST):
    def __init__(self):

        super().__init__()

    def add(self, value):

        self.root = self._add_recursive(self.root, value)  # Note that self.root is updated here


    def _add_recursive(self, current_node, value):

        # If the current node is None, return a new AVLNode containing the value
        if current_node is None:
            return AVLNode(value)

        # Check if current_node is of the base class Node and cast it to AVLNode if necessary
        # This is necessary to not change the add() in the BST class.
        # When the first node is added, the type of the root is Node, so we need to cast it
        if isinstance(current_node, Node) and not isinstance(current_node, AVLNode):
            current_node = AVLNode(current_node.value)
            current_node.left_child = self.root.left_child
            current_node.right_child = self.root.right_child
            self.root = current_node

        # Determine whether the value should be inserted to the left or right subtree
        if value <= current_node.value:
            current_node.left_child = self._add_recursive(current_node.left_child, value)
        else:
            current_node.right_child = self._add_recursive(current_node.right_child, value)

        # Update the height and imbalance factor for the current node
        current_node.calculate_height_and_imbalance()

        # Check if tree balancing is needed and balance if necessary
        if abs(current_node.imbalance) == 2:
            return self._balance(current_node)

        return current_node

    def get_height(self):

        if self.root is None:
            return 0
        return self.root.height

    def _rotate_left(self, node):

        # Store the pivot (the root of the right subtree of 'node')
        pivot = node.right_child

        # Update the right child of 'node' to be the left child of the pivot
        node.right_child = pivot.left_child

        # Set the left child of the pivot to be the node
        pivot.left_child = node

        # Recalculate the height and imbalance factor for the rotated node
        node.calculate_height_and_imbalance()

        # Recalculate the height and imbalance factor for the pivot
        pivot.calculate_height_and_imbalance()

        # Return the pivot as the new root of this subtree
        return pivot


    def _rotate_right(self, node):

        # Store the pivot (the root of the left subtree of 'node')
        pivot = node.left_child

        # Update the left child of 'node' to be the right child of the pivot
        node.left_child = pivot.right_child

        # Set the right child of the pivot to be the node
        pivot.right_child = node

        # Recalculate the height and imbalance factor for the rotated node
        node.calculate_height_and_imbalance()

        # Recalculate the height and imbalance factor for the pivot
        pivot.calculate_height_and_imbalance()

        # Return the pivot as the new root of this subtree
        return pivot

    def _balance(self, node):


      # Case 1: Left subtree is higher than right subtree
      if node.imbalance == 2:
          pivot = node.left_child
          # Single right rotation
          if pivot.imbalance == 1:
              return self._rotate_right(node)
          # Double rotation: Left-Right
          else:
              node.left_child = self._rotate_left(pivot)
              return self._rotate_right(node)
      # Case 2: Right subtree is higher than left subtree
      else:
          pivot = node.right_child
          # Single left rotation
          if pivot.imbalance == -1:
              return self._rotate_left(node)
          # Double rotation: Right-Left
          else:
              node.right_child = self._rotate_right(pivot)
              return self._rotate_left(node)
          
    def search_prefix(self,node,prefix):
        if node is None: #Ou seja, caso o nó esteja vazio
            return []
        if node.value.startswith(prefix):
            return [node.value] + self.search_prefix(node.left_child,prefix)+self.search_prefix(node.right_child,prefix)
        if prefix < node.value:
            return self.search_prefix(node.left_child,prefix)
        else:
            return self.search_prefix(node.right_child,prefix)

    def search_word(self,prefix):
        return self.search_prefix(self.root,prefix)
    
import plotly.graph_objects as go

def visualize_avl_tree(avl_tree):

    # Lists to store node values, hover texts, x and y coordinates, and edge coordinates
    node_values = []
    hover_texts = []
    Xn, Yn = [], []
    Xe, Ye = [], []

    # Traversing the tree to collect node and edge data
    def traverse(node, x=0, y=0, layer=1):
        if node is not None:
            node_values.append(node.value)
            hover_texts.append(f"Value: {node.value}Height: {node.height}Imbalance: {node.imbalance}")
            Xn.append(x)
            Yn.append(y)
            if node.left_child:
                Xe.extend([x, x - layer])
                Ye.extend([y, y - layer * 2])
                traverse(node.left_child, x=x-layer, y=y-layer*2, layer=layer/2)
            if node.right_child:
                Xe.extend([x, x + layer])
                Ye.extend([y, y - layer * 2])
                traverse(node.right_child, x=x+layer, y=y-layer*2, layer=layer/2)

    # Initialize traversal with the root node of the AVL tree
    traverse(avl_tree.root)

    # Create Plotly figure
    fig = go.Figure()

    # Add nodes (as scatter plot)
    fig.add_trace(go.Scatter(x=Xn,
                             y=Yn,
                             mode='markers+text',
                             name='Nodes',
                             marker=dict(symbol='circle-dot',
                                         size=30,
                                         color='blue'),
                             text=node_values,  # This will appear inside the node
                             hoverinfo='text',
                             hovertext=hover_texts,  # This will appear upon hover
                             textposition='top center'))

    # Add edges (as line plot)
    fig.add_trace(go.Scatter(x=Xe,
                             y=Ye,
                             mode='lines',
                             name='Edges',
                             line=dict(width=1.5, color='gray')))

    # Set layout properties
    fig.update_layout(showlegend=False,
                      hovermode='closest',
                      xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                      yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))

    fig.show()
          
###########


# import random

# NUM_VALUES = 10000
# random.seed(0)
# rnd_values = [random.randint(1, 10000) for _ in range(NUM_VALUES)]
# avl = AVLTree()
# for v in rnd_values:
#     avl.add(v)
# print(avl.root.height)

# for v in rnd_values:
#     assert avl.contains(v)

# visualize_avl_tree(avl)


# import time
# import plotly.express as px

# # Generate experiment numbers (replace this with your actual experiment numbers)
# experiment_numbers = list(range(1, len(rnd_values) + 1))

# times_list = []
# times_avl = []

# for v in rnd_values:
#     # Measure runtime for list
#     start = time.time()
#     v in rnd_values
#     end = time.time()
#     times_list.append(end - start)

#     # Measure runtime for AVL
#     start = time.time()
#     avl.contains(v)
#     end = time.time()
#     times_avl.append(end - start)

# # Convert to milliseconds for better visualization
# times_list_ms = [t * 1000 for t in times_list]
# times_avl_ms = [t * 1000 for t in times_avl]

# # Create a Plotly figure as a scatter plot

# fig = px.scatter(x=[experiment_numbers], y=times_list_ms, labels={"x": "Experiment Number", "y": "Runtime (ms)"},
#                  title="Runtime Comparison: List vs. AVL", template="plotly_dark")
# fig.add_scatter(x=experiment_numbers, y=times_avl_ms, mode='markers', name='AVL Tree', marker=dict(size=8))

# # Update axes properties
# fig.update_xaxes(showline=True, linewidth=1, linecolor="gray")
# fig.update_yaxes(showline=True, linewidth=1, linecolor="gray")
# # Change the name in the legend
# fig.update_traces(name="List", selector=dict(name="wide_variable_0"))

# # Show the figure
# fig.show()



