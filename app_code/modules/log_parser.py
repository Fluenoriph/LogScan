import re


class LogParser:
    TARGET_DATA_KEYS = ('ip', 'file_digest', 'upload_time')

    TARGET_DATA_PATTERNS = (re.compile(r'\d+\.\d+\.\d+\.\d+'), re.compile(r'[0-9A-Fa-f]{64}', re.IGNORECASE),
                            re.compile(r'\[\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\..*]'))

    def __init__(self, log_file):
        self.log_file = log_file
        self._matched_data = []

    @property
    def matched_data(self):
        return self._matched_data

    @matched_data.setter
    def matched_data(self, value):
        self._matched_data = value

    def parse(self):
        with open(self.log_file, 'r') as file:
            logs = file.readlines()

            for line in logs:
                target_data = dict.fromkeys(LogParser.TARGET_DATA_KEYS)

                for i in range(len(LogParser.TARGET_DATA_KEYS)):
                    match = re.search(LogParser.TARGET_DATA_PATTERNS[i], line)

                    if match:
                        target_data[LogParser.TARGET_DATA_KEYS[i]] = match.group()

                self.matched_data.append(target_data)
