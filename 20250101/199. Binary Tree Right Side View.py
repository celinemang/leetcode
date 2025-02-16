class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        queue = collections.deque([root])
        rightside = []

        
        while queue:
            level_length = len(queue)

            for i in range(level_length):
	            node = queue.popleft()
	            if i == level_length - 1:
		            rightside.append(node.val)
		           if node.left:
			           queue.append(node.left)
			         if node.right:
				         queue.append(node.right)

        return rightside
