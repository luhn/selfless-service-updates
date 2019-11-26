# selfless-service-updates

Amazon ElastiCache recently added
[self-service updates](https://aws.amazon.com/about-aws/whats-new/2019/06/elasticache-self-service-updates/).
This revolutionary new feature allows you manually manage updates on your
managed cache cluster.

Now, as much as I enjoyed waking up at 4am to hit "Apply Update", everybody
knows:  If you love something, automate it.  This simple Lambda function checks
for any outstanding self-service updates and applies them.  A CloudWatch Events
scheduled expression will run this Lambda function at 10:00 UTC every Monday,
but can be set to your preferred time.

## Deploying

For easy deployment, check out this project on the
[AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:466565666523:applications~selfless-service-updates).
To customize the scheduled time, set "CronExpression" under "Application
Settings" to the desired
[cron expression](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions).

You can also build and deploy yourself using SAM.

```sh
sam deploy --guided
```
