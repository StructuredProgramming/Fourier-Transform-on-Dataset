import numpy as np
import matplotlib.pyplot as plt

with open('x_y.txt', 'r') as f: 
    lines = f.readlines()
for line in lines:  
        x, y = line.split('=')[0], line.split('=')[1]
        x, y = x.split(' '), y.split(' ')
        x = [i for i in x if i]
        y = [i for i in y if i]
        x[0] = x[0][1:]
        y[0] = y[0][1:]
        x[-1] = x[-1][:-1]
        y[-1] = y[-1][:-1]

        x = [float(i) for i in x if i]
        y = [float(i) for i in y if i]
        
        S=np.zeros(360, dtype='complex_')
        for i in range(360):
            for k in range(360):
                a=x[k]
                b=y[k]
                tmp = ((-2j*np.pi*i*k)) /360
                S[i] += (complex(a,b)) * np.exp(tmp)
            S[i]=S[i]/360
        G=np.zeros(360, dtype='complex_')
        xfinal=np.zeros(360)
        yfinal=np.zeros(360)
        for i in range(360):
            k=0
            tmp = ((2j*np.pi*i*k)) /360
            G[i]+=S[k]*np.exp(tmp)
            k=359
            tmp = ((2j*np.pi*i*k)) /360
            G[i]+=S[k]*np.exp(tmp)
            k=1
            tmp = ((2j*np.pi*i*k)) /360
            G[i]+=S[k]*np.exp(tmp)
            k=358
            tmp = ((2j*np.pi*i*k)) /360
            G[i]+=S[k]*np.exp(tmp)
            k=2
            tmp = ((2j*np.pi*i*k)) /360
            G[i]+=S[k]*np.exp(tmp)
            k=357
            tmp = ((2j*np.pi*i*k)) /360
            G[i]+=S[k]*np.exp(tmp)
            k=3
            tmp = ((2j*np.pi*i*k)) /360
            G[i]+=S[k]*np.exp(tmp)
            k=356
            tmp = ((2j*np.pi*i*k)) /360
            G[i]+=S[k]*np.exp(tmp)
            k=4
            tmp = ((2j*np.pi*i*k)) /360
            G[i]+=S[k]*np.exp(tmp)
            k=355
            tmp = ((2j*np.pi*i*k)) /360
            G[i]+=S[k]*np.exp(tmp)
            k=5
            tmp = ((2j*np.pi*i*k)) /360
            G[i]+=S[k]*np.exp(tmp)
            xfinal[i]=np.real(G[i])
            yfinal[i]=np.imag(G[i])

        plt.plot(x,y,color="red")
        plt.show()    
        plt.plot(xfinal,yfinal,color="green")
        plt.show()

       
        
