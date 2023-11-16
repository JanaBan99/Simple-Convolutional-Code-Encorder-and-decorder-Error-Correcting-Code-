
input_bits = [1, 0, 1, 0, 0, 0, 1]
shift_register = [0, 0, 0]
Convolutional_encoded_bits = []

def shift_bits():
    shift_register[2] = shift_register[1]
    shift_register[1] = shift_register[0]

def calculate():
    c1 = shift_register[0] ^ shift_register[1] ^ shift_register[2]
    c2 = shift_register[0] ^ shift_register[2]
    c3 = shift_register[0] ^ shift_register[1]
    Convolutional_encoded_bits.extend([c1, c2, c3])
    shift_bits()

i = 6
while i >= 0:
    temp = input_bits[i]
    shift_register[0] = temp
    input_bits.pop(i)
    i -= 1
    calculate()

print("Convolutional-encoded_bits:", Convolutional_encoded_bits)
