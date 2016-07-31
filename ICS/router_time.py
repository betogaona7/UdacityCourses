""" How long does the data spend at the routers? """

# Information given in question

total_time = 75 #milliseconds traceroute, round trip Birminghas -> Sundsvall
one_way_distance = 2500.0 # Km, Sirmingham -> Sundvall
optic_speed = 200000 # Km/s
ms_per_second = 1000 # Conversion from ms to second (ms/sec)

#Calculations
time_on_the_wires = 2*one_way_distance/optic_speed*ms_per_second # [km]/[km/sec]*[ms/s]
total_time_at_routers = total_time - time_on_the_wires
print (total_time_at_routers)

