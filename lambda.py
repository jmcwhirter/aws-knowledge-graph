from __future__  import print_function
import json
import boto3
import os, sys
from gremlin_python import statics
from gremlin_python.structure.graph import Graph
from gremlin_python.process.graph_traversal import __
from gremlin_python.process.strategies import *
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
import urllib.request
import requests

CLUSTER_ENDPOINT = os.environ['CLUSTER_ENDPOINT']
CLUSTER_PORT = os.environ['CLUSTER_PORT']

       
def lambda_handler(event, context):
    path = event['path']
    
    url = 'http://' + CLUSTER_ENDPOINT + ':' + CLUSTER_PORT # '?gremlin=g.V()'
        
    if (path == '/nodes'):
        url += '?gremlin=g.V()'
    if (path == '/edges'):
        url += '?gremlin=g.E()'
        
    response = requests.get(url)
    data = response.json()['result']
    
    result = {}
    result['statusCode'] = 200
    result['headers'] = {
        'Content-Type': 'application/json', 
        'Access-Control-Allow-Origin': '*',
        "Access-Control-Allow-Credentials" : True
    }
    
    result['body'] = str(data)
    
    print(result)
    return result