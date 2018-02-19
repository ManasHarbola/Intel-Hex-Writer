#Creates a Intel Hex formatted Output.HEX file that can be used to program EEPROMs
#Written by: Manas Harbola
file_name = input("Enter the name of the file you want save to: ")
file_name += ".HEX"
hex_file = open(file_name, "w")
line_count = input("How many hex lines do you want to write? (enter in base 10) ")
line_count = int(line_count,10)


for lines in range(line_count):
    record_size = input("How many data bytes do you want to write in this line? (enter in base 10) ")
    record_size_counter = int(record_size,10)
    record_size = hex(int(record_size,10))
    record_size = record_size[2:].upper()
    if len(record_size) == 1:
        record_size = "0" + record_size
    hex_file.write(":")
    hex_file.write(record_size)
    
    addr = input("What is the starting address? (enter in base 10) ")
    addr_copy = int(addr,10)
    addr = hex(int(addr,10))
    addr = addr[2:].upper()   
    if len(addr) < 4:
        while len(addr) < 4:
            addr = "0" + addr
    print('\n')
    hex_file.write(addr)
    hex_file.write("00") #Record type value
    
    print(addr)
    byte_sum = "0"
    data_byte_sum = int(byte_sum,10)

    for bytes in range(record_size_counter):
        print("Enter byte ", bytes+1, " (in base 2): ")
        data_byte = input()
        data_byte_copy = int(data_byte,2)
        data_byte_sum += data_byte_copy
        data_byte = hex(int(data_byte,2))
        data_byte = data_byte[2:].upper()
        if len(data_byte) == 1:
            data_byte = "0" + data_byte
        hex_file.write(data_byte)
    total_sum = record_size_counter + addr_copy + data_byte_sum
    total_sum = bin(total_sum)
    total_sum = total_sum[2:]
    if (len(total_sum) % 4) != 0:
        pad = ""
        for extra in range(4-(len(total_sum)%4)):
            pad += "0"
        total_sum = pad + total_sum
    inversion = ""
    for bit in total_sum:
        if bit == "0":
            inversion += "1"
        elif bit == "1":
            inversion += "0"
    inversion = int(inversion,2)
    inversion += 1
    inversion = hex(inversion)[2:].upper()

    inversion = inversion[-2:]
    checksum = inversion
    #print(checksum)
    hex_file.write(checksum)
    hex_file.write("\n")

hex_file.write(":00000001FF")
hex_file.close()

print(file_name, "was successfully created!")
