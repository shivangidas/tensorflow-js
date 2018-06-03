from sklearn import tree
features = [[1,10],[2,20],[3,30],[1,11],[1,12],[3,31],[2,21]]
labels= [1,2,3,1,1,3,2]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print (clf.predict([[3,39]]))