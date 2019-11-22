# selfless-service-updates

Amazon ElastiCache recently added
[self-service updates](https://aws.amazon.com/about-aws/whats-new/2019/06/elasticache-self-service-updates/).
This revolutionary new feature allows you manually manage updates on your
managed cache cluster.

Now, as much as I enjoyed waking up at 4am to hit "Apply Update", everybody
knows:  If you love something, automate it.  This simple Lambda function checks
for any outstanding self-service updates and applies them.  A CloudWatch Events
scheduled expression can run this Lambda function during a "maintenance
window."
