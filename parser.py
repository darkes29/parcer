with open("habr.cer", "rb") as binary_file:
    # Read the whole file at once
    data = binary_file.read()
    print(data.hex())
    i = -1
    for letter in data:
        i += 1
        if hex(letter) == '0x30':
            print("SEQUENCE")
            a = data[i + 1] >> 7 & 1
            if a == 1:
                b = (str(bin(data[i + 1])))
                c = b
                print(int(c[-1])*(2^(0)))
                print(int(c[8]))
                print((int(c[8]))*(2^(0))+int(c[9])*(2^(1)))