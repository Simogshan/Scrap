#!/bin/bash

# Create New Bucket
aws s3 mb s3://directcloudfrontdistribution

# Bucket Public Access
aws s3api put-public-access-block \
    --bucket directcloudfrontdistribution \
    --public-access-block-configuration "BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false"

# Bucket Policy
aws s3api put-bucket-policy --bucket directcloudfrontdistribution --policy "{
  \"Version\": \"2012-10-17\",
  \"Statement\": [
      {
          \"Sid\": \"PublicReadGetObject\",
          \"Effect\": \"Allow\",
          \"Principal\": \"*\",
          \"Action\": \"s3:GetObject\",
          \"Resource\": \"arn:aws:s3:::directcloudfrontdistribution/*\"
      }
  ]
}"

# Host S3 Bucket to Index File
aws s3 website "s3://directcloudfrontdistribution" --index-document check.html

# Copy Path index File
aws s3 cp check.html s3://directcloudfrontdistribution

# Cloudfront Distribution Creation
aws cloudfront create-distribution --origin-domain-name directcloudefrontdistribution.s3.amazonaws.com --default-root-object index.html
