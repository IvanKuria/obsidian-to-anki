# Security Policy

## Supported Versions

Use this section to tell people about which versions of your project are currently being supported with security updates.

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability within this project, please send an email to [your-email@example.com]. All security vulnerabilities will be promptly addressed.

Please include the following information in your report:

- A description of the vulnerability
- Steps to reproduce the issue
- Potential impact
- Suggested fix (if any)

## Security Considerations

This project uses OpenAI's API for generating flashcards. Please note:

1. **API Key Security**: Never commit your OpenAI API key to version control
2. **Data Privacy**: Your markdown content is sent to OpenAI for processing
3. **Rate Limiting**: Be aware of OpenAI's rate limits and usage costs

## Best Practices

- Store your API key in a `.env` file (not committed to git)
- Review generated flashcards before importing to Anki
- Be mindful of sensitive information in your notes 