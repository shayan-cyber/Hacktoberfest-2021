class square:
    def update(self):
        dict=({1:[1,2,3],2:[4,5],3:[6,8]})
        print("Dictionary is:",dict)
        l={}
        k=[]
        v=[]
        for i in dict.keys():
            k.append(str(i)+"_mod")
        for i in dict.values():
            v.append(i)
        for j in range(0,len(v)):
            t=[k**2 for k in v[j]]
            l[k[j]]=t
        dict.update(l)
        print("Updated dictionary is:",dict)
ob=square()
ob.update()
