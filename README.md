# YouTube Channel Video Fetcher

## Purpose
The YouTube Channel Video Fetcher script allows you to specify YouTube channels of your choice. It then checks for the latest videos from these channels, taking into account your specified time frame in hours to determine how old the videos can be.

## Example
1. Enter the maximum age (in hours) of videos you want to check:  
120 (example input)

2. Output:    
Candace Owens Exposes Barack Obama and Goes Off on Logan Paul! - FULL SEND PODCAST - https://youtube.com/watch?v=rERky4xzbLM  
dad life - PewDiePie - https://youtube.com/watch?v=_sPXXL9YXok  

# Quick Start

## Prerequisites
- Obtain a YouTube Data API key:
1. Go to the [Google Developers Console](https://console.developers.google.com/).
2. Create a new project if you don't have one.
3. Enable the "YouTube Data API v3" for your project.
4. Create an API key and make sure to restrict its usage as needed (usually by specifying the application or website that will use it).

## Configuration
1. Open the script file in a text editor or integrated development environment (IDE) of your choice.
2. Replace `"YOUR_YOUTUBE_API_KEY"` in the script with the API key you obtained in step 2.
3. Customize the `channels` list in the script to include the YouTube channel IDs and names you want to track.
4. Save your changes to the script.

# How To Run

1. Run the script by entering the following command:
python youtube_channel_video_checker.py

2. The script will prompt you to enter the maximum age (in hours) of videos you want to check. Enter a valid number of hours and press Enter.

3. The script will then connect to the YouTube Data API, check the specified channels for new videos within the specified time frame, and display the results, including video titles, channel names, and links.

4. Review the list of new videos uploaded to the specified channels.
