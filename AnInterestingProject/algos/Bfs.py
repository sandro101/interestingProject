from AnInterestingProject.jcollection.TreeNode import build_some_tree, TreeNode


def bfs(tree):
    if tree is None:
        return
    print(tree.data + " visited")
    for child in tree.children:
        bfs(child)


##bfs(build_some_tree(), order='preorder')
##bfs(build_some_tree(), order='postorder')
##bfs(build_some_tree(), order='inorder')
##bfs_non_recursive_postorder(build_some_tree())
##bfs_non_recursive_preorder(build_some_tree())
