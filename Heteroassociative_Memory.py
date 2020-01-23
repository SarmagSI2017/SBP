

data=[[-1,-1,1,-1,-1,1],[-1,-1,1,-1,1,-1],[-1,1,-1,-1,-1,1],[1,-1,1,-1,1,1],[-1,-1,1,1,-1,-1],[-1,1,-1,1,-1,-1],[1,-1,-1,1,-1,1],[-1,1,1,1,1,1]]
target=[[-1,1],[-1,1],[-1,1],[-1,1],[1,-1],[1,-1],[1,-1],[1,-1]]
w=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]


i=0
j=0
hasil1=0
hasil2=0

for t in range(8):
    print("----------------\ndata ke-",t+1)
    for j in range(6):
        for i in range(2):
            w[j][i]=w[j][i]+data[t][j]*target[t][i]
            print("bobot ke-",j+1,i+1,"adalah ",w[j][i])

#obana is maniger

print("\n\n\ncoba ditest, masukkan 6 inputan: ")
for j in range(6):
    masuk=int(input())
    hasil1=hasil1+masuk*w[j][0]
    hasil2=hasil2+masuk*w[j][1]
    
if hasil1>0:
    y_in1=1
elif hasil1<0:
    y_in1=-1
else:
    y_in1=0

if hasil2>0:
    y_in2=1
elif hasil2<0:
    y_in2=-1
else:
    y_in1=0

print("hasil yang didiapatkan pada bobot 1: ",hasil1,"----->(",y_in1,")")
print("hasil yang didiapatkan pada bobot 2: ",hasil2,"----->(",y_in2,")")