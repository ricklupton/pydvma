# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 17:08:42 2018

@author: tb267
"""



class dataSet():
    def __init__(self,timeData=None,freqData=None,tfData=None,sonoData=None,settings=None,metaData=None):
        self.timeData = timeData
        self.freqData = freqData
        self.tfData   = tfData
        self.sonoData = sonoData
        self.settings = settings
        self.metaData = metaData
        
    def __repr__(self):
        text = '<dataSet class containing: '
        if repr(self.timeData) != 'None':
            text += repr(self.timeData)
        if repr(self.freqData) != 'None':
            text += repr(self.freqData)
        if repr(self.tfData) != 'None':
            text += repr(self.tfData)
        if repr(self.sonoData) != 'None':
            text += repr(self.sonoData)
        if repr(self.metaData) != 'None':
            text += repr(self.metaData)
        
        text += '>'
        return text
        
        
class timeData():
    def __init__(self,time_axis,time_data,settings):
        self.time_axis = time_axis
        self.time_data = time_data  
        self.settings = settings
        
    def __repr__(self):
        return "<timeData>"

        
class freqData():
    def __init__(self,freq_axis,freq_data,settings):
        self.freq_axis = freq_axis
        self.freq_data = freq_data
        self.settings = settings
        
    def __repr__(self):
        return "<freqData>"
        
class tfData():
    def __init__(self,freq_axis,tf_data,settings):
        self.freq_axis = freq_axis
        self.tf_data = tf_data
        self.settings = settings
        
    def __repr__(self):
        return "<tfData>"
        
class sonoData():
    def __init__(self,time_axis,freq_axis,sono_data,settings):
        self.time_axis = time_axis
        self.freq_axis = freq_axis
        self.sono_data = sono_data
        self.settings = settings
        
    def __repr__(self):
        return "<sonoData>"
        
class metaData():
    def __init__(self, timestamp=None, timestring=None, units=None, channel_cal_factors=None, tf_cal_factors = None):
        self.timestamp = timestamp
        self.timestring = timestring
        self.units = units
        self.channel_cal_factors = None
        self.tf_cal_factors = None
        
    def __repr__(self):
        return "<metaData>"