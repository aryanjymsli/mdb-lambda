import re

bucket_name = ''
output_folder = ''
model_file_name = ''
prefix = ''
model_key = ''


def set_input_folder_from_name(image_name):
    arry= split_string_and_append_to_array(image_name)
    client_name=arry[0]
    project_name =arry[1]
    model_file_name =arry[2]
    input_folder =arry[3]
    output_folder=arry[4]
    uuid =arry[5]
    file_type =arry[6]
    prefix = 'Model_files'
    model_key = f'{prefix}/{model_file_name}'

    print(arry,client_name,project_name,model_file_name,input_folder,output_folder,file_type,prefix,model_key)
    
def split_string_and_append_to_array(input_string):
    # Define the regex pattern to split by periods
    pattern = r'\.'
    
    # Use re.split to split the input string by the pattern
    split_strings = re.split(pattern, input_string)
    
    # Initialize an empty array
    result_array = []
    
    # Append each substring to the array
    for substring in split_strings:
        result_array.append(substring)
    
    return result_array

test_image_name = "client_name.project_name.model_name.input_folder.output_folder.uuid.fileType"
set_input_folder_from_name(test_image_name)