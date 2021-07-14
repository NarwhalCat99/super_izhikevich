import numpy as np
import izhikevich_cells as izh


class chCell(izh.izhCell):
    def __init__(self,stimVal):
        # Define Neuron Parameters
        self.celltype='Chattering' # Regular spiking
        self.C=50
        self.vr=-60
        self.vt=-40
        self.k=1.5
        self.a=0.03
        self.b=1
        self.c=-40
        self.d=150
        self.vpeak=25
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
    myCell = chCell(stimVal=4000)        
    myCell.simulate()
    izh.plotMyData(myCell)
    
if __name__=='__main__':
    createCell()


