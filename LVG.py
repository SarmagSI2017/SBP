import math

alpha=0.05

w=[[1,0,0,0,1,0],[0,1,1,1,1,0]]
x=[[0,0,1,0,0,1],[0,0,1,0,1,0],[0,1,0,0,0,1],[1,0,1,0,1,1],[0,0,1,1,0,0],[0,1,0,1,0,0],[1,0,0,1,0,1],[0,1,1,1,1,1]]
t=[0,0,0,0,1,1,1,1]
banding1=0
banding2=0
ulang=0
epoh=0
masuk=0
while (epoh<10):
    print("----------\nepoh ke-",epoh+1,"\n---------")
    for ulang in range (8):
        print("----------\ndata ke-",ulang+1,"\n---------")
        for i in range(6):
            banding1=banding1+(x[ulang][i]-w[0][i])**2
            banding2=banding2+(x[ulang][i]-w[1][i])**2
            

        banding1=math.sqrt(banding1)
        banding2=math.sqrt(banding2)
        print(banding1,banding2)

        if banding1<= banding2:
            pilih=0
        else:
            pilih=1
        if ulang ==6:
            print(w[pilih][j],x[ulang][j])
        if pilih==t[ulang]:
            for j in range(6):
                w[pilih][j]=w[pilih][j]+alpha*(x[ulang][j]-w[pilih][j])
                w[pilih][j]=round(w[pilih][j],4)
                print( w[pilih][j])
        else:
            for j in range(6):
                w[pilih][j]=w[pilih][j]-alpha*(x[ulang][j]-w[pilih][j])
                w[pilih][j]=round(w[pilih][j],4)
                print( w[pilih][j])

        banding1=0
        banding2=0
    alpha=alpha-0.1*alpha
    epoh+=1

print("w1 yang didapat: ",w[0])
print("w2 yang didapat: ",w[1])
#tolong dihapus maniger
print("\n\ntahap mengecek, masukkin 6 input: ")
for i in range(6):
    masuk=int(input())
    banding1=banding1+(masuk-w[0][i])**2
    banding2=banding2+(masuk-w[1][i])**2
            

banding1=math.sqrt(banding1)
banding2=math.sqrt(banding2)
print(banding1,banding2)

if banding1<= banding2:
    pilih=0
else:
    pilih=1

print("input termasuk kelas : ",pilih+1)












