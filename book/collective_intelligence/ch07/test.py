#! /usr/bin/.env python2

import treepredict

print "Gini impurity\n"
print treepredict.giniimpurity(treepredict.my_data)

print "\n"

print "treepredict.entropy\n"
print treepredict.entropy(treepredict.my_data)

print "\n"

set1, set2 = treepredict.divideset(treepredict.my_data, 2, 'yes')

print "Gini impurity\n"
print treepredict.giniimpurity(set1)
print "treepredict.entropy\n"
print treepredict.entropy(set1)

print '\n'
tree = treepredict.buildtree(treepredict.my_data)
print 'tree: ', tree

print '\n'

print 'classify: ', treepredict.classify(['(direct)', 'USA', 'yes', 5], tree)
