# Telegram Account Converter

This project automates the process of converting Telegram `tdata` files into Telethon-compatible session files and JSON metadata. It handles various Telegram client configurations and ensures compatibility across multiple sessions. The script also includes error handling for common Telegram-related issues, such as bans and deactivated accounts.

---

## Features

- **TData Conversion**: Converts Telegram `tdata` files to Telethon-compatible session files.
- **Metadata Generation**: Creates detailed JSON files containing user information, such as phone number, username, and account status.
- **Error Handling**: Handles cases of banned or deactivated accounts gracefully.
- **Supports Multiple Accounts**: Batch processes multiple `tdata` files from a directory.
- **Customizable Fields**: Includes detailed account metadata, such as language, app version, and registration time.

---

## Requirements

- Python 3.7 or higher
- Dependencies:
  - `telethon`
  - `opentele`
  - `requests`
  - Other standard Python libraries (`os`, `glob`, `asyncio`, etc.)

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/atljh/SessionTDataConverter.git
   cd https://github.com/atljh/SessionTDataConverter.git

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3. **Prepare your data**:

    Place your tdata files in the tdatas/ directory.

## Usage
1. **Run the script**:
    ```python
    python main.py
    ```
2. **Follow the prompts, if any, and monitor the output in the terminal.**
    ```plaintext
    Аккаунт tdata123 успешно сконвертирован в 1234567890
    Аккаунт забанен
    Не удалось открыть аккаунт tdata456
    ```
3.  **Converted session files will be saved in the sessions/ directory as .session and .json files.**



## License

This project is open-source and distributed under the MIT License. See LICENSE for more details.