import os
from time import time
import binascii
import math
import os.path
import sys

# @Author Jurijus Pacalovas
# Get the name of the current script

if os.path.basename(sys.argv[0]) != "Shora_Yura.py":
    sys.exit("This is not 'Shora_Yura.py'.")

print("The script 'Shora_Yura.py' is currently running.")


class compression:
    def cryptograpy_compression4(self):

        self.name = "Created Quantum Software: Jurijus pacalovas"
        print(self.name)

        N5 = 1

        if N5 == 1:

            Clear = ""

         
            
            


            name = input("What is name of file input? ")
            
            compress_extract = input("compress: 1 extract: 2? ")
            if compress_extract=="1":
                i=1
            elif compress_extract=="2":
                i=2
            else:
                print("Incorrect letter select!")
                raise SystemExit

            long_21 = len(name)

            name_f = name[long_21 - 2 :]
            if i ==2:

                i = 2

            else:

                i = 1
            

            # print(i)
            if os.path.exists(name):

                print("Path is exists!")

            else:

                print("Path is not exists!")

                raise SystemExit

            x = 0
            C1 = 1
            x1 = 0
            x2 = 0
            x3 = 0
            X2 = 0
            C1 = 0
            C2 = 0
            C3 = 0
            C4 = 0
            ZEROS_ONE_1 = ""
            Circle_times = 0
            Circle_times2 = 1
            Circle_times3 = 0
            CB = -1
            Times1 = 0
            Tc = 0
            x = time()
            File_information6_Times2_1 = 0
            name_2 = name
            Long_Change = len(name_2)
            compress_or_not_compress = 1

            File_information6_Times3 = 0

            if i == 2:

                C = 1

            Long_Change = len(name_2)
            s = ""
            File_information5 = ""
            File_information5_2 = ""
            Clear = ""
            Translate_info_Decimal = ""
            D = 0
            long_name = len(name)
            with open(name, "rb") as binary_file:

                data = binary_file.read()
                s = str(data)

                long_11 = len(data)

                long_17 = len(data)

                if long_17 == 0:

                    raise SystemExit

                END_working = 0

                File_information6_Times2 = 0

                File_information5_24 = ""

                INFO18 = ""

                File_information5_29 = ""

                SpinS = 0

                while END_working < 10:

                    File_information6_Times3 = File_information6_Times3 + 1

                    D = 1

                    if D == 1:

                        if File_information6_Times3 == 1:

                            INFO = bin(int(binascii.hexlify(data), 16))[
                                2:
                            ]  # data to binary

                            long_1 = len(INFO)

                            long_11 = len(data)
                            Shora_Yura_long=long_11

                            count_bits = (long_11 * 8) - long_1

                            z = 0

                            if count_bits != 0:

                                while z < count_bits:

                                    INFO = "0" + INFO

                                    z = z + 1

                            Check = INFO

                            File_information5_2 = INFO

                            Extact = File_information5_2

                        long_13 = len(File_information5_2)

                        long_12 = len(File_information5_2)

                        
                        	

                        if i == 1:

                            Ex = 1

                            if Ex == 1:

                                Extract1 = 0

                                Find = 0

                                En = 3

                                Ci = 1

                                M1 = 0

                                Row1 = 0

                                input_string = ""

                                C1 = ""

                                Row = 0

                                I8 = INFO

                                W3 = ""

                                W4 = ""

                                block = 0

                                IF1 = ""

                                long_F = len(I8)

                                # print(long_F)

                                FC = 0

                                IF2 = ""

                                Z7 = 0

                                CZ = 0

                                if Circle_times == 0:

                                    SINFO = ""

                                    TUPLE = INFO

                                if Circle_times == 0:

                                    SINFO = INFO

                                long_bits_after = 0
                                long_bits_after_b = 0
                                long_bits_before = 0
                                times_compress = 0
                                long_after_bits = 0
                                long_bits_after_b_1 = 0
                                J = 1
                                long_F1 = long_F
                                long_one_time = long_F1
                                stop_compress = 0
                                while stop_compress != 1:
                                    block = 0
                                    long_after_bits = len(INFO)
                                    Transform = INFO
                                    long_F = len(I8)
                                    T10 = ""
                                    c_c = 0
                                    T15=""
                                    T16=""
                                    Transform="1"+Transform
                                    T8 = INFO
                                    Shora_decode=1
                                    if Shora_decode==1:
                                        # Input product
                                            try:
                                                product = int(Transform,2)
                                                #print(product)
                                                
                                                if product <= 0:
                                                    raise ValueError("Product must be a positive integer greater than 0.")
                                                
                                                # Step 1: Factorize the product into byte values (0-255)
                                                factors = []
                                                for i in range(2, 256):
                                                    while product % i == 0:
                                                        factors.append(i)
                                                        product //= i
                                                    if product == 1:
                                                        break  # Exit early if fully factored
                                            
                                                # If product is still greater than 1 and less than 256, it should be a valid byte
                                                if 1 < product < 256:
                                                    factors.append(product)
                                            
                                                # Step 2: Print the results
                                                #print(f"Input Product: {product}")
                                                #print(f"Factors (decoded byte values): {factors}")
                                            
                                                # Step 3: Confirm the product
                                                calculated_product = 1
                                                for byte in factors:
                                                    calculated_product *= byte
                                                #print(f"Product of Byte Values: {calculated_product}")
                                            
                                                # Step 4: Decode the byte values into a message (if possible)
                                                decoded_message = ''
                                                for n in factors:
                                                    if 32 <= n <= 126:  # Check if the byte corresponds to a printable ASCII character
                                                        decoded_message += chr(n)
                                                #print(f"Decoded Message (from byte values): {decoded_message}")
                                            
                                                # Step 5: Convert to Base 256 (Hexadecimal)
                                                base256_message = ' '.join(format(num, 'x') for num in factors)
                                                #print(f"Decoded Message in Base 256: {base256_message}")
                                            
                                                # Step 6: Convert to Binary (8 bits each)
                                                binary_message = ''.join(format(num, '08b') for num in factors)
                                                #print(f"Decoded Message in Binary (8 bits each): {binary_message}")
                                            
                                            except ValueError as e:
                                                print(f"Error: {e}")
                                      
                                    
                                    #print(binary_message)
                                    T10=binary_message
                                    
    
                                                                 

                                    INFO = T10
                                    T8 = T10

                                    long_one_time = len(T10)

                                    if (
                                        times_compress >=0
                                       
                                    ):
                                        stop_compress = 1
                                        Compress_file = 1
                                    long_bits_after_b_1 = 1
                                    times_compress += 1
                                    
                                        
                                        
                                        
                                    
                                    
                                    
                                    

                                # print(Compress_file)
                                if Compress_file == 1:
                                    Extract1 = 1
                                    if Extract1 == 1:
                                        times_compression_format = format(
                                            times_compress, "01b"
                                        )
                                        # print(times_compression_format)
                                        times_255 = format(
                                            len(times_compression_format),
                                            "08b",
                                        )
                                        times_255p = format(
                                            len(times_255),
                                            "016b",
                                        )

                                        # print(times_255_p_255)
                                        #  long of file  start number file before

                                        I_F_B = format(long_F1, "01b")
                                        # long of long before of file
                                        I_F_B_L = format(len(I_F_B), "08b")

                                        # long of file
                                        l_F_N = len(INFO)
                                        # long of  last number file after
                                        I_F_A = format(l_F_N, "01b")
                                        #  After long of long of file
                                        I_F_A_L = format(len(I_F_A), "08b")
                                        File_information5_17 = (
                                            "1"
                                            + times_255p
                                            + times_255
                                            + times_compression_format
                                            + I_F_B_L
                                            + I_F_B
                                            + I_F_A_L
                                            + I_F_A
                                            + INFO
                                        )

                                        long_1 = len(File_information5_17)
                                        add_bits = ""
                                        count_bits = (8 - long_1 % 8) % 8

                                        if count_bits > 0 and count_bits < 8:
                                            for _ in range(count_bits):
                                                add_bits = "0" + add_bits

                                    if Extract1 == 1:

                                        File_information5_17 = (
                                            add_bits + File_information5_17
                                        )
                                        L = len(File_information5_17)

                                        # print(L)

                                        n = int(File_information5_17, 2)

                                        width_bits = len(File_information5_17)

                                        width_bits = (width_bits // 8) * 2

                                        width_bits = str(width_bits)

                                        width_bits = "%0" + width_bits + "x"

                                        width_bits3 = binascii.unhexlify(
                                            width_bits % n
                                        )

                                        width_bits2 = len(width_bits3)

                                        File_information5_2 = Clear

                                        jl = width_bits3
                                        #import paq
                                        #jl = paq.compress(jl)
                                        
                                     

                                        name1 = name + ".s"

                                        with open(name1, "wb") as f2:

                                            f2.write(jl)

                                        x2 = time()

                                        x3 = x2 - x

                                        print(
                                            f"Speed bits: {(long_11) / x3:.5f}"
                                        )

                                        print("checker seccefully")

                                        xs = float(x3)

                                        xs = str(xs)

                                        return xs

                        if i == 2:

                            if C == 1:

                                Extract1 = 0
                                File_information5 = INFO

                                # extract

                                if Circle_times3 == 0:

                                    long_16 = len(File_information5)

                                    if File_information5[:1] == "0":

                                        while File_information5[:1] != "1":

                                            if File_information5[:1] == "0":

                                                File_information5 = (
                                                    File_information5[1:]
                                                )

                                    if File_information5[:1] == "1":

                                        File_information5 = File_information5[
                                            1:
                                        ]

                                INFO = File_information5
                                # print(INFO)

                                if Circle_times3 == 0:
                                    # times count extract

                                    CEI = int(INFO[:16], 2)

                                    # print(CE)

                                    INFO = INFO[16:]

                                    CE = int(INFO[:CEI], 2)

                                    # print(CE)

                                    INFO = INFO[CEI:]

                                    tce = int(INFO[:CE], 2)

                                    # print(tce)

                                    INFO = INFO[CE:]
                                    #############

                                    # INFO before file before size of file
                                    CE1 = int(INFO[:8], 2)

                                    # print(CE)

                                    INFO = INFO[8:]
                                    bfnz = int(INFO[:CE1], 2)

                                    # print(bfnz)

                                    INFO = INFO[CE1:]
                                    #############

                                    # INFO before file after size of file
                                    CE2 = int(INFO[:8], 2)

                                    # print(CE)

                                    INFO = INFO[8:]
                                    efnz = int(INFO[:CE2], 2)

                                    # print(efnz)

                                    INFO = INFO[CE2:]
                                    # e.g.: 12 8-10
                                    #############

                                while Extract1 != 1:
                                    # 1 bits 21
                                    # 0 19
                                    long_F = len(INFO)
                                    # print(long_F)

                                    block = 0
                                    TUPLE = ""
                                    T8 = INFO
                                    T15=""
                                    Transform=T8
                                    shora=1
                                    if shora==1:

                                        
                                            try:
                                                # Step 1: Ask the user to enter a binary string without spaces
                                                binary_input = Transform
                                                
                                                # Step 2: Validate the binary input and decode into byte values (0-255)
                                                if len(binary_input) % 8 != 0:
                                                    raise ValueError("Binary input must be a multiple of 8 bits.")
                                                
                                                byte_values = [int(binary_input[i:i+8], 2) for i in range(0, len(binary_input), 8)]
                                            
                                                # Step 3: Convert the byte values into base 256 (hexadecimal)
                                                base256_message = ''.join(format(num, '02x') for num in byte_values)
                                            
                                                # Step 4: Calculate the product of the byte values
                                                product = 1
                                                for byte in byte_values:
                                                    product *= byte
                                            
                                                # Step 5: Calculate the binary representation of the product
                                                product_binary = format(product, 'b')  # Binary representation without spaces
                                            
                                                # Step 6: Convert byte values back to binary representation (8 bits each, no spaces)
                                                binary_message = ''.join(format(num, '08b') for num in byte_values)
                                            
                                                # Step 7: Display the results
                                                #print(f"Input Binary: {binary_input}")
                                                #print(f"Byte Values (decoded from binary): {byte_values}")
                                                #print(f"Product of Byte Values: {product}")
                                                #print(f"Binary Representation of Product: {product_binary}")
                                                #print(f"Decoded Message in Base 256 (hexadecimal): {base256_message}")
                                                #print(f"Binary Representation (8 bits each, no spaces): {binary_message}")
                                                #print("The decoded message based on the byte values is displayed above.")
                                            
                                            except ValueError as e:
                                                print(f"Error: {e}")
                                   
                                        
                                        


                                    T10=product_binary
                                    #print(T10)
                                    TUPLE=T10
                                    TUPLE1 = TUPLE[1:]
                                    INFO = TUPLE
                                    #print(INFO)

                                    long_L = len(TUPLE)
                                    Tc += 1
                                    # print(Tc)

                                    if tce == Tc:
                                        Extract1 = 1

                                if Extract1 == 1:
                                    num4 = int(TUPLE1, 2)
                                    # print(num4)
                                    C19 = "0" + str(bfnz) + "b"
                                    TUPLE1 = format(num4, C19)
                                    File_information5_17 = TUPLE1

                                if Extract1 == 1:
                                    L = len(File_information5_17)
                                    n = int(File_information5_17, 2)
                                    width_bits = "%0" + str((L // 8) * 2) + "x"
                                    width_bits3 = binascii.unhexlify(
                                        width_bits % n
                                    )
                                    width_bits2 = len(width_bits3)
                                    name2 = name[:-2]
                                    start_time = time()
                                    with open(name2, "wb") as f2:
                                        f2.write(width_bits3)
                                    elapsed_time = time() - start_time
                                    speed_bits = (long_11 * 8) // float(
                                        elapsed_time
                                    )
                                    print(f"Speed bits: {speed_bits:.5f}")
                                    print("checker seccefully")
                                    return str(elapsed_time)


d = compression()
xw1 = d.cryptograpy_compression4()
print(xw1)