# import cv2
# import numpy as np
# import streamlit as st

# def app():

    # st.title("Total Grain Count Detection")
    # photo = st.camera_input("Upload an image containing grains to count them.")

    # if photo is not None:
    #     file_bytes = np.asarray(bytearray(photo.read()), dtype=np.uint8)
    #     image = cv2.imdecode(file_bytes, 1)
    #     image_resized = cv2.resize(image, (600, 600))
    #     gray_image = cv2.cvtColor(image_resized, cv2.COLOR_BGR2GRAY)
    #     blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    #     # Threshold Parameters
    #     block_size = st.slider("Adaptive Threshold Block Size", 3, 21, 11, 2)
    #     c_value = st.slider("Adaptive Threshold Constant", -10, 10, 2, 1)
    #     thresh_image = cv2.adaptiveThreshold(
    #         blurred_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, block_size, c_value
    #     )

    #     # Morphological Parameters
    #     kernel_size = st.slider("Kernel Size for Morphology", 1, 15, 5, 2)
    #     kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))
    #     morphed_image = cv2.morphologyEx(thresh_image, cv2.MORPH_CLOSE, kernel)

    #     # Contour Filtering
    #     contours, _ = cv2.findContours(morphed_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #     min_area = st.slider("Minimum Area Threshold", 10, 300, 50, 10)
    #     filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_area]

    #     # Count and Draw Contours
    #     total_grains = len(filtered_contours)
    #     image_copy = image_resized.copy()
    #     for cnt in filtered_contours:
    #         cv2.drawContours(image_copy, [cnt], -1, (0, 255, 0), 2)

        # # Display Results
        # font = cv2.FONT_HERSHEY_SIMPLEX
        # cv2.putText(image_copy, f"Total Count: {total_grains}", (20, 50), font, 1, (255, 0, 0), 2)
        # _, img_encoded = cv2.imencode('.png', image_copy)
        # st.image(img_encoded.tobytes(), caption="Processed Image with Total Count", use_column_width=True)

        # st.subheader("Thresholded Image")
        # _, thresh_encoded = cv2.imencode('.png', thresh_image)
        # st.image(thresh_encoded.tobytes(), use_column_width=True)

        # st.subheader("Morphed Image")
        # _, morphed_encoded = cv2.imencode('.png', morphed_image)
        # st.image(morphed_encoded.tobytes(), use_column_width=True)

        # st.write(f"## Total number of grains detected: {total_grains}")

# import firebase_admin
# from PIL import Image
# import cv2
# import numpy as np

# def app():

#     if 'db' not in st.session_state:
#         st.session_state.db = ''

#     db = firestore.client()
#     st.session_state.db = db

#     if 'storage' not in st.session_state:
#         st.session_state.storage = ''

#     if 'app' not in st.session_state:
#         st.session_state.app = ''

#     if st.session_state.app == '':
#         cred = firebase_admin.credentials.Certificate('sample-cv-project-1cc3de5db707.json')  
#         st.session_state.app = firebase_admin.initialize_app(cred, {
#             'storageBucket': 'https://console.firebase.google.com/u/0/project/sample-cv-project/storage/sample-cv-project.firebasestorage.app/files?fb_gclid=Cj0KCQiA7NO7BhDsARIsADg_hIa8e6o8tK9pDe36LSWUAdg0gpZmhm0mlVjs8_ERiRmVHAP4Wba018saAjZVEALw_wcB'  # Replace with your storage bucket name
#         })
#         st.session_state.storage = storage.bucket()

#     ph = ''
#     if st.session_state.username == '':
#         ph = 'Login to be able to post!!'
#     else:
#         ph = 'Upload an image'

#     photo = st.camera_input("Upload an image containing grains to count them.")

#     if st.button('Upload', use_container_width=20):

#         if photo is not None:

#             try:
#                 image = Image.open(photo)
#                 image_bytes = image.tobytes()

#                 # Generate a unique filename
#                 filename = f"{st.session_state.username}_{photo.name}"

#                 # Upload image to Firebase Storage
#                 blob = st.session_state.storage.blob(filename)
#                 blob.upload_from_string(image_bytes)

#                 # Store image URL in Firestore
#                 doc_ref = db.collection('Images').document(st.session_state.username)
#                 doc_ref.set({
#                     'ImageUrl': f"gs://{st.session_state.storage.bucket.name}/{filename}",
#                     'Username': st.session_state.username
#                 }, merge=True)

#                 st.success('Image captured successfully!')

#                 butto = st.button("Analyze")

#                 if butto:

#                     file_bytes = np.asarray(bytearray(photo.read()), dtype=np.uint8)
#                     image = cv2.imdecode(file_bytes, 1)
#                     image_resized = cv2.resize(image, (600, 600))
#                     gray_image = cv2.cvtColor(image_resized, cv2.COLOR_BGR2GRAY)
#                     blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

#                     # Threshold Parameters
#                     block_size = st.slider("Adaptive Threshold Block Size", 3, 21, 11, 2)
#                     c_value = st.slider("Adaptive Threshold Constant", -10, 10, 2, 1)
#                     thresh_image = cv2.adaptiveThreshold(
#                         blurred_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, block_size, c_value
#                     )

#                     # Morphological Parameters
#                     kernel_size = st.slider("Kernel Size for Morphology", 1, 15, 5, 2)
#                     kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))
#                     morphed_image = cv2.morphologyEx(thresh_image, cv2.MORPH_CLOSE, kernel)

#                     # Contour Filtering
#                     contours, _ = cv2.findContours(morphed_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#                     min_area = st.slider("Minimum Area Threshold", 10, 300, 50, 10)
#                     filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_area]

#                     # Count and Draw Contours
#                     total_grains = len(filtered_contours)
#                     image_copy = image_resized.copy()
#                     for cnt in filtered_contours:
#                         cv2.drawContours(image_copy, [cnt], -1, (0, 255, 0), 2)


#                     # Display Results
#                     font = cv2.FONT_HERSHEY_SIMPLEX
#                     cv2.putText(image_copy, f"Total Count: {total_grains}", (20, 50), font, 1, (255, 0, 0), 2)
#                     _, img_encoded = cv2.imencode('.png', image_copy)
#                     st.image(img_encoded.tobytes(), caption="Processed Image with Total Count", use_column_width=True)

#                     st.subheader("Thresholded Image")
#                     _, thresh_encoded = cv2.imencode('.png', thresh_image)
#                     st.image(thresh_encoded.tobytes(), use_column_width=True)

#                     st.subheader("Morphed Image")
#                     _, morphed_encoded = cv2.imencode('.png', morphed_image)
#                     st.image(morphed_encoded.tobytes(), use_column_width=True)

#                     st.write(f"## Total number of grains detected: {total_grains}")


#             except Exception as e:
#                 st.error(f"Error in capturing image: {e}")

    # st.header(' :violet[Latest Images] ')

    # docs = db.collection('Images').get()

    # for doc in docs:
    #     d = doc.to_dict()
    #     try:
    #         st.markdown("""
    #             <style>
    #                 .stTextArea [data-baseweb=base-input] [disabled=""]{
    #                     # background-color: #e3d8c8;
    #                     -webkit-text-fill-color: white;
    #                 }
    #             </style>
    #             """, unsafe_allow_html=True)

    #         st.image(d['ImageUrl'], caption=':green[Uploaded by:] '+':orange[{}]'.format(d['Username']), use_column_width=True)

    #     except:
    #         pass

# if __name__ == "__main__":
#     app()


# ------------------------------------ ############## @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# -################## ---------- ~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~ ?//////////////////////9 **************************************************************
# +++++++++++++++ ################ ++++++ ____________


# import streamlit as st
# from firebase_admin import credentials, firestore, storage
# import firebase_admin
# from PIL import Image
# import cv2
# import numpy as np

# def app():      

# Initialize Firestore client
#   cred = firebase_admin.credentials.Certificate('sample-cv-project-firebase-adminsdk-ll15m-e016750a30.json')
#   db = firestore.client()
#   st.session_state.db = db

#   # Initialize Firebase app with storage bucket details (replace with your actual value)
#   if st.session_state.app == '':
#     st.session_state.app = firebase_admin.initialize_app(cred, {
#         'storageBucket': 'gs://sample-cv-project.firebasestorage.app'
#     })
    
#     # st.session_state.storage = storage.bucket('sample-cv-project.firebasestorage.app')
#     st.session_state.storage = storage.bucket()
#     blob = st.session_state.storage.blob('sample-cv-project.firebasestorage.app.name')  
#     blob.upload_from_string(image_bytes)


# Load Firebase credentials
    # cred = credentials.Certificate('sample-cv-project-firebase-adminsdk-ll15m-e016750a30.json')

    # # Initialize Firebase app with storage bucket details
    # if 'app' not in st.session_state:
    #     st.session_state.app = firebase_admin.initialize_app(cred, {
    #         'storageBucket': 'sample-cv-project.appspot.com'  # Ensure this is the correct bucket name
    #     })

    # # Initialize Firestore client and store in session state
    # if 'db' not in st.session_state:
    #     st.session_state.db = firestore.client()

    # # Initialize Storage client and store in session state
    # if 'storage' not in st.session_state:
    #     st.session_state.storage = storage.bucket()

    # # User feedback based on login status
    # ph = ''
    # if 'username' not in st.session_state or st.session_state.username == '':
    #     ph = 'Login to be able to post!!'
    # else:
    #     ph = 'Upload an image'

    # photo = st.camera_input("Take a photo of Red grams.")

    # if st.button('Upload', use_container_width=True):
    #     if photo is not None:
    #         try:
    #             # Read the image data
    #             image_bytes = photo.read()

    #             # Generate a unique filename
    #             filename = f"{st.session_state.username}_{photo.name}"

    #             # Upload image to Firebase Storage
    #             blob = st.session_state.storage.blob(filename)
    #             blob.upload_from_string(image_bytes)

    #             # Store image URL in Firestore
    #             doc_ref = st.session_state.db.collection('Images').document(st.session_state.username)
    #             doc_ref.set({
    #                 'ImageUrl': f"gs://{st.session_state.storage.bucket.name}/{filename}",
    #                 'Username': st.session_state.username
    #             }, merge=True)

    #             st.success("Image uploaded successfully!")



# ---------- # ############## ~~~~~~~~~~~~~~~ -------------
# 000000000000000000 &&&&&&&&&&&&&&&&&&&&&&&&&&& -------------------------------- #


    # cred = credentials.Certificate('sample-cv-project-firebase-adminsdk-ll15m-e016750a30.json')

    # # Initialize Firebase app with storage bucket details (replace with your actual value)
    # if 'app' not in st.session_state:
    #     st.session_state.app = firebase_admin.initialize_app(cred, {
    #         'storageBucket': 'gs://sample-cv-project.firebasestorage.app'  # Ensure this is the correct bucket name
    #     })

    # # Initialize Firestore client and store in session state
    # if 'db' not in st.session_state:
    #     st.session_state.db = firestore.client()

    # # Initialize Storage client and store in session state
    # if 'storage' not in st.session_state:
    #     st.session_state.storage = storage.bucket()

    # # Upload an image (ensure image_bytes is defined)
    # blob = st.session_state.storage.blob('sample-cv-project.firebasestorage.app.name')  
    # blob.upload_from_string(image_bytes)

    # ph = ''
    # if st.session_state.username == '':
    #     ph = 'Login to be able to post!!'
    # else:
    #     ph = 'Upload an image'

    # photo = st.camera_input("Take a photo of Red grams.")

    # if st.button('Upload', use_container_width=20):

    #     if photo is not None:

    #         try:
    #             # Handle potential string input for photo
    #             if isinstance(photo, str):
    #                 # Download the image from the URL
    #                 # ... (Implement image download logic here) ...
    #                 st.error("Downloading from URL is not currently supported.")
    #                 return

    #             # Read the image data
    #             image_bytes = photo.read()

    #             # Generate a unique filename
    #             filename = f"{st.session_state.username}_{photo.name}"

    #             # Upload image to Firebase Storage
    #             blob = st.session_state.storage.blob(filename)
    #             blob.upload_from_string(image_bytes)

    #             # Store image URL in Firestore
    #             doc_ref = db.collection('Images').document(st.session_state.username)
    #             doc_ref.set({
    #                 'ImageUrl': f"gs://{st.session_state.storage.bucket.name}/{filename}",
    #                 'Username': st.session_state.username
    #             }, merge=True)


#                 butto = st.button("Analyze")

#                 if butto:
#                     # ... (Image analysis and display code) ...
#                     file_bytes = np.asarray(bytearray(photo.read()), dtype=np.uint8)
#                     image = cv2.imdecode(file_bytes, 1)
#                     image_resized = cv2.resize(image, (600, 600))
#                     gray_image = cv2.cvtColor(image_resized, cv2.COLOR_BGR2GRAY)
#                     blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

#                     # Threshold Parameters
#                     block_size = st.slider("Adaptive Threshold Block Size", 3, 21, 11, 2)
#                     c_value = st.slider("Adaptive Threshold Constant", -10, 10, 2, 1)
#                     thresh_image = cv2.adaptiveThreshold(
#                         blurred_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, block_size, c_value
#                     )

#                     # Morphological Parameters
#                     kernel_size = st.slider("Kernel Size for Morphology", 1, 15, 5, 2)
#                     kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))
#                     morphed_image = cv2.morphologyEx(thresh_image, cv2.MORPH_CLOSE, kernel)

#                     # Contour Filtering
#                     contours, _ = cv2.findContours(morphed_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#                     min_area = st.slider("Minimum Area Threshold", 10, 300, 50, 10)
#                     filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_area]

#                     # Count and Draw Contours
#                     total_grains = len(filtered_contours)
#                     image_copy = image_resized.copy()
#                     for cnt in filtered_contours:
#                         cv2.drawContours(image_copy, [cnt], -1, (0, 255, 0), 2)


#             except Exception as e:
#                 st.error(f"Error in capturing image: {e}")

#     # ... (Displaying uploaded images code) ...

#     st.header(' :violet[Latest Images] ')

#     docs = d.collection('Images').get()

#     for doc in docs:
#         d = doc.to_dict()
#         try:
#             st.markdown("""
#                 <style>
#                     .stTextArea [data-baseweb=base-input] [disabled=""]{
#                         # background-color: #e3d8c8;
#                         -webkit-text-fill-color: white;
#                     }
#                 </style>
#                 """, unsafe_allow_html=True)

#             st.image(d['ImageUrl'], caption=':green[Uploaded by:] '+':orange[{}]'.format(d['Username']), use_column_width=True)

#         except:
#             pass

# if __name__ == "__main__":
#     app()


# _________________ ######################### ------------------------

# $$$$$$$$$$$$$ %%%%%%%%% &&&&&&&&&&&&&&&&&&&& 0000000000000000


# import firebase_admin
# from firebase_admin import credentials, firestore, storage
# import streamlit as st
# import numpy as np
# import cv2


# def app():

#     # Load Firebase credentials
#     cred = credentials.Certificate('sample-cv-project-firebase-adminsdk-ll15m-e016750a30.json')

#     # Initialize Firebase app with storage bucket details
#     if 'app' not in st.session_state:
#         st.session_state.app = firebase_admin.initialize_app(cred, {
#             'storageBucket': 'gs://sample-cv-project.firebasestorage.app'  # Ensure this is the correct bucket name
#         })

#     # Initialize Firestore client and store in session state
#     if 'db' not in st.session_state:
#         st.session_state.db = firestore.client()
 
#     # Initialize Storage client and store in session state
#     if 'storage' not in st.session_state:
#         st.session_state.storage = storage.bucket()

#     # User feedback based on login status
#     ph = ''
#     if 'username' not in st.session_state or st.session_state.username == '':
#         ph = 'Login to be able to post!!'
#     else:
#         ph = 'Upload an image'

#     photo = st.camera_input("Take a photo of Red grams.")

#     if st.button('Upload', use_container_width=True):
#         if photo is not None:
#             try:
#                 # Read the image data
#                 image_bytes = photo.read()



#                 # Generate a unique filename
#                 filename = f"{st.session_state.username}_{photo.name}"

#                 # Upload image to Firebase Storage
#                 blob = st.session_state.storage.blob(filename)
#                 blob.upload_from_string(image_bytes)

#                 # Store image URL in Firestore
#                 doc_ref = st.session_state.db.collection('Images').document(st.session_state.username)
#                 doc_ref.set({
#                     'ImageUrl': f"gs://{st.session_state.storage.bucket.name}/{filename}",
#                     'Username': st.session_state.username
#                 }, merge=True)

#                 st.success("Image uploaded successfully!")

#                 butto = st.button("Analyze")

#                 if butto:
#                     # Image analysis code here
#                     file_bytes = np.asarray(bytearray(photo.read()), dtype=np.uint8)
#                     image = cv2.imdecode(file_bytes, 1)
#                     image_resized = cv2.resize(image, (600, 600))
#                     gray_image = cv2.cvtColor(image_resized, cv2.COLOR_BGR2GRAY)
#                     blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

#                     # Threshold Parameters
#                     block_size = st.slider("Adaptive Threshold Block Size", 3, 21, 11, 2)
#                     c_value = st.slider("Adaptive Threshold Constant", -10, 10, 2, 1)
#                     thresh_image = cv2.adaptiveThreshold(
#                         blurred_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, block_size, c_value
#                     )

#                     # Morphological Parameters
#                     kernel_size = st.slider("Kernel Size for Morphology", 1, 15, 5, 2)
#                     kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))
#                     morphed_image = cv2.morphologyEx(thresh_image, cv2.MORPH_CLOSE, kernel)

#                     # Contour Filtering
#                     contours, _ = cv2.findContours(morphed_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#                     min_area = st.slider("Minimum Area Threshold", 10, 300, 50, 10)
#                     filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_area]

#                     # Count and Draw Contours
#                     total_grains = len(filtered_contours)
#                     image_copy = image_resized.copy()
#                     for cnt in filtered_contours:
#                         cv2.drawContours(image_copy, [cnt], -1, (0, 255, 0), 2)

#             except Exception as e:
#                 st.error(f"Error in capturing image: {e}")

#     # Displaying uploaded images code

#     st.header(' :violet[Latest Images] ')
#     images_collection_ref = st.session_state.db.collection('Images').get()  # Use a different variable name

#     for doc in images_collection_ref:
#         doc_data = doc.to_dict()  # Use a different variable name for document data
#         try:
#             st.markdown("""
#                 <style>
#                     .stTextArea [data-baseweb=base-input] [disabled=""]{
#                         -webkit-text-fill-color: white;
#                     }
#                 </style>
#                 """, unsafe_allow_html=True)

#             st.image(doc_data['ImageUrl'], caption=':green[Uploaded by:] '+':orange[{}]'.format(doc_data['Username']), use_column_width=True)

#         except Exception as e:
#             st.error(f"Error displaying image: {e}")

# if __name__ == "__main__":
#     app()


# -+++++++++++++++++++++++-------- ############# 0___________________________

# -------- %%%%%%%%%%%%%%%%%%%%%%% ***************** -_____-_-___-__

import firebase_admin
from firebase_admin import credentials, firestore, storage
import streamlit as st
import numpy as np
import cv2
import time
from streamlit_lottie import st_lottie
import json

# Initialize Firebase Admin SDK globally
if not firebase_admin._apps:
    cred = credentials.Certificate('sample-cv-project-firebase-adminsdk-ll15m-e016750a30.json')
    firebase_admin.initialize_app(cred, {'storageBucket': 'sample-cv-project.appspot.com'})


def app():

    st.write("## Capture and Analyze")
    st.write("\n")
    
    with open("animation5.json") as source:
        animation = json.load(source)

    st_lottie(animation, width = 800)

    st.write("\n")
    st.write("---")


    # Initialize Firestore and Storage clients
    if 'db' not in st.session_state:
        st.session_state.db = firestore.client()

    if 'storage' not in st.session_state:
        st.session_state.storage = storage.bucket()

    # User feedback based on login status
    if 'username' not in st.session_state or not st.session_state.username:
        st.warning("Login to be able to post!")
        return
    else:
        st.success(f"Welcome, {st.session_state.username}! You can upload images.")

    # Capture image from camera
    photo = st.camera_input("Take a photo of Red grams.")

    if photo and st.button('Upload', use_container_width=True):
        try:
            # Read image data
            image_bytes = photo.read()

            # Generate a unique filename
            timestamp = int(time.time())
            filename = f"{st.session_state.username}_{timestamp}.jpg"

            # Upload image to Firebase Storage
            blob = st.session_state.storage.blob(filename)
            blob.upload_from_string(image_bytes)

            # Get public URL of uploaded image
            image_url = f"https://firebasestorage.googleapis.com/v0/b/sample-cv-project.appspot.com/o/{filename}?alt=media"

            # Save image metadata in Firestore
            doc_ref = st.session_state.db.collection('Images').document(f"{st.session_state.username}_{timestamp}")
            doc_ref.set({
                'ImageUrl': image_url,
                'Username': st.session_state.username,
                'timestamp': firestore.SERVER_TIMESTAMP
            })

            st.success("Image uploaded successfully!")
        except Exception as e:
            st.error(f"Error uploading image: {e}")

    # Analyze image if "Analyze" button is clicked
    if photo and st.button("Analyze"):
        try:
            file_bytes = np.asarray(bytearray(photo.read()), dtype=np.uint8)
            image = cv2.imdecode(file_bytes, 1)
            image_resized = cv2.resize(image, (600, 600))
            gray_image = cv2.cvtColor(image_resized, cv2.COLOR_BGR2GRAY)
            blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

            # Threshold Parameters
            block_size = st.slider("Adaptive Threshold Block Size", 3, 21, 11, 2)
            c_value = st.slider("Adaptive Threshold Constant", -10, 10, 2, 1)
            thresh_image = cv2.adaptiveThreshold(
                blurred_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, block_size, c_value
            )

            # Morphological Parameters
            kernel_size = st.slider("Kernel Size for Morphology", 1, 15, 5, 2)
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))
            morphed_image = cv2.morphologyEx(thresh_image, cv2.MORPH_CLOSE, kernel)

            # Contour Filtering
            contours, _ = cv2.findContours(morphed_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            min_area = st.slider("Minimum Area Threshold", 10, 300, 30, 10)
            filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_area]

            # Count and Draw Contours
            total_grains = len(filtered_contours)
            image_copy = image_resized.copy()
            for cnt in filtered_contours:
                cv2.drawContours(image_copy, [cnt], -1, (0, 255, 0), 2)


            # Display Results
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(image_copy, f"Total Count: {total_grains}", (20, 50), font, 1, (255, 0, 0), 2)
            _, img_encoded = cv2.imencode('.png', image_copy)
            st.image(img_encoded.tobytes(), caption="Processed Image with Total Count", use_column_width=True)

            st.subheader("Thresholded Image")
            _, thresh_encoded = cv2.imencode('.png', thresh_image)
            st.image(thresh_encoded.tobytes(), use_column_width=True)

            st.subheader("Morphed Image")
            _, morphed_encoded = cv2.imencode('.png', morphed_image)
            st.image(morphed_encoded.tobytes(), use_column_width=True)

            st.write(f"## Total number of grains detected: {total_grains}")


            
            
            
        #     # Read image bytes for analysis
        #     file_bytes = np.asarray(bytearray(photo.read()), dtype=np.uint8)
        #     image = cv2.imdecode(file_bytes, 1)

        #     # Resize and preprocess the image
        #     image_resized = cv2.resize(image, (600, 600))
        #     gray_image = cv2.cvtColor(image_resized, cv2.COLOR_BGR2GRAY)
        #     blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

        #     # Threshold Parameters
        #     block_size = st.slider("Adaptive Threshold Block Size", 3, 21, 3, 2)
        #     c_value = st.slider("Adaptive Threshold Constant", -10, 10, 0, 1)
        #     thresh_image = cv2.adaptiveThreshold(
        #         blurred_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, block_size, c_value
        #     )

        #     # Morphological Operations
        #     kernel_size = st.slider("Kernel Size for Morphology", 1, 15, 5, 2)
        #     kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))
        #     morphed_image = cv2.morphologyEx(thresh_image, cv2.MORPH_CLOSE, kernel)

        #     # Contour Filtering
        #     contours, _ = cv2.findContours(morphed_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        #     min_area = st.slider("Minimum Area Threshold", 10, 300, 30, 10)
        #     filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_area]

        #     # Count and draw contours
        #     total_grains = len(filtered_contours)
        #     image_copy = image_resized.copy()
        #     for cnt in filtered_contours:
        #         cv2.drawContours(image_copy, [cnt], -1, (0, 255, 0), 2)

        #     # Display analyzed image and grain count
        #     st.image(image_copy, caption=f"Total Grains Count: {total_grains}", use_column_width=True)
        except Exception as e:
            st.error(f"Error during image analysis: {e}")

    # Display uploaded images
    st.header('Latest Uploaded Images')
    try:
        images_collection_ref = st.session_state.db.collection('Images').order_by('timestamp', direction=firestore.Query.DESCENDING).limit(10).get()
        for doc in images_collection_ref:
            doc_data = doc.to_dict()
            st.image(doc_data['ImageUrl'], caption=f"Uploaded by: {doc_data['Username']}", use_column_width=True)
    except Exception as e:
        st.error(f"Error displaying images: {e}")


if __name__ == "__main__":
    app()





















































