from app_code.modules.log_parser import LogParser
from app_code.modules.virus_total import VirusTotalChecker
from app_code.modules.csv_report_generator import CsvReportGenerator
from app_code.modules.json_report_generator import JsonReportGenerator
from app_code.modules.program_logger import ProgramLogger


class ProgramProcess:
    def __init__(self, source_log_file, api_key, result_log_path, result_log_format):
        logger = ProgramLogger()
        logger.logger.info('Program started')

        source_log_parser = LogParser(source_log_file)
        source_log_parser.parse()

        virus_analyzer = VirusTotalChecker(api_key, source_log_parser.matched_data, logger.logger)
        self._result = virus_analyzer.checks_result

        if result_log_format == 'csv':
            csv_report = CsvReportGenerator(self.result, result_log_path)
            csv_report.generate()
            logger.logger.info('CSV report generated')

        elif result_log_format == 'json':
            json_report = JsonReportGenerator(self.result, result_log_path)
            json_report.generate()

            logger.logger.info('JSON report generated')

    @property
    def result(self):
        return self._result
