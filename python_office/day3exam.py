

def tree(treeLayers,treeLeaf,treeTrunk):
    for i in range(treeLayers+1):
        print(' ' * (treeLayers -i)+ treeLeaf *(i *2-1))
    for a in range(treeTrunk):
        print(' ' * (treeLayers-1) + '|')


Layers = int(input('请输入树冠高度:'))

Leaf = input('请输入树叶类型：')

Trunk = int(input('请输入树干高度：'))

tree(Layers,Leaf,Trunk)


