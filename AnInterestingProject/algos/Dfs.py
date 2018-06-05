from collections import deque

from AnInterestingProject.jcollection.TreeNode import build_some_tree, TreeNode


def dfs(tree, order=None):
    if tree is None:
        return
    if order == "preorder" and not tree.discovered:
        print(tree.data + " visited")
        tree.discovered = True
    for child in tree.children:
        dfs(child, order=order)
    if order == "postorder" and not tree.discovered:
        print(tree.data + " visited")
        tree.discovered = True


def dfs_non_recursive_preorder(tree):
    container = [tree]

    while container:
        tree = container.pop()
        if not tree.discovered:
            print(tree.data + " visited")
            tree.discovered = True
        for child in reversed(tree.children):
            if not child.discovered:
                container.append(child)


def dfs_non_recursive_postorder(tree):
    container = [tree]
    post_order = []

    while container:
        tree = container.pop()
        post_order.append(tree)
        for child in tree.children:
            if not child.discovered:
                container.append(child)
    for node in reversed(post_order):
        print(node.data + " visited")





##dfs(build_some_tree(), order='preorder')
##dfs(build_some_tree(), order='postorder')
##dfs(build_some_tree(), order='inorder')
##dfs_non_recursive_postorder(build_some_tree())
##dfs_non_recursive_preorder(build_some_tree())
