import xml.etree.ElementTree as ET
import os

def get_root_tag(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        file.readline()
        second_line = file.readline().strip()
        root_tag = second_line[1:].split(' ', 1)[0]
    return root_tag[:-1] if root_tag.endswith('>') else root_tag

def main():
    filename = 'your_input_file.xml'
    input_file = f'path/to/your/input/folder/{filename}'
    size_limit = 200 #MEGABYTES
    size_limit = size_limit * 10240 #convert to BYTES
    output_dir = 'path/to/your/output/folder/'
    output_file_prefix = 'output_file_prefix_'

    root_tag = get_root_tag(input_file)
    print(root_tag)
    last_element_close = '</your_row_tag>'

    with open(input_file, 'r', encoding='utf-8') as file:
        first_line = file.readline()
        second_line = file.readline()
        header = f"{first_line}{second_line}"
        footer = f'</{root_tag}>'

        file_number = 1
        size = 0
        lines_buffer = []

        def write_buffered_lines(out_file, lines):
            nonlocal size
            for line in lines:
                size += len(line.encode('utf-8'))
                out_file.write(line)

        for line in file:
            stripped_line = line.strip()
            lines_buffer.append(line)
            if last_element_close in stripped_line:
                size += len(line.encode('utf-8'))
               
                if size > size_limit:
                    output_file = os.path.join(output_dir, f"{output_file_prefix}{file_number}.xml")
                    with open(output_file, 'w', encoding='utf-8') as out_file:
                        out_file.write(header)
                        write_buffered_lines(out_file, lines_buffer)
                        out_file.write(footer)
                    print(f"arquivo {file_number}: {output_dir}:{output_file_prefix}{file_number}.xml")

                    file_number += 1
                    size = 0
                    lines_buffer = []
                    
            # Write the remaining records to a new file if there are any records left in the buffer
        if lines_buffer:
            output_file = os.path.join(output_dir, f"{output_file_prefix}{file_number}.xml")
            with open(output_file, 'w', encoding='utf-8') as out_file:
                out_file.write(header)
                write_buffered_lines(out_file, lines_buffer)
                #don't need to output the footer, since this is the EOF
            print(f"arquivo {file_number}: {output_dir}:{output_file_prefix}{file_number}.xml")

if __name__ == "__main__":
    main()