import datetime
import json
import requests

# Insert your API key from Google Cloud Platform
API_KEY = "INSERT YOUR API KEY HERE"

# Look up Channel IDS for your favorite channels and insert them into the list below.
# If you aren't sure how to find channel IDs, use ChatGPT, Bard or Bing AI.
channels = [
    {"id": 'UChPuCAEXg7iYkVNjQY1NGYg', "name": "FULL SEND PODCAST"},
    {"id": 'UC_m9eOGw7aL15t3t5Fz59-g', "name": "Impaulsive"},
    {"id": 'UC_w44x41r159p2z-6f2V4_A', "name": "Flagrant"},
    {"id": 'UC39zNWlUcLs9wgRQYMR2lcw', "name": "MrBeast"},
    {"id": 'UC-lHJZR3Gqxm24_Vd_AJ5Yw', "name": "PewDiePie"},
    {"id": 'UC18jBB8wAgH_m2p6437O4XA', "name": "Sidemen"}
]

try:
    hours_old = int(input("Enter the maximum age (in hours) of videos you want to check: "))
except ValueError:
    print("Invalid input. Please enter a valid number of hours.")
    exit()

published_after = (datetime.datetime.now() - datetime.timedelta(hours=hours_old)).isoformat() + "Z"

video_duration = "any"

new_videos = []

for channel in channels:
    channel_id = channel["id"]
    channel_name = channel["name"]

    try:
        response = requests.get(
            f"https://www.googleapis.com/youtube/v3/search?key={API_KEY}&channelId={channel_id}&publishedAfter={published_after}&videoDuration={video_duration}&part=snippet&type=video"
        )

        if response.status_code == 200:
            response_data = response.json()

            if "items" in response_data:
                items = response_data["items"]

                for video in items:
                    snippet = video["snippet"]
                    video_title = snippet["title"]
                    video_id = video["id"]["videoId"]

                    video_response = requests.get(
                        f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={API_KEY}"
                    )

                    if video_response.status_code == 200:
                        video_data = video_response.json()

                        new_videos.append({
                            "title": video_data["items"][0]["snippet"]["title"],
                            "link": f"https://youtube.com/watch?v={video_id}",
                            "channel": channel_name
                        })
                    else:
                        print(f"Error fetching video details for video ID {video_id}: {video_response.content}")
            else:
                print(f"No new videos found for channel: {channel_name}")
        else:
            print(f"Error fetching search results for channel ID {channel_id}: {response.content}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if new_videos:
    print("New videos uploaded:")
    for new_video in new_videos:
        print(f"{new_video['title']} - {new_video['channel']} - {new_video['link']}")
else:
    print("No new videos found.")
