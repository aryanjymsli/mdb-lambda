import re

bucket_name = ''
output_folder = ''
model_file_name = ''
prefix = ''
model_key = ''


#this function set the vaiables which decide input and output folders and model  
def set_input_folder_from_name(image_name):
    arry= split_string_and_append_to_array(image_name)
    client_name=arry[0]
    project_name =arry[1]
    model_file_name =arry[2]
    model_folder_name = arry[3]
    input_folder =arry[4]
    output_folder=arry[5]
    uuid =arry[6]
    file_type =arry[7]
    prefix = model_folder_name
    model_key = f'{prefix}/{model_file_name}'
    local_model_path = '/tmp/' + model_file_name

    print(arry,client_name,project_name,model_folder_name,model_file_name,input_folder,output_folder,file_type,prefix,model_key)
    
#this function uses regex to create variables 
def split_string_and_append_to_array(input_string):
    # Define the regex pattern to split by periods
    pattern = r'\-'
    
    # Use re.split to split the input string by the pattern
    split_strings = re.split(pattern, input_string)
    
    # Initialize an empty array
    result_array = []
    
    # Append each substring to the array
    for substring in split_strings:
        result_array.append(substring)
    
    return result_array



test_image_name = "client_name-project_name-model_folder_name-model_file_name-input_folder-output_folder-uuid-fileType"
set_input_folder_from_name(test_image_name)