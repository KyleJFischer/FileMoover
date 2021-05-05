import time
import yaml
from os import listdir, rename
from os.path import isfile, join
settings = {}

def loadYaml():
    global settings
    with open(r'settings.yaml') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
        settings = yaml.load(file, Loader=yaml.FullLoader)

def moveFile(folder, file):
    inputFolder = join(folder, file)
    outputFolder = join(settings["Output"], file)
    rename(inputFolder, outputFolder)



while (True):
    loadYaml()
    foldersToWatch = settings["foldersToWatch"]
    for folder in foldersToWatch:
        onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]
        for file in onlyfiles:
            moveFile(folder, file)
    time.sleep(5)