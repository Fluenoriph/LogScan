import requests


class VirusTotalChecker:
    API_URL = 'https://www.virustotal.com/api/v3/'
    IP_ANALYS_ENDPOINT = 'ip_addresses/'
    FILE_DIGEST_ANALYS_ENDPOINT = 'files/'

    def __init__(self, api_key, data_to_check):
        self.headers = { 'x-apikey': api_key }
        self.data_to_check = data_to_check
        self._checks_result = []

        for log_data in self.data_to_check:     # может это другой класс ??
            ip_analys_result = self.get_response(VirusTotalChecker.IP_ANALYS_ENDPOINT, log_data[0])

            full_result = {        # может список ???
                "Client action time": log_data[2].strip('[]'), "Client IP address": log_data[0],

                "IP status malicious count": ip_analys_result["data"]["attributes"]["last_analysis_stats"]["malicious"],
                "IP status suspicious count": ip_analys_result["data"]["attributes"]["last_analysis_stats"]["suspicious"],
                "IP status undetected count": ip_analys_result["data"]["attributes"]["last_analysis_stats"]["undetected"],
                "IP status harmless count": ip_analys_result["data"]["attributes"]["last_analysis_stats"]["harmless"],
                "Client uploaded file digest": log_data[1]
            }

            hash_analys_result = self.get_response(VirusTotalChecker.FILE_DIGEST_ANALYS_ENDPOINT, log_data[1])

            if hash_analys_result is not None:
                full_result["Hash status malicious count"] = hash_analys_result["data"]["attributes"]["last_analysis_stats"]["malicious"]
                full_result["Hash status suspicious count"] = hash_analys_result["data"]["attributes"]["last_analysis_stats"]["suspicious"]
                full_result["Hash status undetected count"] = hash_analys_result["data"]["attributes"]["last_analysis_stats"]["undetected"]
                full_result["Hash status harmless count"] = hash_analys_result["data"]["attributes"]["last_analysis_stats"]["harmless"]
            else:
                full_result["Hash status"] = 'Not exist in VirusTotal base'

            self.checks_result.append(full_result)

    @property
    def checks_result(self):
        return self._checks_result

    @checks_result.setter
    def checks_result(self, value):
        self._checks_result = value

    def get_response(self, endpoint_type, log_data_type):
        response = requests.get(f'{VirusTotalChecker.API_URL}{endpoint_type}{log_data_type}', headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            return None







'''
output = []
output.append(f"URL: {url_to_check}")
output.append(f"Безвредный: {stats['harmless']}")
output.append(f"Вредоносный: {stats['malicious']}")
output.append(f"Подозрительный: {stats['suspicious']}")
output.append(f"Неопределённый: {stats['undetected']}")
output.append("\nАнтивирусы, отметившие как вредоносный:")

print("\nДвижки, пометившие как вредоносное:")
for engine, report in results.items():
    if report["category"] == "malicious":
        output.append(f"- {engine}: {report['result']}")

print("\n".join(output))
with open("result.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(output))'''