# Patrick's Website Bot

## Prerequisites

1. Install Python 3.x on computer
2. Install GoogleChrome

## Setup

1. Clone Repo

``` bash
git clone https://github.com/your-repo/selenium-automation-bot.git
cd selenium-automation-bot
```

2. Install Selenium

Open terminal and navigate to campusChron folder and enter:

``` bash
pip install selenium
```

3. Test the script manually to ensure it works

Open terminal and run:

``` bash
python app.py
```

## Scheduling to Run Daily (macOS)

### Edit crontab

``` bash
crontab -e
```

### Add Cron Job

``` bash
0 9 * * * /usr/local/bin/python3 yourPath/app.py
```

   1. `0 9 * * *` means it runs everyday at 9
   2. make sure python is located in `/usr/local/bin/python3/` or change to correct file_path
   3. edit `yourPath` to be the path to where `app.py` is

### Save it

- Save the crontab file by pressing Ctrl + O and then press Enter to confirm
- exit with Ctrl + x

### Check job

`crontab -l` in terminal to check if successfully running
