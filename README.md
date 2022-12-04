# PYTHON parser for leader-id.ru
This parser is written in Python 3.10.0, following libraries you can find in `requirements.txt`   
Parsed data is stored in `users.json` and `users.csv` files
## installation and usage
```
git clone https://github.com/V4kodin/Leader_parsing
```
```
cd Leader_parsing
```
```
python -m venv env
```
```
env/Scripts/Activate.ps1
```
```
pip install -r requirements.txt
```
* Create account on https://leader-id.ru/ 
* edit `headers.txt` file with your headers from https://leader-id.ru/users
![headers](/1.png)
* edit `user_headers.txt` file with your headers from https://leader-id.ru/users/<any_user_id> which you can select from https://leader-id.ru/users
![user_headers](/2.png)
### !!! PAST INTO `headers.txt` and `user_headers.txt` WITHOUT 1st ROW !!!

```
python main.py
```
if you want pars with another filters, change `url_json` in `main.py` with url from headers from `headres.txt` (click rmb on request, copy url)
