import xml.etree.ElementTree as ET

# This function extracts content under the String tag
def extract_strings_from_xml(filepath):
    # Parse the XML file
    tree = ET.parse(filepath)
    root = tree.getroot()

    # Namespace dictionary
    namespace = {'alto': 'http://www.loc.gov/standards/alto/ns-v4#'}

    # Find all <String> elements under <TextLine>
    strings = root.findall('.//alto:TextLine/alto:String', namespace)

    # Extract the content of <String> elements
    contents = [string.get('CONTENT') for string in strings]

    # Print the extracted contents
    return " ".join(contents)