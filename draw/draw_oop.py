#2019.8.6mrc for rmsd
import matplotlib.pyplot as plt
import numpy as np
class draw():
    def __init__(self):
        pass
    def drawrmsd(self,filelist=[]):
        #user-defined:color,linewidth,linestyle,marker
        self.color = ['k','r','b','y','g','c','m','w']
        self.linewidth = ['0.5','1','2','2','2','2','2','2']
        self.linestyle = [':','-','--','-.',':','-','-','-']
        self.marker = ['.','None','v','.','+','*','','']
        self.filelist = filelist
        self.y = ["y"+str(i) for i in range(1,10)]
        self.x = ["x"+str(i) for i in range(1,10)]
        num = 0
        num2 = 0
        for filename in self.filelist:
            self.y[num] = np.loadtxt(filename)
            self.x[num] = list(range(1,len(self.y[num])+1))
            plt.plot(self.x[num],self.y[num],label=filename.split('.')[0],color=self.color[num],linewidth=self.linewidth[num],linestyle=self.linestyle[num],marker=self.marker[num])
            print (filename,self.color[num],self.linewidth[num],self.linestyle[num],self.marker[num])
            #define num2 for xlim and xticks
            if len(self.y[num]) > num2:
                num2 = len(self.y[num])      
            num += 1      
        plt.xlim((0,num2+1))
        #user-defined,change the number behind 'num2' and the range value to set up the x axis label
        plt.xticks(np.linspace(1,num2,11),[str(i)+'ns' for i in range(100,201,10)],fontsize=9)
        plt.xlabel('Time(ns)',fontsize=13)
        plt.ylabel('rmsd(Ans.)',fontsize=13)
        plt.title('RMSD show',fontsize=15)
        plt.legend()
        plt.show()

if __name__ == '__main__':
    draw_task1 = draw()
    draw_task1.drawrmsd(['backbone_rmsd.dat','cla_rmsd.dat','bcr_rmsd.dat'])
