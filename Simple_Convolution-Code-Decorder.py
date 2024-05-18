array1=[]
array2=[]
array3=[]
array4=[]
array5=[]
array6=[]

# Decording_bits              
Decording_bits = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1] #[1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1]

# Split Decording_bits into arrays with 3 elements each
arrays = [Decording_bits[i:i+3] for i in range(0, len(Decording_bits), 3)]

# Declare arrays with names array1, array2, etc.
for i, array in enumerate(arrays, start=1):
    globals()[f"array{i}"] = array

# Print the arrays with their names
for i, array in enumerate(arrays, start=1):
    print(f"array{i}: {array}")
    print()

############## decode the bits in the first stage ################
if array1 == [0, 0, 0]:
    input_value = 0
    print("Input1:", input_value)
    
elif array1 == [1, 1, 1]:
    input_value = 1
    print("Input1:", input_value)

else:
    a = [1, 1, 1]
    b = [0, 0, 0]
    hamming_dist_111 = sum(1 for x, y in zip(array1, a) if x != y)
    hamming_dist_000 = sum(1 for x, y in zip(array1, b) if x != y)
    
    values = [x for x in (hamming_dist_111, hamming_dist_000) if x != 0]
    min_hamming_dist = min(values)
    #print("hamming_dist_000:", hamming_dist_000)
    #print("hamming_dist_111:", hamming_dist_111)
    if hamming_dist_111 > hamming_dist_000:
        input_value = 0
        print("Input1:", input_value)
    else:
        input_value = 1
        print("Input1:", input_value)

############### Decord the bits in the second stage ##############

if array2 == [0, 0, 0]:
    input_value = 0
    next_shift_reg = [0, 0, 0]
    print("Input2:", input_value)
    
elif array2 == [1, 1, 1]:
    input_value = 1
    next_shift_reg = [1, 0, 0]
    print("Input2:", input_value)
    
elif array2 == [1, 1, 0]:
    input_value = 0
    next_shift_reg = [0, 1, 0]
    #print("next_shift_reg:", next_shift_reg)
    print("Input2:", input_value)
    
elif array2 == [0, 0, 1]:
    input_value = 1
    next_shift_reg = [1, 1, 0]
    print("Input2:", input_value)
    

else:
    a = [1, 1, 1]
    b = [0, 0, 0]
    c = [1, 1, 0]
    d = [0, 0, 1]
    hamming_dist_111 = sum(1 for x, y in zip(array2, a) if x != y)
    hamming_dist_000 = sum(1 for x, y in zip(array2, b) if x != y)
    hamming_dist_110 = sum(1 for x, y in zip(array2, c) if x != y)
    hamming_dist_001 = sum(1 for x, y in zip(array2, d) if x != y)

    values = [x for x in (hamming_dist_111, hamming_dist_000, hamming_dist_110, hamming_dist_001) if x != 0]
    min_hamming_dist = min(values)
    
    if min_hamming_dist == hamming_dist_111:
        input_value = 1
        next_shift_reg = [1, 0, 0]
        print("Input2:", input_value)
    elif min_hamming_dist == hamming_dist_000:
        input_value = 0
        next_shift_reg = [0, 0, 0]
        print("Input2:", input_value)
    elif min_hamming_dist == hamming_dist_110:
        input_value = 0
        next_shift_reg = [0, 1, 0]
        print("Input2:", input_value)
        #result_array = c
    elif min_hamming_dist == hamming_dist_001:
        input_value = 1
        next_shift_reg = [1, 1, 0]
        print("Input2:", input_value)



############### Decord the bits in the third stage ##############
# decorde the bits in the third stage
#print("next_shift_reg:", next_shift_reg)
if array3 == [0, 0, 0] and next_shift_reg == [0, 0, 0]: ############
    input_value = 0
    print("Input3:", input_value)
    
elif array3 == [1, 1, 1] and next_shift_reg == [0, 0, 0]:
    input_value = 1
    print("Input3:", input_value)
    
elif array3 == [1, 1, 0] and next_shift_reg == [1, 0, 0]:
    input_value = 0
    print("Input3:", input_value)
    
elif array3 == [0, 0, 1] and next_shift_reg == [1, 0, 0]:
    input_value = 1
    print("Input3:", input_value)
    
elif array3 == [1, 1, 1] and next_shift_reg == [0, 1, 0]:
    input_value = 1
    print("Input3:", input_value)
    
elif array3 == [0, 0, 0] and next_shift_reg == [0, 1, 0]: #############
    input_value = 1
    print("Input3:", input_value)
    
elif array3 == [0, 0, 1] and next_shift_reg == [1, 1, 0]:
    input_value = 1
    print("Input3:", input_value)
    
elif array3 == [1, 1, 0] and next_shift_reg == [1, 1, 0]:
    input_value = 1
    print("Input3:", input_value)

else:
    a = [1, 1, 1]
    b = [0, 0, 0]
    c = [1, 1, 0]
    d = [0, 0, 1]
    hamming_dist_111 = sum(1 for x, y in zip(array3, a) if x != y)
    hamming_dist_000 = sum(1 for x, y in zip(array3, b) if x != y)
    hamming_dist_110 = sum(1 for x, y in zip(array3, c) if x != y)
    hamming_dist_001 = sum(1 for x, y in zip(array3, d) if x != y)

    values = [x for x in (hamming_dist_111, hamming_dist_000, hamming_dist_110, hamming_dist_001) if x != 0]
    min_hamming_dist = min(values)
    
    
    if min_hamming_dist == hamming_dist_111 and next_shift_reg == [0, 0, 0]: #check input bits in these 
        input_value = 1
        print("Input3:", input_value)
    elif min_hamming_dist == hamming_dist_111 and next_shift_reg == [0, 1, 0]:
        input_value = 1
        print("Input3:", input_value)
    elif min_hamming_dist == hamming_dist_000 and next_shift_reg == [0, 0, 0]:
        input_value = 0
        print("Input3:", input_value)
    elif min_hamming_dist == hamming_dist_000 and next_shift_reg == [0, 1, 0]:
        input_value = 1
        print("Input3:", input_value)
    elif min_hamming_dist == hamming_dist_110 and next_shift_reg == [1, 0, 0]:
        input_value = 0
        print("Input3:", input_value)
    elif min_hamming_dist == hamming_dist_110 and next_shift_reg == [1, 1, 0]:
        input_value = 1
        print("Input3:", input_value)
    elif min_hamming_dist == hamming_dist_001 and next_shift_reg == [1, 0, 0]:
        input_value = 1
        print("Input3:", input_value)
    elif min_hamming_dist == hamming_dist_001 and next_shift_reg == [1, 1, 0]:
        input_value = 1
        print("Input3:", input_value)

############### decorde the bits in the fourth stage ###############
if array4 == [0, 0, 0]:
    input_value = 0
    print("Input4:", input_value)
    
elif array4 == [1, 0, 1]:
    input_value = 0
    print("Input4:", input_value)
    
elif array4 == [1, 1, 0]:
    input_value = 0
    print("Input4:", input_value)
    
elif array4 == [1, 1, 1]:
    input_value = 0
    print("Input4:", input_value)
    
elif array4 == [0, 1, 1]:
    input_value = 0
    print("Input4:", input_value)
    
elif array4 == [0, 0, 1]:
    input_value = 0
    print("Input4:", input_value)
    
elif array4 == [0, 1, 0]:
    input_value = 0
    print("Input4:", input_value)
    
elif array4 == [1, 0, 0]:
    input_value = 0
    print("Input4:", input_value)

else:
    a = [0, 0, 0] 
    b = [1, 0, 1] 
    c = [1, 1, 0] 
    d = [1, 1, 1] 
    e = [0, 1, 1] 
    f = [0, 0, 1] 
    g = [0, 1, 0]
    h = [1, 0, 0]
    hamming_dist_000 = sum(1 for x, y in zip(array4, a) if x != y)
    hamming_dist_101 = sum(1 for x, y in zip(array4, b) if x != y)
    hamming_dist_110 = sum(1 for x, y in zip(array4, c) if x != y)
    hamming_dist_111 = sum(1 for x, y in zip(array4, d) if x != y)
    hamming_dist_011 = sum(1 for x, y in zip(array4, e) if x != y)
    hamming_dist_001 = sum(1 for x, y in zip(array4, f) if x != y)
    hamming_dist_010 = sum(1 for x, y in zip(array4, g) if x != y)
    hamming_dist_100 = sum(1 for x, y in zip(array4, h) if x != y)
    
    values = [x for x in (hamming_dist_111, hamming_dist_000, hamming_dist_110, hamming_dist_001, hamming_dist_101, hamming_dist_011, hamming_dist_010, hamming_dist_100) if x != 0]
    min_hamming_dist = min(values)
    
    if min_hamming_dist == hamming_dist_000:## last ek gtte ne ss ekt ekth blnn
        input_value = 0
        print("Input4:", input_value)
        
    elif min_hamming_dist == hamming_dist_101:
        input_value = 0
        print("Input4:", input_value)
        
    elif min_hamming_dist == hamming_dist_110:
        input_value = 0
        print("Input4:", input_value)
        
    elif min_hamming_dist == hamming_dist_111:
        input_value = 0
        print("Input4:", input_value)
        
    elif min_hamming_dist == hamming_dist_011:
        input_value = 0
        print("Input4:", input_value)
        
    elif min_hamming_dist == hamming_dist_001:
        input_value = 0
        print("Input4:", input_value)
        
    elif min_hamming_dist == hamming_dist_101:
        input_value = 0
        print("Input4:", input_value)
        
    elif min_hamming_dist == hamming_dist_100:
        input_value = 0
        print("Input4:", input_value)
        
############### decorde the bits in the fifth stage ###############
if array5 == [0, 0, 0]:
    input_value = 0
    print("Input5:", input_value)
    
elif array5 == [1, 0, 1]:
    input_value = 0
    print("Input5:", input_value)
    
elif array5 == [1, 1, 0]:
    input_value = 0
    print("Input5:", input_value)
    
elif array5 == [1, 1, 1]:
    input_value = 0
    print("Input5:", input_value)
    

else:
    a = [1, 1, 1]
    b = [0, 0, 0]
    c = [1, 1, 0]
    d = [1, 0, 1]
    
    hamming_dist_000 = sum(1 for x, y in zip(array5, b) if x != y)
    hamming_dist_111 = sum(1 for x, y in zip(array5, a) if x != y)
    hamming_dist_110 = sum(1 for x, y in zip(array5, c) if x != y)
    hamming_dist_101 = sum(1 for x, y in zip(array5, d) if x != y)
    

    values = [x for x in (hamming_dist_111, hamming_dist_000, hamming_dist_110, hamming_dist_101) if x != 0]
    min_hamming_dist = min(values)
    #min_hamming_dist = min(hamming_dist_000, hamming_dist_101, hamming_dist_110, hamming_dist_111)
    
    if min_hamming_dist == hamming_dist_000:
        input_value = 0
        print("Input5:", input_value)
        
    elif min_hamming_dist == hamming_dist_101:
        input_value = 0
        print("Input5:", input_value)
        
    elif min_hamming_dist == hamming_dist_110:
        input_value = 0
        print("Input5:", input_value)
        
    elif min_hamming_dist == hamming_dist_111:
        input_value = 0
        print("Input5:", input_value)


############### decorde the bits in the sixth stage ###############

if array6 == [0, 0, 0]:
    input_value = 0
    print("Input6:", input_value)
    
elif array6 == [1, 0, 1]:
    input_value = 0
    print("Input6:", input_value)
    
else:
    a = [1, 0, 1]
    b = [0, 0, 0]
    hamming_dist_000 = sum(1 for x, y in zip(array6, b) if x != y)
    hamming_dist_101 = sum(1 for x, y in zip(array6, a) if x != y)
    
    values = [x for x in (hamming_dist_000, hamming_dist_101) if x != 0]
    min_hamming_dist = min(values)
    
    if min_hamming_dist == hamming_dist_000:
        input_value = 0
        print("Input6:", input_value)
        
    elif min_hamming_dist == hamming_dist_101:
        input_value = 0
        print("Input6:", input_value)