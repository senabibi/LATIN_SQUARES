def rotate():
    square=int(input("Please input the order of square:"))
    left=int(input("Please input the top left number:"))
    print("The Latin Square")
    
    if 1<left<square:
        list=[]
        list2=[]
        all=[]
        for i in range(1,square+1):
            list.append(i)
        for i in range(len(list)):
            if list[i]==left:
                n=i 
        for i in range(0,n):
            first_elem=list[0]
            for j in range(0,len(list)-1):
                list[j]=list[j+1]
            list[len(list)-1]=first_elem 
        all+=list   
        for i in range(square):
            list
            for j in range(0,1):   
                first_elem=list[0]
                for k in range(0,len(list)-1):
                    list[k]=list[k+1]
                list[len(list)-1]=first_elem  
            all+=(list)
            
        for i in range(0,(len(all)-square),square):
            print(*all[i:i+5],sep=' ')    
    else:
        print("ERROR!!")

rotate()        
