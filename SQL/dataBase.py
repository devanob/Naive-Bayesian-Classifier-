from databases import Database
import asyncio

class DataBaseComponet:

    def __init__(self):
        #create database connection 
         self.database = Database('sqlite:///BayesianDataBase.db')
         #get event loop
         self.eventLoop = asyncio.get_event_loop()
     
    async def setUpDataBase(self):
        pass


async def main():
    database = Database('sqlite:///BayesianDataBase.db')
    await database.connect()
    query = "CREATE TABLE IF NOT EXISTS ClassificationType \
    (ID  INTEGER PRIMARY KEY, Classification VARCHAR(200) )"
    result = await database.execute(query=query)
    insert = "INSERT INTO ClassificationType (Classification) VALUES ('Hellohvhvhvhvhvhvhvtycycycycycg')"
    result = await database.execute(query=insert)
    getRows= "Select * from ClassificationType"
    result= await database.fetch_all(query=getRows)
    print(result)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
   