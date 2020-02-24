import IPluginBitalino
from datetime import datetime
import numpy as np

class PluginCsv(IPluginBitalino.IPluginBitalino):
    def activate(self):
        self.formatting_string = "{:2.0f} " * 5 + "{:8.3f} " * len(self.acq_channels)
        print("Csv activated")
        if(len(self.args)==0):
            now = datetime.now()
            time = now.strftime("%H:%M:%S")
            self.f = open(time, "a")
            
        else: 
            self.f = open(self.args[0],"a")
            print(self.args)

    # called with each set of samples received from Bitalino
    def __call__(self, samples):
        
        np.savetxt(self.f, samples, delimiter=',')
        

    def deactivate(self):
        self.f.close()