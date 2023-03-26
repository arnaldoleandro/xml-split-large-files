# Repo xml-split-large-files Description
Efficiently split large XML files into smaller files using Python, while preserving the structure and integrity of the original data. Ideal for processing and handling massive XML datasets.


# XML File Splitter

This Python script splits a large XML file into smaller files based on a specified file size limit.

## Usage

1. Set the variables at the beginning of the `main` function:
   - `filename`: Name of the input XML file.
   - `input_file`: Path to the input XML file.
   - `size_limit`: Maximum size of the output files in MB.
   - `output_dir`: Path to the directory where the output files will be saved.
   - `output_file_prefix`: Prefix for the output file names.
   - `last_element_close`: The closing tag of the XML element that represents a single record in the file. Like `</food>` in the example:
```xml
<breakfast_menu>
	<food>
		<name>Belgian Waffles</name>
		<price>$5.95</price>
		<description>Two of our famous Belgian Waffles with plenty of real maple syrup</description>
		<calories>650</calories>
	</food>
	<food>
    <name>Strawberry Belgian Waffles</name>
		<price>$7.95</price>
		<description>Light Belgian waffles covered with strawberries and whipped cream</description>
		<calories>900</calories>
	</food>`
</breakfast_menu>

2. Run the script:

    `python xml_file_splitter.py`

## Requirements

- Python 3.6 or higher

