import requests
import json
import os

class ApiClient:
    def __init__(self, auth_token):
        self.url = "https://metmetric-coms-api-115347578365.africa-south1.run.app"
        self.auth_token = auth_token

    def _post(self, payload, file_path=None):
        headers = {'Authorization': f'{self.auth_token}'}
        if file_path and os.path.isfile(file_path):
            print("file found")
            files = {'files': open(file_path, 'rb')}
            response = requests.post(self.url, headers=headers, data={"data": json.dumps(payload)}, files=files)
            files['files'].close()
        else:
            print("file not found")
            headers['Content-Type'] = 'application/json'
            response = requests.post(self.url, headers=headers, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def send_whatsapp_grid_change_notification(self, recipients, building_id, power_status, file_path=None):
        payload = {
            "message_type": "whatsapp",
            "recipients": recipients,
            "whatsapp": {
                "message_type": "template",
                "template_info": {
                    "template_name": "grid_change_notification",
                    "header_parameters": [power_status],
                    "body_parameters": [building_id, power_status],
                    "number_of_buttons": 0
                }
            }
        }
        return self._post(payload, file_path=file_path)

    def send_email(self, recipients, subject, html_content):
        payload = {
            "message_type": "email",
            "recipients": recipients,
            "email": {
                "subject": subject,
                "html_content": html_content
            }
        }
        return self._post(payload)

    def send_email_with_files(self, recipients, subject, html_content, file_path):
        payload = {
            "message_type": "email",
            "recipients": recipients,
            "email": {
                "subject": subject,
                "html_content": html_content
            }
        }
        return self._post(payload, file_path=file_path)

    def send_sms(self, recipients, text_content):
        payload = {
            "message_type": "sms",
            "recipients": recipients,
            "sms": {
                "text_content": text_content
            }
        }
        return self._post(payload)


