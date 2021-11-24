from helper_function import *

def image_recognition(image):
        s3 = boto3.client('s3')
        s3.upload_file(image, "omsin", "myPhoto.jpg")

        maxlabels = 5
        rekognition = boto3.client('rekognition')
        response = rekognition.detect_labels(
            Image={
                'S3Object': {
                    'Bucket': 'omsin',
                    'Name': 'myPhoto.jpg',
                }
            },
            MaxLabels=maxlabels,
            MinConfidence=80)
        result = []
        for i in range(0, len(response['Labels'])):
            result.append(response['Labels'][i]["Name"])

        return result
