import yt_dlp

yt_dlp.utils.bug_reports_message = lambda: ''
yt_dlp.YoutubeDL({
    'format': 'bestvideo[height<=1080]+bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'ffmpeg_location': r'C:\ffmpeg\ffmpeg-7.1-essentials_build\bin'
}).download(['https://youtube.com/shorts/Fp0cXjJKrV0?si=vY1CLqrj4l_4yRIR'])
