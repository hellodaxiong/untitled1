# coding=utf-8

ip_list = open('switch_ip.txt', 'r')
number_of_switch = len(ip_list.readlines())
number_of_switch_check = 'We have ' + str(number_of_switch) + ' switches need to check.'
print(number_of_switch_check)
ip_list.seek(0)

for switch in ip_list.readlines():
    switch_ip = switch.split()
    #print(switch_ip)
    print(switch_ip[0])
    print(switch_ip[1])