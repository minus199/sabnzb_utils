import sys
class DownloadInfo:
    __slots__ = ['script_name', 'directory', 'original_nzb_name', 'job_name', 'report_number', 'category', 'group', 'postprocess_status', 'url']
    def __init__(self):
        super().__init__()
        (self.script_name, self.directory, self.original_nzb_name, self.job_name, self.report_number, self.category, self.group, self.postprocess_status, self.url) = sys.argv
