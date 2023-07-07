#transient simulation:
resistance = 730000000000 #resistance of the RTP crystal, measured in ohms
capacitance = 0.0000000000033 #capacitance of the RTP crystal, measured in farads
nominal_voltage = 3000 #nominal voltage of the power circuitry, meansured in volts
nominal_frequency = 500000 #Roughly double transient frequency? #nominal frequency of the power circuitry, measured in hertz
voltage_ripple = 600 #voltage ripple of the power circuitry, measured in volts
switching_frequency = 1920 #1920 #switching frequency of the power circuitry, measured in hertz

#trigger pulse:
trigger_rise_time = 0
trigger_duty_cycle = 0
trigger_latency = 0

#general:
num_of_modules = 1 #number of simulated voltage transistions
time_resolution = 1 #resolution for the x-axis on the graph, measured in microseconds

BCM_resolution = 1 #resolution with which the wave is generated as "measured" by the BCM, measured in radians
detector_resolution = 0.1 #resolution with which the wave is generated as "measured" by the detector, measured in radians

#temp:
transient_voltage = 14400 #volts
transient_rise_time = 0.25 #microseconds