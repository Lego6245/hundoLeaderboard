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

  def sorter(e):
    return e.numFrames.value
  
  entityList.sort(key=sorter)

  def mapper(e):
    mapped = {}
    mapped['userName'] = e.RowKey
    mapped['frameCount'] = e.numFrames.value
    return mapped

  mappedEntities = list(map(mapper, entityList))
  
  lastRunTime = datetime.now()
  if os.path.isfile('current.json'):
    timeString = lastRunTime.strftime("%d-%m-%y %H %M")
    os.replace('current.json', 'historical/' + timeString + '.json')
  
  f = open("current.json", "w+")
  jsonOutput = {}
  jsonOutput['ranAt'] = lastRunTime.strftime("%d-%m-%y %H:%M")
  jsonOutput['entries'] = mappedEntities
  f.write(json.dumps(jsonOutput))
  f.close()

if __name__ == "__main__":
  main()