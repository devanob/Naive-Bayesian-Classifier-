from databases import Database
import asyncio
import os
import random

script_dir = os.path.dirname(__file__)


class DataBaseComponet:

    def __init__(self, dataBaseName, asyncIoEventLoop):
        # create database connection
         self.database = Database('sqlite:///BayesianDataBase.db')
         # get event loop
         self.eventLoop = asyncio.get_event_loop()

    async def setUpDataBase(self):
        await database.connect()

    def loadSQLCmds(self):
        sqlCmds = open('SQLComponet/SQLFiles/CreateTables.sql', 'r')
        rawQuery = sqlCmds.read().split(";")
        processedQuery = []
        for query in rawQuery:
            queryInstace = query.strip()
            queryInstace.replace('\n', '')
            if (queryInstace):
                processedQuery.append(queryInstace)
        self.setUpQueries = processedQuery


async def main():
   sqlCmds = open('SQLComponet/SQLFiles/CreateTables.sql', 'r')
   rawQuery = sqlCmds.read().split(";")
   processedQuery = []
   for query in rawQuery:
       queryInstace = query.strip()
       queryInstace.replace('\n', '')
       if (queryInstace):
           processedQuery.append(queryInstace)

   database = Database('sqlite:///BayesianDataBase.db')
   await database.connect()
   for query in processedQuery:
        print(await database.execute(query=query))

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

   
