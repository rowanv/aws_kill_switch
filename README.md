# aws_kill_switch
A serverless application for killing pre-defined AWS services that go over a budget limit.


## Deploy Instructions

Package CloudFormation serverless app:
```
aws cloudformation package --template-file template.yaml --s3-bucket <MY_BUCKET_NAME> --output-template-file packaged-template.yaml
```

Deploy the packaged app (sample invocation if packaged it into EC2):
```
aws cloudformation deploy \
--template-file /home/ec2-user/workspace/aws_kill_switch/packaged-template.yaml \
--stack-name aws-kill-switch-stack \
--capabilities CAPABILITY_IAM \
--region us-east-1
```