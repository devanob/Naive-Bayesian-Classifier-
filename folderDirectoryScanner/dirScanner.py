import os
dir_path = os.path.dirname(os.path.realpath(__file__))
scanFolder = "/TestDir"
full_dir = dir_path+scanFolder

# folderDirectory 
# This Class Scan A Certain Directory Given To It In The Contructor 
# Method Return Various Information In A List Form 
class folderDirectory:
    """[Class That Allow For Directory Walk]
    
    Raises:
        Exception: [description]
        Exception: [description]
    
    Returns:
        [type] -- [description]
    """
    root_dir = ""

    def __init__(self, directory=''):
        if not directory:
            raise Exception(
                'Exception: Constructor: "directory" should not be empty string or None')
        self.root_dir = directory
        self.list_dir = [dirInfo for dirInfo in os.walk(self.root_dir)]
    # retunrs the label of each folder in the root director
    def setRootDir(self,dir):
        if not dir:
            raise Exception('Exception: setRootDir: "dir" should not be empty string or None ')
    #gets all Folders in the root without aboslute directory 
    def getListFolder(self):
        return self.list_dir[0][1]
    # retunrs the absolute folder path of each folder in the root directory
    def getPathDirFolder(self):
        return [fulldir[0] for fulldir in self.list_dir[1:]]
    # returns the absolute file path of each folder in the root directory
    def getFilesDir(self):
        listFiles= self.list_dir[0][2]
        filesDir = [self.root_dir + "/" + fileName  for fileName in listFiles]
        return filesDir
    # returns the absolute folder path of each folder in the root directory
    def getFilesLabels(self):
        return self.list_dir[0][2]
    
        
if __name__ == '__main__':
    testDir = folderDirectory("./Dat")
    print(testDir.getPathDirFolder())
    