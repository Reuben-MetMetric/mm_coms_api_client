import requests
import json
import os
from .exceptions import AuthenticationError, APIError

class ApiClient:
    """Client for MetMetric Communications API"""
    
    def __init__(self, auth_token):
        """
        Initialize the API client.
        
        Args:
            auth_token (str): Authentication token for the API
        """
        self.url = "https://metmetric-coms-api-115347578365.africa-south1.run.app"
        self.auth_token = auth_token

    def _post(self, payload, file_path=None):
        """
        Internal method to handle POST requests.
        
        Args:
            payload (dict): Request payload
            file_path (str, optional): Path to file attachment
            
        Returns:
            dict: API response
            
        Raises:
            AuthenticationError: If authentication fails
            APIError: If API request fails
        """
        headers = {'Authorization': f'{self.auth_token}'}
        
        try:
            if file_path and os.path.isfile(file_path):
                with open(file_path, 'rb') as file:
                    files = {'files': file}
                    response = requests.post(
                        self.url, 
                        headers=headers, 
                        data={"data": json.dumps(payload)}, 
                        files=files
                    )
            else:
                headers['Content-Type'] = 'application/json'
                response = requests.post(self.url, headers=headers, json=payload)
            
            if response.status_code == 401:
                raise AuthenticationError("Invalid authentication token")
            elif response.status_code == 200:
                return response.json()
            else:
                raise APIError(f"API request failed with status {response.status_code}: {response.text}")
                
        except requests.exceptions.RequestException as e:
            raise APIError(f"Network error: {str(e)}")

    def send_whatsapp_grid_change_notification(self, recipients, building_id, power_status, file_path=None):
        """
        Send WhatsApp grid change notification.
        
        Args:
            recipients (list): List of recipient phone numbers
            building_id (str): Building identifier
            power_status (str): Current power status
            file_path (str, optional): Path to attachment file
            
        Returns:
            dict: API response
        """
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
        """
        Send email without attachments.
        
        Args:
            recipients (list): List of recipient email addresses
            subject (str): Email subject
            html_content (str): HTML email content
            
        Returns:
            dict: API response
        """
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
        """
        Send email with file attachment.
        
        Args:
            recipients (list): List of recipient email addresses
            subject (str): Email subject
            html_content (str): HTML email content
            file_path (str): Path to attachment file
            
        Returns:
            dict: API response
        """
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
        """
        Send SMS message.
        
        Args:
            recipients (list): List of recipient phone numbers
            text_content (str): SMS message content
            
        Returns:
            dict: API response
        """
        payload = {
            "message_type": "sms",
            "recipients": recipients,
            "sms": {
                "text_content": text_content
            }
        }
        return self._post(payload)