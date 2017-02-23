str = "If monkeys like bananas, then I must be a monkey!"
print str.find('monkey')
print str.replace('monkey','alligator')
x = [2,54,-2,7,12,98]
print min(x)
print max(x)
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0:1]
print x[7:]
print x[0:1]+x[7:]
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
x.remove(-3)
x.remove(-2)
print x
list = []
list.append(-3)
list.append(-2)
print list
x.insert(0,list)
print x