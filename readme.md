**Load Data**
```
curl -X POST \
    -H 'Content-Type: application/json' \
    <clusterURL>:<Cluster Port>/loader -d '
    {
      "source" : "<YOUR-S3-BUCKET>",
      "format" : "<format>",
      "iamRoleArn" : "<NeptuneLoadFromS3ARN>",
      "region" : "<region>", 
      "failOnError" : "FALSE",
      "parallelism" : "MEDIUM"
    }'
```

After entering the above, you will get something like this back:
```
{
    "status" : "200 OK",
    "payload" : {
        "loadId" : "ef478d76-d9da-4d94-8ff1-08d9d4863aa5"
    }
}
```
To confirm that the data was loaded correctly, run the follow code replace '<loadId>' with the load ID from the response:
```
curl -G '<YOUR-CLUSTER>:<CLUSTER-PORT>/loader/<loadId>'
```