import requests

video_url = input("https://xhamster46.desi/videos/lick-my-ass-and-get-a-promotion-the-choice-is-yours-xhMXtel?pw= ")
filename = "video.mp4"

with requests.get(video_url, stream=True) as response:
    response.raise_for_status()
    with open(filename, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)

print("Download complete!")