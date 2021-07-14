import numpy as np
import izhikevich_cells as izh


class ibCell(izh.izhCell):
    def __init__(self,stimVal):
        # Define Neuron Parameters
        self.celltype='Intrinsically Bursting' # Regular spiking
        self.C=150
        self.vr=-75
        self.vt=-45
        self.k=1.2
        self.a=0.01
        self.b=5
        self.c=-56
        self.d=130
        self.vpeak=50
        self.stimVal = stimVal
    
        
        # Set up the simulation
        self.T=1000 # ms
        self.tau=1 # ms - time step
        self.n=int(np.round(self.T/self.tau))
        
        # Set up the stimulation
        self.I = np.concatenate((np.zeros((1,int(0.1*self.n))),self.stimVal*np.ones((1,int(0.01*self.n))),self.stimVal*.1*np.ones((1,int(0.89*self.n)))), axis=1)

        # Set up placeholders for my outputs from the simulation              
        self.v=self.vr*np.zeros((1,self.n))
        self.u=0*self.v


def createCell():
    myCell = ibCell(stimVal=4000)        
    myCell.simulate()
    izh.plotMyData(myCell)
    
if __name__=='__main__':
    createCell()


