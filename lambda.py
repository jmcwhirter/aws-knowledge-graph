from __future__  import print_function
import boto3
import os, sys
from gremlin_python import statics
from gremlin_python.structure.graph import Graph
from gremlin_python.structure.graph import *
from gremlin_python.process.graph_traversal import __
from gremlin_python.process.strategies import *
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
import requests

CLUSTER_ENDPOINT = os.environ['CLUSTER_ENDPOINT']
CLUSTER_PORT = os.environ['CLUSTER_PORT']

def run_sample_gremlin_websocket():
    print('running sample gremlin websocket code')
    remoteConn = DriverRemoteConnection('ws://' + CLUSTER_ENDPOINT + ":" + CLUSTER_PORT + '/gremlin','g')
    graph = Graph()
    g = graph.traversal().withRemote(remoteConn)
    
    #create and open a log file
    f = open("/tmp/output.txt", "w+")


    #Listing verticies/edges and properties
    vertList = g.V().toList()
    numVerticies = g.V().count().next()
    f.write('Number of verticies: '+ str(numVerticies) + '\n')
    f.write('\n----------------------------------------\n')
    f.write('All verticies and their properties:' + '\n')
    for v in vertList:
        f.write(str(v.label) + ': '+ str(v.id) + '\n')
        f.write(str(g.V(v.id).properties().toList()) + '\n\n')
    
    f.write('\n----------------------------------------\n')
    f.write('All Edges and their weights: \n')
    edgeList = g.E().toList()
    for e in edgeList:
        f.write(str(e) + '\n')
        f.write(str(g.E(e.id).properties().toList()) + '\n\n')
    f.write('\n----------------------------------------\n')
    
    #Filtering
    f.write('All Adventure Games:' + '\n')
    advGames = g.V().has('GameGenre','Adventure').toList()
    for game in advGames:
        f.write(game.id + '\n')
    
    f.write('\n----------------------------------------\n')
    f.write('\nThe following users like MarioKart8:' + '\n')
    mKart = g.V('MarioKart8').inE().toList()
    for u in mKart:
        f.write(u.outV.id + '\n')
        
    f.write('\n----------------------------------------\n')
    f.close()
    s3_client = boto3.client('s3')
    s3_client.upload_file("/tmp/output.txt", 'neptune-test-dmmaillo', 'output.txt')
    remoteConn.close()
    
def run_sample_gremlin_http():
    print('running sample gremlin http code')
    URL = 'http://' + CLUSTER_ENDPOINT + ":" + CLUSTER_PORT + '/gremlin'
    r = requests.post(URL,data='{"gremlin":"g.V().count()"}')
    print(r.text)

def lambda_handler(event, context):
    print(event)
    print('hello from lambda handler')

    ## run gremlin query
    if CLUSTER_ENDPOINT and CLUSTER_PORT:
        run_sample_gremlin_websocket()
        run_sample_gremlin_http()
    else:
        print("provide CLUSTER_ENDPOINT and CLUSTER_PORT environment varibles")

    return "done"