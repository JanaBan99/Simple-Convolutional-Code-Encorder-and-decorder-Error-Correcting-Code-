def process_data(dataword):
    # Function to process the dataword using the given logic

    # Define the initial states and arrays
    Current_status = [0, 0, 0]
    output_status_array = []


    separate_arrays = []
    for i in range(0, len(dataword), 3):
        separate_arrays.append(dataword[i:i+3])
        
    print("Separate Array:", separate_arrays)

    # Process each separate array
    for input_codeword in separate_arrays:
        input_codeword.extend([0, 0, 0]) 
        print("Input Codeword:", input_codeword)

        # Process each input codeword
        for Input in input_codeword:
            if Current_status == [0, 0, 0] and Input == 0:
                Output_status = [0, 0, 0]
                Current_status = [0, 0, 0]
                output_status_array.extend(Output_status)

            elif Current_status == [0,0,0] and Input == 1:
                Output_status = [1,1,1]
                Current_status = [1,0,0]
                output_status_array.extend(Output_status)
        
            ############## 
        
            elif Current_status == [0,0,1] and Input == 0:
                Output_status = [1,0,1]
                Current_status = [0,0,0]
                output_status_array.extend(Output_status)
        
            elif Current_status == [0,0,1] and Input == 1:
                Output_status = [0,1,0]
                Current_status = [1,0,0]
                output_status_array.extend(Output_status)
        
            ###############
        
            elif Current_status == [0,1,0] and Input == 0:
                Output_status = [1,1,1]
                Current_status = [0,0,1]
                output_status_array.extend(Output_status)
        
            elif Current_status == [0,1,0] and Input == 1:
                Output_status = [0,0,0]
                Current_status = [1,0,1]
                output_status_array.extend(Output_status)
        
            ###############
        
            elif Current_status == [0,1,1] and Input == 0:
                Output_status = [0,1,0]
                Current_status = [0,0,1]
                output_status_array.extend(Output_status)
        
            elif Current_status == [0,1,1] and Input == 1:
                Output_status = [1,0,1]
                Current_status = [1,0,1]
                output_status_array.extend(Output_status)
        
            ###############
        
            elif Current_status == [1,0,0] and Input == 0:
                Output_status = [1,1,0]
                Current_status = [0,1,0]
                output_status_array.extend(Output_status)
        
            elif Current_status == [1,0,0] and Input == 1:
                Output_status = [0,0,1]
                Current_status = [1,1,0]
                output_status_array.extend(Output_status)
        
            ###############
        
            elif Current_status == [1,0,1] and Input == 0:
                Output_status = [0,1,1]
                Current_status = [0,1,0]
                output_status_array.extend(Output_status)
        
            elif Current_status == [1,0,1] and Input == 1:
                Output_status = [1,0,0]
                Current_status = [1,1,0]
                output_status_array.extend(Output_status)
        
            ###############
        
            elif Current_status == [1,1,0] and Input == 0:
                Output_status = [0,0,1]
                Current_status = [0,1,1]
                output_status_array.extend(Output_status)
        
            elif Current_status == [1,1,0] and Input == 1:
                Output_status = [1,1,0]
                Current_status = [1,1,1]
                output_status_array.extend(Output_status)
        
            ###############
        
            elif Current_status == [1,1,1] and Input == 0:
                Output_status = [1,0,0]
                Current_status = [0,1,1]
                output_status_array.extend(Output_status)
        
            elif Current_status == [1,1,1] and Input == 1:
                Output_status = [0,1,1]
                Current_status = [1,1,1]
                output_status_array.extend(Output_status)

        print("Input:", Input)
        print("Current Status:", Current_status)
        print("------------------------")

    print("------------------------")
    print("Output Status Array:", output_status_array)
    print("------------------------")


# Test the function with a sample dataword
dataword = [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1]
#dataword = [1, 0, 1, 1, 0, 1]
process_data(dataword)
