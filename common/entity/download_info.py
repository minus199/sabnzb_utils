import sys
from subliminal import Video

class DownloadInfo:
    __slots__ = ['video', 'script_name', 'directory', 'original_nzb_name', 'job_name', 'report_number', 'category', 'group', 'postprocess_status', 'url']
    def __init__(self):
        super().__init__()
        (self.script_name, self.directory, self.original_nzb_name, self.job_name, self.report_number, self.category, self.group, self.postprocess_status, self.url) = sys.argv
        self.video = Video.fromname('The.Big.Bang.Theory.S05E18.HDTV.x264-LOL.mp4')

    def __str__(self):
        return f'script_name={self.script_name}, directory={self.directory}, original_nzb_name={self.original_nzb_name}, job_name={self.job_name}, report_number={self.report_number}, category={self.category}, group={self.group}, postprocess_status={self.postprocess_status}, url={self.url}'