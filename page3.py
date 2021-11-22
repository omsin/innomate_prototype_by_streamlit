from helper_function import *

def page_three():
    st.title("Design Analytics")

    uploaded_file = st.file_uploader("Choose a image file", type=['png', 'jpeg', 'jpg'])
    if uploaded_file is not None:
        with open(os.path.join("image_temp", "temp.jpg"), "wb") as f:
            f.write((uploaded_file).getbuffer())

        st.image(uploaded_file, width=300)

    if st.button('Detect'):

        s3 = boto3.client('s3')
        s3.upload_file("image_temp/temp.jpg", "omsin", "myPhoto.jpg")

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

        photo1 = cv2.imread("image_temp/temp.jpg")
        imgHeight, imgWidth, channels = photo1.shape

        # print(imgHeight)
        # print(imgWidth)

        # To get the dimensions of the bounding box
        colors = [(247, 202, 201), (146, 168, 209), (200, 120, 55), (60, 200, 0), (0, 50, 200)]
        for i in range(0, maxlabels):
            st.caption(response['Labels'][i]["Name"])
            if (len(response['Labels'][i]["Instances"]) != 0):
                noOfBoundingBox = len(response['Labels'][i]["Instances"])
                for j in range(0, noOfBoundingBox):
                    dimensions = (response['Labels'][i]["Instances"][j]["BoundingBox"])
                    # Storing them in variables
                    boxWidth = dimensions['Width']
                    boxHeight = dimensions['Height']
                    boxLeft = dimensions['Left']
                    boxTop = dimensions['Top']
                    # Plotting points of rectangle
                    start_point = (int(boxLeft * imgWidth), int(boxTop * imgHeight))
                    end_point = (
                        int((boxLeft + boxWidth) * imgWidth), int((boxTop + boxHeight) * imgHeight))
                    # Drawing Bounding Box on the coordinates
                    color = colors[i]
                    thickness = 2
                    image = cv2.rectangle(photo1, start_point, end_point, color, thickness)
                    cv2.imwrite('image_temp/temp_labelled.jpg', image)

        image = Image.open('image_temp/temp_labelled.jpg')
        st.image(image, width=300)
