from DataLoaderModule.DataLoaderModules import DataLoaderModules


if __name__ == "__main__":
    testData = DataLoaderModules("Data")
    print(testData.getListFilePerDirectory())