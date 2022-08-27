from pytube import YouTube


video_url = input("Enter the video url: ")
if video_url in ["cancel", "exit", "quit", "leave"]: quit()
video = YouTube(video_url)

media_type = input("audio or video? (aud/vid): ")
media_type = "video" if "vid" in media_type else "audio"
streams = video.streams.filter(type=media_type)

if not len(streams): 
	print(f"available streams for {media_type}")
	quit()
elif media_type == "video":
	streams = streams.filter(progressive=True, file_extension="mp4").order_by('resolution')
	resolutions = [(idx, stream.resolution) for idx, stream in enumerate(streams)]
	resolution = resolutions[int(input(f"pick some of these resolution by index {resolutions}: "))][1]
	target_stream = streams.filter(res=resolution)[0]
	target_stream.download()
else:
	streams = streams.filter(mime_type="audio/mp4")
	abrs = [(idx, stream.abr) for idx, stream in enumerate(streams)]
	abr = abrs[int(input(f"pick some of these frequence by index {abrs}: "))][1]
	target_stream = streams.filter(abr=abr)[0]
	target_stream.download()
