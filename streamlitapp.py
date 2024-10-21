import streamlit as st
import os
import json
from cbc_diagnose import diagnose  

def main():
    st.title("CBC Report Diagnosis")

    # Upload image
    uploaded_file = st.file_uploader("Upload a CBC report image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Save the uploaded file
        image_path = os.path.join("uploads", uploaded_file.name)
        
        # Ensure uploads directory exists
        if not os.path.exists("uploads"):
            os.makedirs("uploads")
        
        with open(image_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        st.success("Image uploaded successfully!")

        # Call the diagnosis function
        result = diagnose(image_path)

        # Display the output
        if result:
            st.subheader("Diagnosis Result:")
            st.markdown("<h3 style='text-align: center;'>Detected:</h3>", unsafe_allow_html=True)
            st.markdown(f"<h1 style='text-align: center;'> <strong>{result['Diagnosis']}</strong></h1>", unsafe_allow_html=True)  


            # Display other parameters
            st.write("Extracted data:")
            for key, value in result.items():
                if key != "Diagnosis":
                    st.write(f"{key}: {value}")

if __name__ == "__main__":
    main()
