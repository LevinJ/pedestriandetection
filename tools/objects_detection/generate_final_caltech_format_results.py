'''
Created on Dec 4, 2014

@author: levin
'''
import os, os.path
import glob


def write_file_force(resultFilePath, lines):
    resultfiledir = os.path.dirname(resultFilePath)
    if not os.path.exists(resultfiledir):
        os.makedirs(resultfiledir)
    #text_file = open(resultFilePath, "a+") # append to the file
    with open(resultFilePath,"a+",) as f:
        f.writelines(lines)

def get_path_and_id(infile):
    filename = os.path.basename(infile)
    templist = filename.split("_")
    #  print templist
    result_file_path = os.path.dirname(infile)+ "/res/" + templist[0] + "/"+templist[1] + ".txt"
    # print result_file_path 
    num = templist[2].split(".")[0]
    num = num[1: len(num)]
    num = int(num) + 1
    return {"file_path": result_file_path, "numtoadd":str(num)}
    
    
def generate_result_files(output_path):
    filelist = glob.glob(os.path.join(output_path, '*.txt'))
    for infile in sorted(filelist): 
        #do some fancy stuff
        print str(infile) 
        respathid = get_path_and_id(infile)
        with open(infile) as f:
            linelist =[]
            for line in f:
                linelist.append(respathid["numtoadd"] + "," + line)
            print(respathid["file_path"],linelist)
            write_file_force(respathid["file_path"],linelist)
        
    


