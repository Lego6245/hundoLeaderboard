import sys
import json
import os
from azure.cosmosdb.table.tableservice import TableService
from datetime import datetime, timedelta

def main():
  connection_string = sys.argv[1]
  print('connection string loaded')
  table_service = TableService(connection_string=connection_string)
  entities = table_service.query_entities('fastestLeaderboard', "PartitionKey eq 'frameCount'")
  
  entityList = list(entities)
  
  entityList.sort(key=lambda e: (e.numFrames.value, e.Timestamp))

  def mapper(e):
    mapped = {}
    mapped['userName'] = e.RowKey
    mapped['frameCount'] = e.numFrames.value
    mapped['timeStamp'] = e.Timestamp.strftime("%m/%d/%Y %H:%M:%S")
    return mapped

  mappedEntities = list(map(mapper, entityList))[:50]
  
  lastRunTime = datetime.now()
  if os.path.isfile('src/data/current.json'):
    timeString = lastRunTime.strftime("%d-%m-%y %H %M")
    os.replace('src/data/current.json', 'src/historical/' + timeString + '.json')
  
  f = open("src/data/current.json", "w+")
  jsonOutput = {}
  jsonOutput['ranAt'] = lastRunTime.strftime("%d-%m-%y %H:%M")
  jsonOutput['entries'] = mappedEntities
  f.write(json.dumps(jsonOutput))
  f.close()

if __name__ == "__main__":
  main()