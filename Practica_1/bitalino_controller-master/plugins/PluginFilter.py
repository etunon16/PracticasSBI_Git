# -*- coding: utf-8 -*-

import IPluginBitalino
import numpy as np
import scipy.signal as sig

class PluginFilter(IPluginBitalino.IPluginBitalino):

    def activate(self):
       
        f0 = 50.0
        Q = 30.0
        w0 = f0/(self.sampling_rate/2)
        self.b, self.a = sig.iirnotch(w0, Q)
        self.z_i = np.zeros(max(len(self.a), len(self.b))-1)
        
    def __call__(self, samples):
        
        emg = samples[:,-1]
        emg,z_f = sig.lfilter(self.b,self.a,emg, zi = self.z_i)
        self.z_i = z_f 
        