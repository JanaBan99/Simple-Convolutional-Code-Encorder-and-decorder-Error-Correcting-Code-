temp = []
user_input_bits = input("Enter the data bits you want to encode:")
input_bits = []
input_bits = [int(bit) for bit in user_input_bits]
input_bits.extend([0, 0, 0])
shift_register = [0, 0, 0]
Convolutional_encoded_bits = []
n = len(input_bits)
print("print n value:", n)

def shift_bits():
    shift_register[2] = shift_register[1]
    shift_register[1] = shift_register[0]

def calculate():
    c1 = shift_register[0] ^ shift_register[1] ^ shift_register[2]
    c2 = shift_register[0] ^ shift_register[2]
    c3 = shift_register[0] ^ shift_register[1]
    Convolutional_encoded_bits.extend([c1, c2, c3])
    shift_bits()
    #Convolutional_encoded_bits.extend([c1,c2])
    #print ("i value:", i)
    #print ("c1 value:", c1)
    #print ("c2 value:", c2)
    #print ("c3 value:", c3)
    
    
i =  0
while i <= n-1 :
    temp = input_bits[i]
    shift_register[0] = temp
    #input_bits.pop(i)
    i += 1
    calculate()
#else:
    #print("Finished encoding bits")

print("Convolutional-encoded_bits:", Convolutional_encoded_bits)
