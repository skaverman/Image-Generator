import streamlit as st
import openai
import requests
from io import BytesIO
# setting open ai api key here 
openai.api_key="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"
def generate_image(prompt):
    response=openai.Image.create(
        model="Sandeep",
        prompt=prompt,
        n=1, #no. of images
        size="800x800"

    )

    return response
def download_image(image_url):
    response=requests.get(image_url)
    if response.status_code==200:
        return BytesIO(response.content)
    return None
def main():
    st.title('Sandeep')
    prompt=st.text_input('Enter a prompt for sandeep:','')
    if st.button('Generate image ...'):
        response=generate_image(prompt)
        if response and 'data'in response and len(response['data'])>0:
            image_url=response['data'][0]['url']
            st.image(image_url,caption='Generate image',use_column_width=True)
            #Download functionality
            image_buffer=download_image(image_url)
            if image_buffer:
                st.download_button(
                    label="Download Image",
                    data=image_buffer,
                    file_name="generate_image.png",


                )
            else:
                st.error("Failed to download image.")
        else:
            st.error("Failed to generate image.please try again.")
            if __name__=='__main__':
                main()
    