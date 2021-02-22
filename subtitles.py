from subtitles.main import main
import sys
import logging

from subliminal import region

from common.data.postprocessing_status import postprocessing_status
from common.entity.download_info import DownloadInfo

logging.basicConfig(filename='/app/scripts.log', level=logging.DEBUG)

region.configure('dogpile.cache.memory')

try:    
    logging.info("starting subtitles fetcher")
    main()
    sys.exit(0)
except Exception as e:
    logging.error(("No commandline parameters found", e))
    sys.exit(1)