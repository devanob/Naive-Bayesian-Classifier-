from folderDirectoryScanner.dirScanner import folderDirectory

"""[summary]

Returns:
    [type] -- [description]
"""
class DataLoaderModules(object): 

    def __init__(self,rootDataDir):
        self.rootDataDir = rootDataDir
        self.processClassifications()

    def setRootDataDir(self,rootDataDir):
        self.rootDataDir = rootDataDir

    def processClassifications(self):
        self.folderScan = folderDirectory(self.rootDataDir)

    def getListClassifications(self):
        return self.folderScan.getListFolder()

    def getListClassifications_Directory(self):
        return self.folderScan.getPathDirFolder()

    def getListFilePerDirectory(self):
        self.filePerDir = {}
        absDir =  self.getListClassifications_Directory()
        nameDir = self.getListClassifications()
        for  index in range(len(absDir)):
            self.filePerDir[nameDir[index]] = folderDirectory(absDir[index]).getFilesDir()
        print(self.filePerDir)

    def scan(self):
        self.processClassifications()
        self.getListFilePerDirectory()

    







