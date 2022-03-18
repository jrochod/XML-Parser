# used to parse the xml file and edit it
import xml.etree.ElementTree as ET
# used to obtain the file to be edited from the command line upon program execution
import argparse

# gets the arguments from the command line
def get_args():
    # initialize argument parser
    parser = argparse.ArgumentParser()
    # add argument to parser to look for a filename in the command line
    parser.add_argument('filename', type = argparse.FileType('rb+')) # --> read and write permissions in binary format (need binary format for doc.write)
    # add argument to parser to look for a string (represents the branchname) in the command line
    parser.add_argument('branchname', type = str)
    # parses the arguments from the command line
    argFile = parser.parse_args()
    return argFile

    """ ---> the following are all of the allowed access modifiers for argparse.FileType:
    "r"   Opens a file for reading only.
    "r+"  Opens a file for both reading and writing.
    "rb"  Opens a file for reading only in binary format.
    "rb+" Opens a file for both reading and writing in binary format.
    "w"   Opens a file for writing only.
    "a"   Open for writing. The file is created if it does not exist.
    "a+"  Open for reading and writing.  The file is created if it does not exist.

    """

# edits the xml file (if needed) and prints the resulting xml file
def edit_xml(file_name, file_path, branch_name):
    doc = ET.parse(file_name) 
    docRoot = doc.getroot()
    print("Printing from element tree using argparse: ")
    for project in doc.findall('project'):
        print(project.attrib)

    print("Attempting to edit xml file using argparse and element tree: ")
    for project in doc.findall('project'):
        name = project.get('name')
        if(name == "acm" or name == "corelockr" or name == "Edge2_Web" or name == "extraFiles" or name == "G2_Keys_And_Certs" or name == "iSTAR_App" 
            or name == "iSTAR_Web" or name == "iSTAR-EdgeG2-M4" or name == "jci_data" or name == "Manifests" or name == "meta-jci-app-edge2" 
            or name == "meta-jci-ate-edge2" or name == "meta-jci-bsp-edge2" or name == "meta-jci-distro-edge" or name == "meta-jci-startup" 
            or name == "meta-jci-web-edge2" or name == "optee_client" or name == "provisioning" or name == "provSD12-uboot" or name == "provSign" 
            or name == "sli_resources" or name == "u-boot-fslc" or name == "Ubuntu_Build" or name == "Ubuntu_OS_Utils"):
                project.set('revision', branch_name)
                doc.write(file_path)
        print(project.attrib)

    file_name.close()




def main():

    # get the arguments from the command line
    argFile = get_args()

    # debugging statements:
    # print(argFile.filename) # --> BufferedRandom object, name = edge2.xml (file we need to read/write from)
    # print(argFile.filename.name) # --> .name obtains name of BuffereRandom object, will use when write changes back to xml file
    # print(argFile.branchname)

    # editing the xml file (if needed) based on the branch name
    edit_xml(argFile.filename, argFile.filename.name, argFile.branchname)


if __name__ == "__main__":
    main()