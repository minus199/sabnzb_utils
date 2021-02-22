
import logging

from subliminal import download_best_subtitles, Video, region
from babelfish import Language
from common.data.postprocessing_status import postprocessing_status
from common.entity.download_info import DownloadInfo
    
def fetch_subs(metadata):
    video = Video.fromname('The.Big.Bang.Theory.S05E18.HDTV.x264-LOL.mp4')
    best_subtitles = download_best_subtitles([video], {Language('eng')}, providers=['podnapisi'])
    return best_subtitles[video].content
    
def main():
    metadata = DownloadInfo()
    fetch_subs(metadata)
    sys.exit(0)
    

if __name__ == "__main__":
    import sys
    logging.basicConfig(filename='/app/scripts.log', level=logging.DEBUG)
    region.configure('dogpile.cache.memory')
    
    try:    
        main()    
    except Exception as e:
        print("No commandline parameters found")
        print(e)
        sys.exit(1)

