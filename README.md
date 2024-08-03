# TarotAI

made by brAIns

## How to use:

1. Clone the repository.

```shell
git clone https://github.com/taehyunKIMGH/TarotAI
```

2. install all the requirements.

   1. using makefile

   ```shell
   make install
   ```

   2. using install.sh

   ```shell
   chmod +x install.sh
   ./install.sh
   ```
3. Write `secret.py` with following contents:
```python
sender_email = <YOUR_EMAIL_ADDRESS>
password = <YOUR_EMAIL_PASSWORD>
```

4. Fill in `my_api_key` with your own OpenAI api key.

5. Specify your kakaotalk rest_id, redirect_url, code in `set_kakao_token.py`

6. Run `set_kakao_token.py` via Shell.

```shell
python3 set_kakao_token.py
```

7. Specify your Google OAuth credentials path in `google_drive_api.py`

8. Run `main.py` via Shell.

```shell
python3 main.py
```
