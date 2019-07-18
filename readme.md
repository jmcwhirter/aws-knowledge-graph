**Load Data**
```curl -X POST \
    -H 'Content-Type: application/json' \
    <b><clusterURL></b>:<b><Cluster Port></b>/loader -d '
    {
      "source" : "<b><YOUR-S3-BUCKET></b>",
      "format" : "<b><format></b>",
      "iamRoleArn" : "<b><NeptuneLoadFromS3ARN></b>",
      "region" : "<b><region></b>", 
      "failOnError" : "FALSE",
      "parallelism" : "MEDIUM"
    }'```

After entering the above, you will get something like this back:
```{
    "status" : "200 OK",
    "payload" : {
        "loadId" : "<b>ef478d76-d9da-4d94-8ff1-08d9d4863aa5</b>"
    }
}```