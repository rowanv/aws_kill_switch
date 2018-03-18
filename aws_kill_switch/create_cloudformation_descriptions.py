from troposphere import Template, Output, Ref, cloudwatch



ALL_SERVICES_BILLING_ALARM_LIMIT = 10




t = Template()

t.add_description(
	"A set of serverless Lambda functions that shut down services that exceed"
	" billing limits. **WARNING** This template creates Lambda functions and "
	"Amazon CloudWatch alarms. You will be billed for the AWS resources used "
	"if you create a stack from this template."
)

if ALL_SERVICES_BILLING_ALARM_LIMIT:

	exceed_billing_limit_alarm = t.add_resource(
		cloudwatch.Alarm('AllServicesBillingAlarm',
			AlarmDescription='Alarm if all services exceed billing limit',
			Namespace='AWS/Billing',
			MetricName='EstimatedCharges',
			Dimensions=[
				cloudwatch.MetricDimension(
					Name='Currency',
					Value='USD'
				),
			],
			Statistic='Maximum',
			Period='300',
			EvaluationPeriods='1',
			Threshold=str(ALL_SERVICES_BILLING_ALARM_LIMIT),
			ComparisonOperator='GreaterThanThreshold',
			#AlarmActions=Ref('BillingAlarmNotification'),
			#InsufficientDataActions=Ref('BillingAlarmNotification'),
			)
		)


print(t.to_yaml())

#with open('aws_kill_switch_cloudfront.yaml', 'w') as f:
#    f.write(t.to_yaml())
