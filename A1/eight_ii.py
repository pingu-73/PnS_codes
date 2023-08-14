import random
import matplotlib.pyplot as plt

dic = {"A":["B","D"],"B":["A","C","D"],"C":["B","E"],"D":["A","B","E"],"E":["C","D"]}
lis = ["A","B","C","D","E"]
count = {"A":0,"B":0,"C":0,"D":0,"E":0}
for i in range(1000):
    prev = random.choice(lis)
    for i in range(20):
        cur = random.choice(dic[prev])
        count[cur] +=1
        prev = cur

list1 = []
for i in range(len(dic)):
    list1.append(count[lis[i]])

list2 = sorted(list1,reverse=True)

node_list = []
for i in range(len(list2)):
    for key,value in count.items():
        if (value==list2[i]):
            print(key,list2[i])
            node_list.append(key)

plt.bar(node_list,list2)
plt.xlabel('Nodes')
plt.ylabel('No of times Nodes is visited')
plt.show()
