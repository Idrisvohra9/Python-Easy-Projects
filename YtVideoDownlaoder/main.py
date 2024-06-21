import requests
from pytube import YouTube
from tqdm import tqdm

def download_youtube_video(video_url, output_path):
    try:
        # Create a YouTube object with the video URL
        yt = YouTube(video_url)

        # Get the highest resolution stream (usually the first one in the list)
        stream = yt.streams.first()

        # Get the stream URL
        stream_url = stream.url

        # Get the file size of the video
        file_size = int(requests.head(stream_url).headers['Content-Length'])

        # Initialize the progress bar
        progress = tqdm(total=file_size, unit='B', unit_scale=True, desc=yt.title)

        # Open a connection to the stream URL
        with requests.get(stream_url, stream=True) as response:
            # Open the output file in binary write mode
            with open(output_path, 'wb') as file:
                # Iterate over the response content (chunk by chunk)
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        # Write the chunk to the output file
                        file.write(chunk)
                        # Update the progress bar
                        progress.update(len(chunk))

        # Close the progress bar
        progress.close()

        print(f"Downloaded successfully: {yt.title}")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

# Example usage
if __name__ == '__main__':
    video_url = input("Enter the YouTube video URL: ")
    output_path = input("Enter the output file path to save the video (e.g., 'video.mp4'): ")

    download_youtube_video(video_url, output_path)
