
class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        simplify_path = []

        index = 0
        l = len(path)
        while index < l:
            while index < l and path[index] == '/':
                index += 1
            if index >= l:
                return self.combinePath(simplify_path)
            
            if path[index] == '.':
                if index + 1 < l:
                    if path[index + 1] == '.':
                        if index + 2 >= l or path[index + 2] == '/':
                            if simplify_path:
                                simplify_path.pop()
                            index += 1
                        else:
                            start = index
                            while index < l and path[index] != '/':
                                index += 1
                            simplify_path.append(path[start:index])
                    elif path[index + 1] != '/':
                        start = index
                        while index < l and path[index] != '/':
                            index += 1
                        simplify_path.append(path[start:index])
            else:
                start = index
                while index < l and path[index] != '/':
                    index += 1
                simplify_path.append(path[start:index])
                        
            index += 1
        return self.combinePath(simplify_path)
        
    def combinePath(self, path):
        if not path:
            return '/'

        str = ""
        for p in path:
            str += "/" + p
        return str
        
if __name__ == "__main__":
    s = Solution()

    assert s.simplifyPath("/home/") == '/home'
    assert s.simplifyPath("/a/./b/../../c/") == '/c'
    assert s.simplifyPath("/////home//foo/////") == '/home/foo'
    assert s.simplifyPath("/../") == '/'
    assert s.simplifyPath("/...") == '/...'
    assert s.simplifyPath("/..") == '/'
