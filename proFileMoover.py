import time
import yaml
from os import listdir, rename
from os.path import isfile, join
settings = {}




def loadYaml():
    global settings
    with open(r'proMoverSettings.yaml') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
        settings = yaml.load(file, Loader=yaml.FullLoader)

def moveFile(folder, file):
    
    inputFolder = join(folder, file)
    outputFolder = identifyOutputPath(file)
    
    rename(inputFolder, join(outputFolder, file))

def identifyOutputPath(fileName):
    global settings
    outputLocs = settings["OutputLocations"]
    keys = list(outputLocs.keys())
    for key in keys:
        if (fileName.startswith(key + "_")):
            return join(settings["OutputBasePath"], outputLocs[key], settings["OutputEndPath"])
    print(keys)
    

while (True):
    loadYaml()
    folder = settings["InputLocation"]
    onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]
    for file in onlyfiles:
        moveFile(folder, file)
    time.sleep(5)        