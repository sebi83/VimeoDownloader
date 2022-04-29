#beautiful soup GUI scraper that downloads videos from vimeo 
#and saves them to a folder

from bs4 import BeautifulSoup
import streamlit as st
import requests
import os
import requests
import sys
import re 

# version 0.1a have to implement save to directory option
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def main():
    try:
        st.title('Sebians VIMEO video downloader 📹')
        video_url_input = st.text_input(label='Copy and paste URL from the browser and press ENTER:')
        #check if url is reachable from internet
        if video_url_input:
            if requests.get(video_url_input, headers=HEADERS).status_code == 200:
                #check if url is a vimeo video
                #download link  
                if 'vimeo' in video_url_input:
                    with st.spinner("Processing..."):
                        video_id = video_url_input.split('/')[-1]
                        direct_link = 'https://player.vimeo.com/video/' + video_id
                        result = requests.get(direct_link, headers=HEADERS)
                        bs = BeautifulSoup(result.text, 'html.parser')
                        bs = str(bs)
                        vod = re.findall(
                            ".*\"url\":\"https://vod-progressive(.*)\.mp4\",.*", bs)
                        vod = vod[0]
                        mp4 = 'https://vod-progressive' + vod + '.mp4'
                        video = requests.get(mp4)
                    
                        file_name = st.text_input(
                            label='To save the file, enter name you want ❗without❗ extension and press ENTER:')
                        #download and save to disk with mp4 extension and file name
                        #ask what directory to save -> todo
                        
                        if file_name:
                            with open(file_name + '.mp4', 'wb') as f:
                                f.write(video.content)
                            
                                       
                            st.success('Video saved to disk')
                            st.write('File saved to: ' + os.getcwd())
                    


                else:
                    st.error('This is not a vimeo video.☠️')
            else:
                st.error('This URL is not reachable from the internet')

    except:
        st.error('Invalid link or something screwed up.💀')
    

if __name__ == "__main__":
    main()







