from DataLoaderModule.DataLoaderModules import DataLoaderModules


if __name__ == "__main__":
    testData = DataLoaderModules("Dat")
    print(testData.getListFilePerDirectory())