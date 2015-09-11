__author__ = 'drzzh'


'''
    /../ 返回上一级目录
    /./ 当前目录
    用一个stack记录上一级目录，
    遇到/../就pop一个
    同时一定要用split('/')，能省很多事

    /.../这是个合法目录
'''

class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        folders = []
        for c in path.split('/'):
            if not c:
                continue
            elif c == '.':
                continue
            elif c == '..':
                if len(folders) != 0:
                    folders.pop()
            else:
                folders.append(c)

        return '/' + '/'.join(folders)
