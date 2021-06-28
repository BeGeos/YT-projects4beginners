from pytube import YouTube
import os


def progress(stream, chunk, bytes_remaining):
    size = stream.filesize
    downloaded = ((size - bytes_remaining) / size) * 100
    print(f"{round(downloaded)} of 100")
    return


def complete(chunk, filepath):
    print("Done!")
    return


def download_video(url, filename=None):
    folder = os.path.join("/Users/lakota/Desktop", "YT-downloads")
    if not os.path.exists(folder):
        os.mkdir(folder)
    path = folder

    if filename is not None:
        file = os.path.join(path, filename + ".mp4")
        if os.path.exists(file):
            print(f"{filename} already exists!")
            return

    video = YouTube(url, on_progress_callback=progress, on_complete_callback=complete)
    video.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first().download(path,
                                                                                                                filename)

    return
