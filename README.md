# Cross-Browser Testing Project

This project implements automated cross-browser testing using Selenium WebDriver to test web applications across different browsers including Chrome, Firefox, Edge, and Yandex Browser.

## Features

- Cross-browser testing support for:
  - Google Chrome
  - Mozilla Firefox
  - Microsoft Edge
  - Yandex Browser
- Automated test execution using Selenium WebDriver
- GitHub Actions integration for CI/CD
- Allure reporting for test results

## Prerequisites

- Python 3.9 or higher
- Web browsers installed on your system
- WebDriver executables for each browser

## Installation

1. Clone the repository:

```bash
git clone <your-repository-url>
cd <repository-name>
```

2. Install Python dependencies:

```bash
pip install -r requirements.txt
```

3. Install WebDrivers:
   - ChromeDriver
   - GeckoDriver (Firefox)
   - EdgeDriver
   - YandexDriver

## Project Structure

```
.
├── crossbrowsertests.py    # Main test file
├── requirements.txt       # Python dependencies
└── .github/
    └── workflows/        # GitHub Actions workflows
        └── cross-browser-tests.yml
```

## Running Tests

### Local Execution

To run tests locally, use the following command:

```bash
python crossbrowsertests.py
```

You can specify the browser using the BROWSER environment variable:

```bash
BROWSER=chrome python crossbrowsertests.py
BROWSER=firefox python crossbrowsertests.py
BROWSER=edge python crossbrowsertests.py
BROWSER=yandex python crossbrowsertests.py
```

### GitHub Actions

Tests are automatically triggered on:

- Push to main branch
- Pull requests to main branch

The workflow will:

1. Set up the Python environment
2. Install all required browsers and drivers
3. Run tests across all supported browsers
4. Generate and upload Allure reports

## Test Reports

After test execution, Allure reports are generated and can be found in the `allure-report` directory. The reports include:

- Test execution results
- Test duration
- Screenshots (if configured)
- Test steps and logs

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
