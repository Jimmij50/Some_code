import numpy as np 
import copy
def com(a,b):
    if(a<=b):
        return a;
    else:
        return b;
def memcal(a,b):#隶属度矩阵计算
    ans0=[]
    ans1=[]
    for j in range(b.shape[1]):
        for i in range(a.shape[1]):
            ans0.append(com(b[i,j],a[0,i]))
        ans00=np.array(ans0)
        ans=np.max(ans00)
        ans1.append(ans)
        ans0.clear()
    anss=np.array(ans1)
    return anss




if __name__ == "__main__":
    #A1=np.array([[0.2,0.1,0.5,0.2]])
    A1=np.array([[0.125,0.075,0.15,0.15,0.15,0.125,0.125,0.1]])
    #R=np.array([[0.57,0.29,0.14,0,0],[0.86,0.14,0,0,0],[0,0,0.71,0.14,0.14],[0.29,0.29,0.14,0.14,0.14]])
    R=np.array([[0.8,0.71,0.71,0.71,0.75],[0.57,0.5,0.83,0.83,0.53],[0.143,0.143,0.67,0.67,0.67],[0.14,0.14,0.14,0.14,0.14],[0.83,0.67,0.45,0.1,0.4],[1.0,0.67,1.0,0.83,0.67],[0.68,0.68,0.68,0.68,0.68],[0.43,0.48,0.57,0.97,0.40]])
    print(A1.shape)
    print(R.shape)
    ans=memcal(A1,R)
    print(ans)

###########################################################################################
## string with number 带有符号的矩阵计算
class swn():
    # def __init__(self):
    #     self.num=1
    #     self.str=None 
    def __init__(self,num_,str_):
        self.num=num_
        self.str=str_
def cmul(a,b):
    if b.shape[0]!=a.shape[1]:
        print("EORROR: the dimensions of matrix do not match in function \"cmul\" ")
        exit()
    l1=[]
    l2=[]
    ans=swn(0,"")
    for b_c in range(b.shape[1]): 
        for a_r in range(a.shape[0]):
            for a_c in range(a.shape[1]):
                temp_num=a[a_r,a_c].num*b[a_c,b_c].num
                temp=a[a_r,a_c].str+b[a_c,b_c].str
                ans.num=1
                if(ans.str==""):
                    if temp_num==0:
                        ans.str+=str(0)
                    else:
                       
                        ans.str+=str(temp_num)+"("+ temp +")" #防止第一位出现加号
                else:
                    if temp_num==0:
                        pass
                    else:
                        if(temp_num<0):
                            ans.str+=str(temp_num)+"("+temp+")"
                        else:
                            ans.str= ans.str+"+"+str(temp_num)+"("+temp+")"
            if ans.str=="0":
                ans.num=0
            l1.append(ans)
            ans=swn(0,"")
        
        l2.append(copy.deepcopy(l1)) #矩阵运算中这个是是个列，但是加入到list变成了一个行，所以输出要转置一下。
        l1.clear()
    return np.transpose(np.array(l2))
# def tran(a):
#     for i in range(a.shape[0]):
#         for j in range(a.shape[1]):
#             if()

# MA=np.array([[swn(1,"a"),swn(1,"b")],[swn(2,""),swn(3,"")]])
# MB=np.array([[swn(1,"a"),swn(1,"b")],[swn(2,""),swn(3,"")]])
def show_swn(ans):
    for i in range(ans.shape[0]):
        for j in range(ans.shape[1]):
            print(ans[i,j].str,end="") 
            print(" ",end="") 
            print(" ",end="")
        print("\n")



if __name__ == "__main__":
    MA=np.array([
        [swn(1,"r_11"),swn(1,"r_12"),swn(1,"r_13"),swn(1,"p_x")],
        [swn(1,"r_21"),swn(1,"r_22"),swn(1,"r_23"),swn(1,"p_y")],
        [swn(1,"r_31"),swn(1,"r_32"),swn(1,"r_33"),swn(1,"p_z")],
        [swn(0,""),swn(0,""),swn(0,""),swn(1,"")]            
    ])
    MB=np.array([
                [swn(0,"")],
                [swn(0,"")],
                [swn(0,"")],
                [swn(1,"")],
                ])
    ans=cmul(MA,MB)
    print(MA.shape)
    print(MB.shape)
    print (ans.shape)
    show_swn(ans)
########################################
#skew_symetric #generally the input is 3x1 vector
def negetive_swn(a):
    ans=swn(a.num*-1,a.str)
    return ans
def list2array(a):
    l1=[]
    l2=[]
    for i in a:
        l1.append(i)
        l2.append(copy.deepcopy(l1)) 
        l1.clear()
    return np.array(l2)
def skew_s(a):
    #a=list2array(in)
    ans=np.array([
        [swn(0,""),negetive_swn(a[2,0]),a[1,0]],
        [a[2,0],swn(0,""),negetive_swn(a[0,0])],
        [negetive_swn(a[1,0]),a[0,0],swn(0,"")]
    ])
    # ans=np.array([
    #         [swn(0,""),negetive_swn(a[2,0]),a[1,0]],
    #         [a[2,0],swn(0,""),negetive_swn(a[0,0])],
    #         [negetive_swn(a[1,0]),a[0,0],swn(0,"")]     
    #   ])
    i_m=gen_i(ans.shape[0])
    anss=cmul(ans,i_m)
    return ans #需要称一下单位矩阵 才能正确输出 
def gen_i(n):
    l1=[]
    l2=[]
    for i in range(3):
        for j in range(3):
            if j==i:
                l1.append(swn(1,""))
            else:
                l1.append(swn(0,""))
        l2.append(copy.deepcopy(l1)) 
        l1.clear()
    temp=np.array(l2)
    return temp