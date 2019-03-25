#f = open("a_example.txt","r")
#f = open("b_lovely_landscapes.txt","r")
#f = open("c_memorable_moments.txt","r")
#f = open("d_pet_pictures.txt","r")
f = open("e_shiny_selfies.txt","r")
data = f.read()
d = data.split("\n")
t=int(d[0])

d=d[1:]
index = [i for i in range(t)]
#print(index)
orientations = []
tags = []
for i in range(t):
    linesplit = d[i]
    terms = linesplit.split(" ")
    orientation = terms[0]
    nx = terms[1]
    extras = terms[2:]
    orientations.append(orientation)
    tags.append(extras)

#print(orientations)
#print(tags)

new_indexes = []
new_tags = []


#Putting horizontal clips together
for i,j in enumerate(orientations):
    if(j=='H'):
        new_indexes.append(i)
        new_tags.append(tags[i])
#print(new_tags)


verticals = []
for i,j in enumerate(orientations):
    if(j=='V'):
        verticals.append(i)

#print(verticals)

#Vertical Mixing
templist = verticals
jx=len(templist)
while(len(templist)>0):
    jx-=1
    if(jx==0): break
    i=templist[0]
    count = 0
    newtags={}
    newV=[]
    for j in templist:
        if(i!=j):
            if(len(set(tags[i]).intersection(set(tags[j])))>count):
                count = len(set(tags[i]).intersection(set(tags[j])))
                newtags = set(tags[i]).union(set(tags[j]))
                newV=[]
                newV.append(i)
                newV.append(j)
    if(len(newV)>1):
        new_indexes.append(newV)
        new_tags.append(list(newtags))
        templist.remove(newV[0])
        templist.remove(newV[1])
#print(templist)

printing_order = []

#print(new_tags)
#print(new_indexes)


#Final Mixing
templist = [i for i in range(len(new_tags))]
printing_order.append(0)
jx=len(templist)
i=templist[0]
templist.remove(0)
while(len(templist)>0):
    jx-=1
    if(jx==0): break
    count = 0
    newtags={}
    nextP = 0
    for j in templist:
        if(i!=j):
            if(len(set(new_tags[i]).intersection(set(new_tags[j])))>count):
                count = len(set(new_tags[i]).intersection(set(new_tags[j])))
                nextP = j
    if(count==0 or nextP==0):
        break
    i=nextP
    templist.remove(i)
    printing_order.append(nextP)
#print(printing_order)

#for i in range(len(printing_order)):
#    x=new_indexes[printing_order[i]]
    #print(x)

#f1 = open("output_a.txt","w")
#f1 = open("output_b.txt","w")
#f1 = open("output_c.txt","w")
#f1 = open("output_d.txt","w")
f1 = open("output_e.txt","w")

f1.write(str(len(printing_order)))
f1.write("\n")
for i in range(len(printing_order)):
    x=new_indexes[printing_order[i]]
    if(isinstance(x,int)):
        f1.write(str(x))
        f1.write("\n")
    else:
        f1.write(str(x[0]))
        f1.write(" ")
        f1.write(str(x[1]))
        f1.write("\n")
f1.close()