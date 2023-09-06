class Tree:
    def __init__(self, node_data):
        self.root = node_data

    def depth_first_search(self, node, target_id):
        if node['id'] == target_id:
            return node

        for child in node['children']:
            result = self.depth_first_search(child, target_id)
            if result:
                return result

        return None

    def breadth_first_search(self, target_id):
        queue = [self.root]

        while queue:
            node = queue.pop(0)
            if node['id'] == target_id:
                return node

            queue.extend(node['children'])

        return None

    def get_element_by_id(self, target_id, depth_first=True):
        if depth_first:
            return self.depth_first_search(self.root, target_id)
        else:
            return self.breadth_first_search(target_id)
