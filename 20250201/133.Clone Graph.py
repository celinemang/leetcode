"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None  # Edge case: empty graph
        
        visited = {}  # HashMap to store cloned nodes

        def dfs(original_node):
            if original_node in visited:
                return visited[original_node]  # Return cloned node if already created
            
            # Create a new node with the same value
            clone = Node(original_node.val)
            visited[original_node] = clone  # Store cloned node
            
            # Recursively clone neighbors
            for neighbor in original_node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)
  