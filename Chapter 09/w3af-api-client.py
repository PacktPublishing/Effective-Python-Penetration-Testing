from w3af_api_client import Connection, Scan

connection = Connection('http://127.0.0.1:5000/')
print connection.get_version()

profile = file('w3af/profiles/OWASP_TOP10.pw3af').read()
target = ['http://localhost']

scan = Scan(connection)
scan.start(profile, target)

scan.get_urls()
scan.get_log()
scan.get_findings()
scan.get_fuzzable_requests()
