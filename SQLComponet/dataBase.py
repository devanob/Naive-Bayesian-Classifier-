from databases import Database
import asyncio
import os
import random

script_dir = os.path.dirname(__file__)


class DataBaseComponet:

    def __init__(self, dataBaseName, asyncIoEventLoop=None):
        # create database connection
         self.database = Database('sqlite:///BayesianDataBase.db')
         # get event loop
         self.eventLoop = asyncio.get_event_loop()
         self.loadSQLCmds()
        

    #@app.on_event("startup")
    async def connectDateBase(self):
        await self.database.connect()

    #@app.on_event("shutdown")
    async def disconnectDateBase(self):
        await self.database.disconnect()

    def loadSQLCmds(self):
        ##load table set ups 
        sqlCmds = open('SQLComponet/SQLFiles/CreateTables.sql', 'r')
        rawQuery = sqlCmds.read().split(";")
        processedQuery = []
        for query in rawQuery:
            queryInstace = query.strip()
            queryInstace.replace('\n', '')
            if (queryInstace):
                processedQuery.append(queryInstace)
        self.setUpQueries = processedQuery
        sqlCmds.close()
        ##get insert Classification
        sqlCmds = open('SQLComponet/SQLFiles/insertClassification.sql', 'r')
        self.insertClassification = sqlCmds.read().strip().replace('\n', '').replace(';', ' ')
        ##get word sql 
        sqlCmds = open('SQLComponet/SQLFiles/insertWordList.sql', 'r')
        self.insertWordCmd = sqlCmds.read().strip().replace('\n', ' ').replace(';', '')
        ###get inset word list
        sqlCmds = open('SQLComponet/SQLFiles/insertClassificationWord.sql', 'r')
        self.insertWordClassCmd = sqlCmds.read().strip().replace('\n', ' ').replace(';', '')

        

    async def insertClassificationType(self, typeClassification):
        try:
            await self.database.execute(query=self.insertClassification.format(typeClassification))
        except:
            raise Exception('Could Not Insert: {}'.format(typeClassification))

    async def insertWord(self, word, count, classification=None):
        transaction = await self.database.transaction()
        try:
            query = self.insertWordCmd.format(word,count)
            print(query)
            await self.database.execute(query=query)
            if classification:
                query = self.insertWordClassCmd.format(classification,word,count)
                print(query)
                await self.database.execute(query=query)
        except:
            await transaction.rollback()
            #if the word exist
        else :
            await transaction.commit()

    async def setUpTables(self):
         for query in self.setUpQueries:
             await asyncio.create_task(self.database.execute(query=query))
    async def setUp(self):
        await self.connectDateBase()
        await self.setUpTables()
        



async def main():
   test = DataBaseComponet("io")
   await test.setUp()
   try:
       await test.insertClassificationType("Arther")
       await test.insertClassificationType("Merlin")
   except:
        pass
   await test.insertWord("King",10,"Arther")
   await test.insertWord("Magic",10,"Merlin")
   await test.insertWord("Staff",10,"Merlin")
   await test.insertWord("Camelot",10,"Arther")
   
   #await transaction.commit()


async def io(index):
    randInt = random.randint(5,20)
    print("Hello From Guy {} Sleep For {}".format(index,randInt))
    await asyncio.sleep(randInt)
    print("Good Bye From Guy {} Sleep For {}".format(index,randInt))
    return randInt

async def testStuff():

     for i in range(20):
        val = await asyncio.ensure_future(io(i))
        print(val)
    
   

if __name__ == "__main__":
    Loop = asyncio.get_event_loop()
    Loop.create_task(main())
    Loop.run_forever()

   
