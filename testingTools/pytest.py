import fins.udp
import fins
import time

fins_instance = fins.udp.UDPFinsConnection()
fins_instance.connect('192.168.250.41')
fins_instance.dest_node_add =41  #node -> the last numbers of the ip addresss
fins_instance.srce_node_add =46

for i in range(100):
    # fins_instance.memory_area_write(fins.FinsPLCMemoryAreas().CIO_WORD,b'\x00\x02\x00',b'\x00\x00',1)
    mem_area = fins_instance.memory_area_read(fins.FinsPLCMemoryAreas().CIO_WORD,b'\x00\x02\x00',1)
    temp = str(mem_area) 

    print(temp[-3] + temp[-2])# always these last two chars that make up the target byte
    #val = bytes( hex"0x" + temp[-3] + temp[-2])
    #print (val)
    time.sleep(1)

    # fins_instance.memory_area_write(fins.FinsPLCMemoryAreas().CIO_WORD,b'\x00\x02\x00',b'\x00\x1f', 1)
    # mem_area = fins_instance.memory_area_read(fins.FinsPLCMemoryAreas().CIO_WORD,b'\x00\x02\x00')
    # print(mem_area)

    # time.sleep(1)

#def getVal():

   