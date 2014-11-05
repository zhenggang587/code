
class Solution:
    def getSolution(self, graph):
        queue = [0]
        colors = {0: 0}

        while queue:
            v = queue.pop(0)
            color = 1 - colors[v]
            for vertex in graph[v]:
                if vertex not in colors:
                    colors[vertex] = color
                    queue.append(vertex)
                elif colors[vertex] != color:
                    return False
        return True


if __name__ == "__main__":
    s = Solution()
    
    print s.getSolution([[1, 2, 3], [0, 3], [0, 3], [1, 2]])
