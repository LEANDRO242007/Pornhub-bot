import yt_dlp
import asyncio

async def ydl(url: str):
    loop = asyncio.get_running_loop()
    dl = yt_dlp.YoutubeDL({"logger": YT_DLP_LOGGER()})
    fdata = await loop.run_in_executor(None, dl.extract_info, url)
    fname = dl.prepare_filename(fdata)

    return fname


class YT_DLP_LOGGER(object):
    def debug(self, msg):
            pass
    def error(self, msg):
            pass
    def warning(self, msg):
            pass
