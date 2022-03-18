# used to parse the xml file and edit it
import xml.etree.ElementTree as ET
# used to obtain the file to be edited from the command line upon program execution
import argparse
import sys

# initialize argument parser
parser = argparse.ArgumentParser()
parser.add_argument('filename', type = argparse.FileType('rb+')) # --> read and write permissions in binary format (need binary format for doc.write)
parser.add_argument('branchname', type = str)
argFile = parser.parse_args()

"""
"r"   Opens a file for reading only.
"r+"  Opens a file for both reading and writing.
"rb"  Opens a file for reading only in binary format.
"rb+" Opens a file for both reading and writing in binary format.
"w"   Opens a file for writing only.
"a"   Open for writing. The file is created if it does not exist.
"a+"  Open for reading and writing.  The file is created if it does not exist.

"""





def main():
    # initialize argument parser
    # parser = argparse.ArgumentParser()
    # parser.add_argument('filename', type = argparse.FileType('r')) # ---> TODO: these don't work, only argFile initialized outside of main works with element tree. I need both parsers for it to work for some reason.
    # args = parser.parse_args()
    # print("Printing from argparser: ")
    # for file in argFile.filename: ---> TODO: if this for loop is implemented, the ones below don't work, need two different parsers.
        # print(file.strip())

    # with argFile.filename as file: ---> use this line?
    """
    attempted to print the file path of the variable, cannot figure this out

    for file_name in argFile.filename:
        with open(file_name, 'r+') as files:
            print(file_name)
    """

    print(argFile.filename) # --> BufferedRandom object, name = edge2.xml (file we need to read/write from)
    print(argFile.filename.name) # --> .name obtains name of BuffereRandom object, will use when write changes back to xml file

    doc = ET.parse(argFile.filename) 
    docRoot = doc.getroot()
    print("Printing from element tree using argparse: ")
    for project in doc.findall('project'):
        print(project.attrib)

    print("Attempting to edit xml file using argparse and element tree: ")
    for project in doc.findall('project'):
        name = project.get('name')
        if(name == "meta-jci-app-edge2"):
            project.set('revision', argFile.branchname)
            doc.write(argFile.filename.name) # TODO --> without .name, rewrites entire contents of the file in the same file with the edit. Also, once does once, says junk at end of file
        print(project.attrib)

    argFile.filename.close()

    # TODO: do we need argparse? Just import sys and do following: f = open(sys.argv[1],"r") contents = f.read() f.close() print contents and use ET.parse on f?
    """
    # The following works using sys, not argparse:
    print("Trying sys")
    f = open(sys.argv[1], "r")
    contents = f.read()
    f.close()
    print(contents)

    print("Attempting to use element tree to edit file using sys to parse the file from command line")
    doc = ET.parse(sys.argv[1])
    for project in doc.findall('project'):
        print(project.attrib)

    """

if __name__ == "__main__":
    main()