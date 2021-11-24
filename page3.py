from helper_function import *
from image_recognition import *

def page_three():
    st.title("Design Analytics")

    image1 = Image.open('data/Picture1.png')
    image2 = Image.open('data/Picture2.png')
    image3 = Image.open('data/Picture3.png')


    text1 = "Stay with ROS the best 💚 because we are the number 1 network with the most waves Supports most users Covering all areas throughout Thailand"
    text2 = "monthly package that brings you to a new world Use the mobile internet faster than before, suitable for the 5G era, with a maximum speed of 1Gbps at a starting price of only 699 baht and ready to be used with all 5G smartphones that come in Thailand"
    text3 = "For prepaid customers that last for a lifetime Change top up to ROS 5G monthly, get discounts on smartphones, great prices, special prices Or choose to receive a 50% discount, just change the top-up to monthly, convenient, complete in one place"
    text4 = "Promotion as you wish for prepaid line ROS comes with an as-you-want promotion. Promotion for prepaid people that you can choose from, whether it's the duration of use of the Internet to data packages for use on various applications, I can say that it's very worthwhile"
    text5 = "When you choose ROS Pro Net 12 Months, you will pay 80% cheaper by choosing ROS Pro Net Yearly subscription. To illustrate, I would like to take an example from the ROS daily 2 Mbps speed, priced at 29.96 baht per day, but when you sign up for a year, you will pay at 2,782 baht per year, or an average of 7.62 baht per day, which is 74.57% cheaper than daily. Or if the whole year's amount is 8,153.4 baht, you'll save ten thousand and ten thousand baht a year! Just change from daily to Internet ROS for 12 months only!"


    option1 = st.selectbox(
    'Select your advertising from all campaign on your facebook',
    ('text1', 'text2', 'text3', 'text4', 'text5'))
    st.write('You selected:', option1)

    if option1 == 'text1':
        text = text1
    elif option1 == 'text2':
        text = text2
    elif option1 == 'text3':
        text = text3
    elif option1 == 'text4':
        text = text4
    elif option1 == 'text5':
        text = text5
    st.text_area("",text, height=130)

    option2 = st.selectbox(
    'Select your picture from all campaign on your facebook',
    ('picture1', 'picture2', 'picture3'))
    st.write('You selected:', option2)

    if option2 == 'picture1':
        image = image1
    elif option2 == 'picture2':
        image = image2
    elif option2 == 'picture3':
        image = image3
    st.image(image, width=300)

    str = ", "
    eva = ""
    if st.button('Submit'):
        if option1 == 'text1' and option2 == 'picture1':
            image_result = image_recognition('data/Picture1.png')
            eva = "Text performance => 2/10," \
                  " Image performance => 1/10," \
                  " Overall performance => 2/10" + \
                  ", Detected => [" + str.join(image_result) + "]"
        elif option1 == 'text1' and option2 == 'picture2':
            image_result = image_recognition('data/Picture2.png')
            eva = "Text performance => 2/10," \
                  " Image performance => 6/10," \
                  " Overall performance => 4/10" + \
                  ", Detected => [" + str.join(image_result) + "]"
        elif option1 == 'text1' and option2 == 'picture3':
            image_result = image_recognition('data/Picture3.png')
            eva = "Text performance => 2/10," \
                  " Image performance => 4/10," \
                  " Overall performance => 3/10" + \
                  ", Detected => [" + str.join(image_result) + "]"
        elif option1 == 'text2' and option2 == 'picture1':
            image_result = image_recognition('data/Picture1.png')
            eva = "Text performance => 8/10," \
                  " Image performance => 1/10," \
                  " Overall performance => 5/10" + \
                  ", Detected => [" + str.join(image_result) + "]"
        elif option1 == 'text2' and option2 == 'picture2':
            image_result = image_recognition('data/Picture2.png')
            eva = "Text performance => 8/10," \
                  " Image performance => 6/10," \
                  " Overall performance => 7/10" + \
                  ", Detected => [" + str.join(image_result) + "]"
        elif option1 == 'text2' and option2 == 'picture3':
            image_result = image_recognition('data/Picture3.png')
            eva = "Text performance => 8/10," \
                  " Image performance => 4/10," \
                  " Overall performance => 6/10" + \
                  ", Detected => [" + str.join(image_result) + "]"
        elif option1 == 'text3' and option2 == 'picture1':
            image_result = image_recognition('data/Picture1.png')
            eva = "Text performance => 5/10," \
                  " Image performance => 1/10," \
                  " Overall performance => 3/10" + \
                  ", Detected => [" + str.join(image_result) + "]"
        elif option1 == 'text3' and option2 == 'picture2':
            image_result = image_recognition('data/Picture2.png')
            eva = "Text performance => 5/10," \
                  " Image performance => 6/10," \
                  " Overall performance => 6/10" + \
                  ", Detected => [" + str.join(image_result) + "]"
        elif option1 == 'text3' and option2 == 'picture3':
            image_result = image_recognition('data/Picture3.png')
            eva = "Text performance => 5/10," \
                  " Image performance => 4/10," \
                  " Overall performance => 5/10" + \
                  ", Detected => [" + str.join(image_result) + "]"
        elif option1 == 'text4' and option2 == 'picture1':
            image_result = image_recognition('data/Picture1.png')
            eva = "Text performance => 7/10," \
                  " Image performance => 1/10," \
                  " Overall performance => 4/10" + \
                  ", Detected => [" + str.join(image_result) + "]"
        elif option1 == 'text4' and option2 == 'picture2':
            image_result = image_recognition('data/Picture2.png')
            eva = "Text performance => 7/10," \
                  " Image performance => 6/10," \
                  " Overall performance => 7/10" + \
                  ", Detected => [" + str.join(image_result) + "]"
        elif option1 == 'text4' and option2 == 'picture3':
            image_result = image_recognition('data/Picture3.png')
            eva = "Text performance => 7/10," \
                  " Image performance => 4/10," \
                  " Overall performance => 6/10" + \
                  ", Detected => [" + str.join(image_result) + "]"
        elif option1 == 'text5' and option2 == 'picture1':
            image_result = image_recognition('data/Picture1.png')
            eva = "Text performance => 3/10," \
                  " Image performance => 1/10," \
                  " Overall performance => 2/10" + \
                  ", Detected => [" + str.join(image_result) + "]"
        elif option1 == 'text5' and option2 == 'picture2':
            image_result = image_recognition('data/Picture2.png')
            eva = "Text performance => 3/10," \
                  " Image performance => 6/10," \
                  " Overall performance => 5/10" + \
                  ", Detected => [" + str.join(image_result) + "]"
        elif option1 == 'text5' and option2 == 'picture3':
            image_result = image_recognition('data/Picture3.png')
            eva = "Text performance => 3/10," \
                  " Image performance => 4/10," \
                  " Overall performance => 4/10" + \
                  ", Detected => [" + str.join(image_result) + "]"

    st.text_area("Evaluation",eva, height=80)

    st.button('Next')

    with st.expander("Test Amazon Amazon Rekognition (Amazon Image Recognition)"):
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
            result=[]
            colors = [(247, 202, 201), (146, 168, 209), (200, 120, 55), (60, 200, 0), (0, 50, 200)]
            for i in range(0, len(response['Labels'])):
                result.append(response['Labels'][i]["Name"])
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
            st.write(result)
            image = Image.open('image_temp/temp_labelled.jpg')
            st.image(image, width=300)
