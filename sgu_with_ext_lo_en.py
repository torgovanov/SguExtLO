# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 10:14:07 2017

@author: TORGOVAN
"""

import visa

rm = visa.ResourceManager()

sgu = rm.open_resource('TCPIP0::169.254.152.50::inst0::INSTR')
ext_lo = rm.open_resource('TCPIP0::169.254.74.77::inst0::INSTR')


def sgu_set(settings):
    '''
	Power and frequency settings of SGU
	'''
	freq = settings[0]
    level = settings[1]
    sgu.write(':SOURce:FREQuency:CW %s' % freq)
    sgu.write(':SOURce:POWer %s' % level)
    sgu.query('*OPC?')
#    pass

def read_ext_lo_set():
	'''
	Get requirement settings from SGU
	'''
    freq = sgu.query('LOSCillator:FREQuency?')
    level = sgu.query('LOSCillator:POWer?')
    sgu.query('*OPC?')
    return [freq, level]
#    pass

def ext_lo_set():
	'''
	Set power and frequency on exteranal LO
	'''
    settings = read_ext_lo_set()
    freq = settings[0]
    level = settings[1]
    ext_lo.write(':SOURce:FREQuency:CW %s' % freq)
    ext_lo.write(':SOURce:POWer %s' % level)
    ext_lo.query('*OPC?')
    sgu.write(':SETTings:APPLy')
#    pass

def close_res():
    sgu.close()
    ext_lo.close()
#    pass

com=''
while com != 'q':
    print('q - quit')
    com = input('Enter f(Hz), p(dBm):')
    settings = com.split(',')
    if(len(settings) == 2):
        sgu_set(settings)
        ext_lo_set()
    else:
        if(settings == 'q'):
            close_res()
            break