Current_status = [0, 0, 0]
Output_status = []
input_codeword = [1, 0, 1]
input_codeword.extend([0, 0, 0])  # Add three zeros to input_codeword
output_status_array = [] 

print(Current_status)

for Input in input_codeword:
    
    if Current_status == [0,0,0] and Input == 0:
        Output_status = [0,0,0]
        Current_status = [0,0,0]
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

###############
    # Add more conditions for other cases as shown in your example

    print("Input:", Input)
    print("Current_status:", Current_status)
    #print("Output_status:", Output_status)
    print("------------------------")


print("------------------------")
print("Output Status Array:", output_status_array)
print("------------------------")
