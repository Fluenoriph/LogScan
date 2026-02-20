import requests
import time
import sys



API_KEY = "59663e053a0133586cfbe60c422e81b132fcf5286fe7ac1235a2360f2f074aa8"
url_submit = "https://www.virustotal.com/api/v3/urls"
url_to_check = sys.argv[1]

headers = {
    "x-apikey": API_KEY
}

data = {"url": url_to_check}
response = requests.post(url_submit, data=data, headers=headers)
response_json = response.json()

analysis_id = response_json["data"]["id"]

url_analysis = f"https://www.virustotal.com/api/v3/analyses/{analysis_id}"

while True:
    response = requests.get(url_analysis, headers=headers)
    result = response.json()

    status = result["data"]["attributes"]["status"]
    if status == "completed":
        break

    print("Анализ в процессе... Ожидание")
    time.sleep(2)

stats = result["data"]["attributes"]["stats"]
results = result["data"]["attributes"]["results"]








class VirusTotalChecker:
    API_URL = 'https://www.virustotal.com/api/v3/'

    def __init__(self, api_key, data_to_check):
        self.headers = { 'x-apikey': api_key }
        self.data_to_check = data_to_check
        self._checks_result = None

    @property
    def checks_result(self):
        return self._checks_result

    @checks_result.setter
    def checks_result(self, value):
        self._checks_result = value

    #def



















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