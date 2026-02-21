import abc
import os
from app_code.modules.real_time import CurrentTime


class BaseReportGenerator(abc.ABC):
    REPORT_FILE_TYPE = ('csv', 'json', 'html')

    def __init__(self, result_data, report_path):
        self.result_data = result_data
        self.report_path = report_path

        self.create_report_file = lambda file_type: os.path.join(self.report_path, f'report_{CurrentTime.get_time().replace(':', '-')}.{file_type}')

    @abc.abstractmethod
    def generate(self):
        pass
