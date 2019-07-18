**Load Data**
```curl -X POST \
    -H 'Content-Type: application/json' \
    <clusterURL>:<Cluster Port>/loader -d '
    {
      "source" : "s3://neptune-test-dmmaillo",
      "format" : "csv",
      "iamRoleArn" : "arn:aws:iam::759449822753:role/NeptuneQuickStart-NeptuneSta-NeptuneLoadFromS3Role-10KS4DTXW96IS",
      "region" : "us-east-1",
      "failOnError" : "FALSE",
      "parallelism" : "MEDIUM"
    }'```