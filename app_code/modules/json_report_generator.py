import json
import os.path
from app_code.modules.base_report_generator import BaseReportGenerator
from app_code.modules.real_time import CurrentTime


class JsonReportGenerator(BaseReportGenerator):
    def __init__(self, result_data, report_path):
        super().__init__(result_data, report_path)

    def generate(self):
        with open(os.path.join(self.report_path, f'report_{CurrentTime.get_time().replace(':', '-')}.json'), "w", encoding="utf-8") as file:
            json.dump(self.result_data, file, indent=4)
