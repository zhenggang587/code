
class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        v = [part for part in path.split('/') if part and part != '.']

        s = []
        for part in v:
            if part == '..':
                if s:
                    s.pop()
            else:
                s.append(part)

        return '/' + '/'.join(s)
        
        
if __name__ == "__main__":
    s = Solution()

    assert s.simplifyPath("/home/") == '/home'
    assert s.simplifyPath("/a/./b/../../c/") == '/c'
    assert s.simplifyPath("/////home//foo/////") == '/home/foo'
    assert s.simplifyPath("/../") == '/'
    assert s.simplifyPath("/...") == '/...'
    assert s.simplifyPath("/..") == '/'
