import os

def read_file(file_name, encode_name):

    # Open file
    read_target = open(os.getcwd() + '\\' + file_name, 'r', encoding=encode_name)

    # Read content
    raw_content = read_target.readlines()

    # Close file
    read_target.close()

    # Display raw_content and adjust content for use
    content = []
    for line in raw_content:
        temp_data = line.strip('\n')
        print('  - Read Script File: ' + temp_data)

        if len(temp_data) > 0 and temp_data[0] not in ['#', ' ']:
            temp_data = temp_data.split(' ')
            print('    - Accept Script: {}'.format(temp_data))
            content.append(temp_data)

    # Return result
    return content