# Abstract
This script is used to determine how much students with more points than you have sent their consent to enrollment. The result is obtained by parsing info from https://abit.itmo.ru/bachelor/rating/266/.


# Install

```
# pull repository
git clone https://github.com/dreps350/abit2020.git
cd abit2020

# create venv
python -m venv venv

# activate on Windows
& ./venv/Scripts/Activate.ps1

# install dependencies
pip install -r requirements.txt
```

# Run example

```
python .\main.py 288

> [{'name': 'Михайлова Полина Михайловна', 'points': '292'},
>  {'name': 'Шкаровская Валерия Леонидовна', 'points': '289'}]
> Всего подавших согласие с баллом выше 288: 2
```