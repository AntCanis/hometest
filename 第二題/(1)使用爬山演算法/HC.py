import random
import matplotlib.pyplot as plt

capacity = 750  #背包容量

#物品列表,每個物品表示為一組(重量,價值)
items = [[70, 135], [73, 139], [77, 149], [80, 150],[82,156],[87,163],[90,173],[94,184],[98,192],[106,201],[110,210],[113,214],[115,221],[118,229],[120,240]]

#---------------------------------------------------------------------------------------------
def spawn_number(x): #                                                用法:spawn_number(希望長度)
    return [random.randint(0, 1) for i in range(x)]#                  用途:隨機生成一串長度為x的二元串列,代表一個選取狀況 
#                                                                     !RETURN:一個二元串列
# -------------------------------------------------------------------------------------------
def find_neighbour(x):                        #用法:find_neighbour(二元串列)
    neighbor = x.copy()   #                   用途:隨機把一個0,1位置調換
    temp=random.randint(0,len(x)-1)           #!RETURN:一個新的串列,(原串列的鄰居)
    if neighbor[temp]==0:
        neighbor[temp]=1
    else:
        neighbor[temp]=0
        temp=random.randint(0,len(x)-1)
        neighbor[temp]=1
    return neighbor
#------------------------------------------------------------------------------------------------
# 計算解的評估函數值，即總價值
def price(x,item):
    value = 0       #代表價值                                      #用法:price(我的取法,物品以及對應重量價值的串列)
    weight = 0      #代表重量                                       用途:計算該拿法的價值,如有超重則價值為0
    for i in range(0,14):      #去檢測目前拿取狀況                   !RETURN:一個數字,該取法的價值
        if x[i]==1:             #如果有拿
            weight += items[i][0]     #加上重量以及價值
            value+=item[i][1]
           
          
        if weight > capacity:     #如果超重則價值就是0
            value = 0
       
    return value
#----------------------------------------------------------------------------------------------------
def HC_search(max_times):
    pick = spawn_number(15)    #隨機產生一種拿取方式
    best_solution = [1,0,1,0,1,0,1,1,1,0,0,0,0,1,1]#輸入最佳解  
    convergence = []              
    best_value = price(pick,items)
    convergence.append(best_value)                                                          #用法:HC_search(最大loop次數)
    for _ in range(0,max_times):#                                                            用途:使用HC去找最大價值
        neighbour = find_neighbour(pick)  #尋找鄰居(採變一個位元的方式)                         !RETURN:印出最佳解 最佳價值 匹配度
        neighbour_value = price(neighbour,items)#                                            
        if neighbour_value >=best_value: #如果鄰居的價值比目前所選更好
            pick = neighbour.copy()                     #把鄰居當成目前的最佳解
            best_value = neighbour_value
        convergence.append(best_value)
    diff = 0     #看和最佳解差多少位
    for i in range(0,14):
        if pick[i] == best_solution[i]:  
           diff +=1       #每一位相同就+1

    

    output = price(pick,items)
    print("計算出的最佳解為",pick)
    print("計算出來的最佳價值",output)
    print("與最佳解匹配度",round(diff/15,2))
    plot_convergence(convergence)
 #----------------------------------------------------------------------------------------------------       
def plot_convergence(convergence):
    plt.plot(convergence)
    plt.title('Convergence')
    plt.xlabel('Iteration')
    plt.ylabel('Best Value')
    plt.show()

#----------------------------------------------------------------------------------------------------主程式
HC_search(500)  #數字代表最大loop次數
