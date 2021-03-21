import numpy as np
L= int(input('L'))
N= int(input('N'))
T= int(input('T'))
p= int(input('Pacient number'))
pmariz=float(input('percentage of infection'))
ts=int(input('ts'))
counter=0


base=np.zeros((L,L),dtype=float)
randmake =np.random.randint(L, size=(2, N))
randmakep =np.random.randint(L, size=(2, p))
for i in range (0,N):#random maker
    base[randmake[0][i]][randmake[1][i]]=1
for i in range (0,p):#random maker
    base[randmakep[0][i]][randmakep[1][i]]=2
    


for i in range (0,T):
    
  
#################################################################################random walk     
     for x in range (1,L-2):#base base 
        for y in range (1,L-2):
            if base[x][y] > 0.95:
                
                direction = np.random.randint(low=0,high=3)
                if direction ==0 and base[x-1][y]==0 :
                    base[x-1][y]=base[x][y]
                    base[x][y]=0
                elif direction ==1 and base[x+1][y]==0 :
                    base[x+1][y]=base[x][y]
                    base[x][y]=0
                elif direction ==2 and base[x][y-1]==0 :
                    base[x][y-1]=base[x][y]
                    base[x][y]=0
                elif direction ==3 and base[x][y+1]==0 :
                    base[x][y+1]=base[x][y]
                    base[x][y]=0
            
     for y in range (1,L-2):#base up 
            if base[0][y] >0.95:
                direction = np.random.randint(low=0,high=2)
                if direction ==0 and base[1][y]==0 :
                    base[1][y]=base[0][y]
                    base[0][y]=0
                elif direction ==1 and base[x][y-1]==0:
                    base[x][y-1]=base[0][y]
                    base[0][y]=0
                elif direction ==2 and base[x][y+1]==0 :
                    base[x][y+1]=base[0][y]
                    base[0][y]=0
     for y in range (1,L-2):#base down 
            if base[L-1][y] >0.95:
                
                direction = np.random.randint(low=0,high=2)
                if direction ==0 and base[L-2][y]==0:
                    base[L-2][y]=base[L-1][y]
                    base[L-1][y]=0
                elif direction ==1 and base[x][y-1]==0:
                    base[x][y-1]=base[L-1][y]
                    base[L-1][y]=0
                elif direction ==2 and base[x][y+1]==0 :
                    base[x][y+1]=base[L-1][y]
                    base[L-1][y]=0
     for x in range (1,L-2):#base left 
            if base[x][0] >0.95:
                
                direction = np.random.randint(low=0,high=2)
                if direction ==0 and base[x][1]==0 :
                    base[x][1]=base[x][0]
                    base[x][0]=0
                elif direction ==1 and base[x-1][0]==0:
                    base[x-1][0]=base[x][0]
                    base[x][0]=0
                elif direction ==2 and base[x+1][0]==0 :
                    base[x+1][0]=base[x][0]
                    base[x][0]=0
     for x in range (1,L-2):#base right 
            if base[x][L-1] >0.95:
                
                direction = np.random.randint(low=0,high=2)
                if direction ==0 and base[x][L-1]==0:
                    base[x][L-2]=base[x][L-1]
                    base[x][L-1]=0
                elif direction ==1 and base[x-1][L-1]==0 :
                    base[x-1][L-1]=base[x][L-1]
                    base[x][L-1]=0
                elif direction ==2 and base[x+1][L-1]==0 :
                    base[x+1][L-1]=base[x][L-1]
                    base[x][L-1]=0
     if base[0][0]>0.95:#corner LU
        
        direction = np.random.randint(low=0,high=1)
        if direction ==0 and base[0][1]==0:
                    base[0][1]=base[0][0]
                    base[0][0]=0
        elif direction ==1 and base[1][0]==0 :
                    base[1][0]=base[0][0]
                    base[0][0]=0
     if base[L-1][0]>0.95: #corner LD
        
        direction = np.random.randint(low=0,high=1)
        if direction ==0 and base[L-2][0]==0  :
                    base[L-2][0]=base[L-1][0]
                    base[L-1][0]=0
        elif direction ==1 and base[L-1][1]==0 :
                    base[L-1][1]=base[L-1][0]
                    base[L-1][0]=0
    
     if base[0][L-1]>0.95:#cornr RU
        
        direction = np.random.randint(low=0,high=1)
        if direction ==0 and base[0][L-2]==0 :
                    base[0][L-2]=base[0][L-1]
                    base[0][L-1]=0
        elif direction ==1 and base[1][L-1]==0 :
                    base[1][L-1]=base[0][L-1]
                    base[0][L-1]=0
     if base[L-1][L-1]>0.95: #corner RD
            
        direction = np.random.randint(low=0,high=1)
        if direction ==0 and base[L-2][L-1]==0 :
                    base[L-2][L-1]=base[L-1][L-1]
                    base[L-1][L-1]=0
        elif direction ==1 and base[L-1][L-2]==0 :
                    base[L-1][L-2]=base[L-1][L-1]
                    base[L-1][L-1]=0
    #############################################################################random walk
  #############################################################################spread
     for x in range (1,L-2):#base base 
        for y in range (1,L-2):
            percentage = np.random.random()
            if int(base[x][y]) ==2 and percentage<=p:
                
                
                if int(base[x-1][y])==1.0:
                    base[x-1][y]=2 
                if int(base[x+1][y])==1.0:
                    base[x+1][y]=2
                if int(base[x][y-1])==1.0:
                    base[x][y-1]=2
                if int(base[x][y+1])==1.0:
                    base[x][y+1]=2
        
     for y in range (1,L-2):#base up 
            percentage = np.random.random()
            if int(base[0][y])==2 and percentage<=p:
                
                if base[1][y]==1.0:
                    base[1][y]=2
                if base[x][y-1]==1.0:
                    base[x][y-1]=2
                if base[x][y+1]==1.0:
                    base[x][y+1]=2
            
     for y in range (1,L-2):#base down 
            percentage = np.random.random()
            if int(base[L-1][y]) ==2 and percentage<=p:
                
                
                if base[L-2][y]==1.0:
                    base[L-2][y]=2
                if base[x][y-1]==1.0:
                    base[x][y-1]=2
                if base[x][y+1]==1.0:
                    base[x][y+1]=2
            
     for x in range (1,L-2):#base left 
            percentage = np.random.random()
            if int(base[x][0])==2 and percentage<=p:
                
            
                if base[x][1]==1.0:
                    base[x][1]=2
                if base[x-1][0]==1.0:
                    base[x-1][0]=2
                if base[x+1][0]==1.0:
                    base[x+1][0]=2                
        
     for x in range (1,L-2):#base right
            percentage = np.random.random()
            if int(base[x][L-1])==2 and percentage<p:
                
                
                if base[x][L-2]==1.0:
                    base[x][L-2]=2
                if base[x-1][L-1]==1.0:
                    base[x-1][L-1]=2
                if base[x+1][L-1]==1.0:
                    base[x+1][L-1]=2
            
     if int(base[0][0])==2:#corner LU
        percentage = np.random.random()
        
        
        if base[0][1]==1.0 and percentage<=p:
                    base[0][1]=2
        if base[1][0]==1.0 and percentage<=p:
                    base[1][0]=2
        
     if int(base[L-1][0])==2: #corner LD
        percentage = np.random.random()
        
        if base[L-2][0]==1.0 and percentage<=p:
                    base[L-2][0]=2
        if base[L-1][1]==1.0 and percentage<=p:
                    base[L-1][1]=2
        
     if int(base[0][L-1])==2:#cornr RU
        percentage = np.random.random()
        
        if base[0][L-2]==1.0 and percentage<p:
                    base[0][L-2]=2
        if base[1][L-1]==1.0 and percentage<=p:
                    base[1][L-1]=2
        
     if int(base[L-1][L-1])==2: #corner RD
        percentage = np.random.random()    
        
        if base[L-2][L-1]==1.0 and percentage<=p:
                    base[L-2][L-1]=2
        if base[L-1][L-2]==1.0 and percentage<p:
                    base[L-1][L-2]=2  
        
    ############################################################################spread
    
    #############################################################################add time step
   # for s in range (0,ts):
     for x in range (0,L-1) :
        for y in range (0,L-1):
            if base[x][y]>3:
               base[x][y]=1
            if int(base[x][y])==2:
                base[x][y]=base[x][y]+(1.0/ts)
    ##################################################################################time step
    

    
   
   
    
    
for x in range (0,L-1):
     for y in range (0,L-1):
         if int(base[x][y])>=2:
             counter= counter+1
print(counter)