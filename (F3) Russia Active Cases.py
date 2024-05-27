
import matplotlib.pyplot as plt
import math
import numpy as np

plt.cla()
plt.clf()

n=250
gammar=1/14
gammarv=gammar
gammad=gammar/50
gammadv=gammad/5
Tvi=180
Tii=360
sigma=1/5.2
Rt=1.5
vi=0.9
   


for p in range(1,10):
        if p==1:
            e=0.92
            v=0.001

        elif p==2:
            e=0.92
            v=0.003

        elif p==3:
            e=0.92
            v=0.005

        elif p==4:
            e=0.72
            v=0.003

        elif p==5:
            e=0.72
            v=0.005

        elif p==6:
            e=0.72
            v=0.007

        elif p==7:
            e=0.55
            v=0.007

        elif p==8:
            e=0.55
            v=0.01

        else:
            e=0.55
            v=0.015


        for qq in range(5) :
            tau=qq/4

            R=0.2712
            D=0.0023
            Iv=0
            I=0.0184
            Sv=0
            Sn=0.2262
            E=I
            Ev=Iv
            S=1-R-D-I-Iv-Sv-Sn-E-Ev

            yA=[]
            x=[]        
                
            for i in range(n):
                
                
                beta=Rt*gammar
                betav=Rt*gammarv
                
                Si=S
                Svi=Sv
                Sni=Sn
                Ei=E
                Evi=Ev
                Ii=I
                Ivi=Iv
                Ri=R
                Di=D
                Ai=Ii+Ivi

                x.append(i)
                yA.append(Ai*100)        


                S= -beta*(Ii+Ivi)*Si - (1-tau)*v*Si + Si
                Sv= (1-tau)*(1-e*vi)*v*Si - betav*(Ii+Ivi)*Svi + 2*tau*v*Sni*0.1 + Svi
                Sn= (gammarv*Ivi+gammar*Ii)/Tii + ((1-tau)*e*vi*v*Si+2*tau*v*Sni*e*vi)/Tvi - betav*(Ii+Ivi)*Sni - 2*tau*v*Sni + Sni
                E= beta*(Ii+Ivi)*Si - sigma*Ei + Ei
                Ev= betav*(Ii+Ivi)*(Svi+Sni) - sigma*Evi + Evi
                I= sigma*Ei - (gammad + gammar)*Ii + Ii
                Iv=  sigma*Evi - (gammadv + gammarv)*Ivi + Ivi
                R= (1-tau)*e*vi*v*Si + 2*tau*v*Sni*e + gammar*Ii + gammarv*Ivi - ((1-tau)*e*vi*v*Si+2*tau*v*Sni*e*vi)/Tvi - (gammar*Ii+gammarv*Ivi)/Tii + Ri
                D= gammad*Ii + gammadv*Ivi + Di

                

            k=yA
            yaxis= 'Active Cases (%)'

            plt.subplot(3,3,p)
                        
            title=['tau=',str(tau)]
            a=''.join(title)
            plt.plot(x,k,label=a)

            plt.legend()
            plt.xlabel('Days')
            plt.ylabel(yaxis)

            plt.xlim((0,250))
            plt.ylim((0,3))

            
            b=['Rt=1.5',' / e=',str(e),' / v=',str(v)]
            b=''.join(b)
            plt.title(b)

plt.subplots_adjust(left=0.05, bottom=0.071, right=0.988, top=0.962, wspace=0.238, hspace=0.471)
plt.gcf().set_size_inches(16,8)

plt.show()

