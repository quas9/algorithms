inf = open("job_Var11.in","r")
outf = open("job_Var11.out","w")
import numpy as np

n = inf.readline().split()
N = int(n[0])
start = int(n[1])

print(N,start)

D = np.zeros((N, N),dtype=int)
for i in range(N):
    row = list(map(str, inf.readline().split()))
    row = [99999999 if x == '*' else int(x) for x in row]
    row = row[:N]
    D[i] = row


P = np.zeros((N, N),dtype=int)
for i in range(N):
    for j in range(N):
        P[i][j] = i+1


for k in range(N):
        for i in range(N):
            for j in range(N):
                if (D[i][k] != 99999999 and D[k][j] != 99999999 and i!=j):
                    a = D[i][j]
                    D[i][j] = min(D[i][j],D[i][k] + D[k][j])
                    if(D[i][j] != a ):
                        P[i][j] = P[k][j]
        outf.write(f'{k+1}\n')
        outf.write("D:\n")
        for i in range(N):
            for j in range(N):
                if (D[i][j] != 99999999):
                    outf.write(f'{D[i][j]} ')
                else:
                    outf.write("* ")
            outf.write("\n")
        outf.write("P:\n")
        np.savetxt(outf, P, fmt='%d')


inf.close()
outf.close()















