import logging

from subliminal import download_best_subtitles, Video
from babelfish import Language
from common.data.postprocessing_status import postprocessing_status
from common.entity.download_info import DownloadInfo

def fetch_subs(metadata):
    logging.info("Fetching subs")
    best_subtitles = download_best_subtitles([metadata.video], {Language('eng')}, providers=['podnapisi'])
    return best_subtitles[metadata.video].content
    
def main():
    metadata = DownloadInfo()
    logging.info(metadata)
    # fetch_subs(metadata)
    