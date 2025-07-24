# MetMetric Communications API Client

A Python client library for the MetMetric Communications API that enables sending emails, SMS messages, and WhatsApp notifications through a unified interface.

## Features

- 📧 Send emails with or without attachments
- 📱 Send SMS messages
- 💬 Send WhatsApp template notifications
- 🔒 Secure authentication with API tokens
- 🛡️ Built-in error handling and custom exceptions
- 📝 Comprehensive logging and documentation

## Installation

### Install from GitHub

```bash
pip install git+https://github.com/Reuben-MetMetric/mm_coms_api_client.git
```

### Development Installation

```bash
git clone https://github.com/Reuben-MetMetric/mm_coms_api_client.git
cd mm_coms_api_client
pip install -e .
```

## Quick Start

```python
from mmComsClient import ApiClient

# Initialize the client with your API token
client = ApiClient("your-api-token-here")

# Send a simple email
client.send_email(
    recipients=["user@example.com"],
    subject="Hello from MetMetric",
    html_content="<h1>Welcome!</h1><p>This is a test email.</p>"
)
```

## Authentication

You need an API token to use this library. Contact your MetMetric administrator to obtain your authentication token.

```python
from mmComsClient import ApiClient

client = ApiClient("your-api-token")
```

## API Reference

### Email Functions

#### `send_email(recipients, subject, html_content)`

Send an email without attachments.

**Parameters:**
- `recipients` (list): List of recipient email addresses
- `subject` (str): Email subject line
- `html_content` (str): HTML content of the email

**Example:**
```python
response = client.send_email(
    recipients=["john@example.com", "jane@example.com"],
    subject="Monthly Report",
    html_content="""
    <html>
        <body>
            <h2>Monthly Report</h2>
            <p>Please find the monthly report attached.</p>
            <p>Best regards,<br>MetMetric Team</p>
        </body>
    </html>
    """
)
```

#### `send_email_with_files(recipients, subject, html_content, file_path)`

Send an email with a file attachment.

**Parameters:**
- `recipients` (list): List of recipient email addresses
- `subject` (str): Email subject line
- `html_content` (str): HTML content of the email
- `file_path` (str): Path to the file to attach

**Example:**
```python
response = client.send_email_with_files(
    recipients=["manager@example.com"],
    subject="Report with Attachment",
    html_content="<p>Please find the report attached.</p>",
    file_path="/path/to/report.pdf"
)
```

### SMS Functions

#### `send_sms(recipients, text_content)`

Send SMS messages to one or more recipients.

**Parameters:**
- `recipients` (list): List of recipient phone numbers (with country codes)
- `text_content` (str): SMS message content

**Example:**
```python
response = client.send_sms(
    recipients=["27123456789", "27987654321"],
    text_content="Alert: Power outage detected in Building A. Estimated restoration: 2 hours."
)
```

### WhatsApp Functions

#### `send_whatsapp_grid_change_notification(recipients, building_id, power_status, file_path=None)`

Send WhatsApp grid change notifications using a predefined template.

**Parameters:**
- `recipients` (list): List of recipient WhatsApp numbers (with country codes)
- `building_id` (str): Identifier for the building
- `power_status` (str): Current power status (e.g., "online", "offline")
- `file_path` (str, optional): Path to attachment file

**Example:**
```python
response = client.send_whatsapp_grid_change_notification(
    recipients=["+27123456789"],
    building_id="BLDG-001",
    power_status="offline"
)

# With attachment
response = client.send_whatsapp_grid_change_notification(
    recipients=["+27123456789"],
    building_id="BLDG-001",
    power_status="online",
    file_path="/path/to/status_report.pdf"
)
```

## Error Handling

The library provides custom exceptions for better error handling:

```python
from mmComsClient import ApiClient
from mmComsClient.exceptions import AuthenticationError, APIError, MetMetricError

client = ApiClient("your-token")

try:
    response = client.send_email(
        recipients=["test@example.com"],
        subject="Test",
        html_content="<p>Test email</p>"
    )
    print("Email sent successfully:", response)
    
except AuthenticationError:
    print("Authentication failed. Please check your API token.")
    
except APIError as e:
    print(f"API request failed: {e}")
    
except MetMetricError as e:
    print(f"MetMetric service error: {e}")
```

### Exception Types

- `MetMetricError`: Base exception for all MetMetric-related errors
- `AuthenticationError`: Raised when API authentication fails
- `APIError`: Raised when API requests fail (network issues, server errors, etc.)

## Response Format

All methods return a JSON response from the API. A successful response typically looks like:

```json
{
    "status": "success",
    "message": "Message sent successfully",
    "message_id": "msg_12345",
    "timestamp": "2024-01-15T10:30:00Z"
}
```

## Complete Example

```python
from mmComsClient import ApiClient
from mmComsClient.exceptions import AuthenticationError, APIError

def main():
    # Initialize client
    client = ApiClient("your-api-token-here")
    
    try:
        # Send email notification
        email_response = client.send_email(
            recipients=["admin@company.com"],
            subject="System Alert",
            html_content="<h2>System Status Update</h2><p>All systems operational.</p>"
        )
        print("Email sent:", email_response.get('message_id'))
        
        # Send SMS alert
        sms_response = client.send_sms(
            recipients=["27123456789"],
            text_content="System alert: All systems are now operational."
        )
        print("SMS sent:", sms_response.get('message_id'))
        
        # Send WhatsApp notification
        whatsapp_response = client.send_whatsapp_grid_change_notification(
            recipients=["27123456789"],
            building_id="HQ-BLDG",
            power_status="online"
        )
        print("WhatsApp sent:", whatsapp_response.get('message_id'))
        
    except AuthenticationError:
        print("Error: Invalid API token")
    except APIError as e:
        print(f"Error: API request failed - {e}")

if __name__ == "__main__":
    main()
```

## Phone Number Format

For SMS and WhatsApp functions, use international format with country codes:

- ✅ Correct: `"27123456789"` (South Africa)
- ✅ Correct: `"1234567890"` (US)

## File Attachments

When using file attachments:

- Ensure the file path exists and is accessible
- The file will be automatically closed after sending
- Supported file types depend on your MetMetric API configuration
- File size limits apply (check with your administrator)

## Requirements

- Python 3.7+
- requests >= 2.25.0

## Support

For support and questions:

- Email: reuben@metmetric.co.za
- GitHub Issues: [https://github.com/Reuben-MetMetric/mm_coms_api_client/issues](https://github.com/Reuben-MetMetric/mm_coms_api_client/issues)