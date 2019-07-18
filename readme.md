# CloudFormation Setup
1. Place `cf.yaml`, `cf-base.yaml`, and `cf-ec2.yaml` into an S3 bucket in your AWS account.
2. Go to CloudFormation inside the AWS Console. Create a new stack, load from S3, and input the URL to the `cf.yaml` file in your S3 bucket.
3. Fill out the EC2SSHKeyPairName and CloudFormationS3Path parameters

      For the CloudFormationS3Path, follow this example: https://your-bucket-name.s3.amazonaws.com/

# Loading Data
1. Upload data into a S3 bucket. (sample data is provided in `sample-data`).
2. SSH into your EC2 instance created earlier.
3. Run the following command, replacing the correct values (most of these can be found from the outputs of the CloudFormation stack). NOTE: For the source, you can put a path to specific folder and Neptune will automatically load all of the data files from within that folder.
```bash
curl -X POST \
    -H 'Content-Type: application/json' \
    `http://<clusterURL>:<Cluster Port>/loader -d '
    {
      "source" : "<YOUR-S3-BUCKET>/<OBJECT-KEY-NAME>",
      "format" : "<format>", #csv, ntriples, nquads, rdfxml, turtle, etc.
      "iamRoleArn" : "<NeptuneLoadFromS3ARN>",
      "region" : "<region>", #us-east-1
      "failOnError" : "FALSE",
      "parallelism" : "MEDIUM"
    }'
```

4. After entering the above, you will get something like this back:
```bash
{
    "status" : "200 OK",
    "payload" : {
        "loadId" : "ef478d76-d9da-4d94-8ff1-08d9d4863aa5"
    }
}
```
To confirm that the data was loaded correctly, run the follow code replacing '<loadId>' with the load ID from the response:
```bash
curl -G '<YOUR-CLUSTER>:<CLUSTER-PORT>/loader/<loadId>'
```

# Lambda function
1. Use the following AWS provided stack to create a lambda function use in Neptune: https://docs.aws.amazon.com/neptune/latest/userguide/get-started-cfn-lambda.html. Make sure to enter the NeptuneClusterEndpoint and select the NeptuneClientSG and the correct Subnets.
2. 