import abc


class BaseReportGenerator(abc.ABC):
    def __init__(self, result_data, report_path):
        self.result_data = result_data
        self.report_path = report_path
        # abstract report file ???

    @abc.abstractmethod
    def generate(self):
        pass
