'''
This Program is to Download Video From YouTube
'''
# Importing the module
import pytube
# Link of desired Video
Video_Link = input('Paste url of Video: ')

Download_Video = pytube.YouTube(Video_Link)
Download_Video.streams.first().download()
print("Your Video is Downloaded Successfully: ", Video_Link)
exit()
