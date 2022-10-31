import requests
import tempfile
import base64

resume_url = 'https://storage.googleapis.com/nytro-caliber.appspot.com/test/a62f4caedae94c_1660209901.a62f4caedae6ec.MyCV.pdf?Expires=1667215815&GoogleAccessId=firebase-adminsdk-sl39b%40nytro-caliber.iam.gserviceaccount.com&Signature=kPhgzGLqQhUJrodYfbykUooyRftKMO7TS0g4%2FxKA9Vt3HTpFaNM9qA6Mxok1wc6kEfMQ2%2BQLeVvBLJG%2FE7SCIOaeZIE6%2FLzmbDO8ZvfSkXYlL0BrfiTa59DiHM2dvMWFMzZqrR0R7NCKCo6J8c1ZvaFQWe1OFEOJ7aKKvzXpm4kYHWt4%2FsO%2Fk%2FFdD8wY6N8Zq6rXhe%2FeKTuNJbUsPKvQ8Z2%2Fits728vRg1T7IrlqDC0%2FT66NoPkAYCsvcnM6%2Fq1Te1uro0DHuxn36QrdzNg3D3EniOgGOjHE5%2FF4HluUXS%2BCNo82uLedBxuLnwsgL5D%2BTZ7%2BiOrNr2hlMxL9aoKc2Q%3D%3D'
keyword_url = 'https://storage.googleapis.com/nytro-caliber.appspot.com/test/keywords_template.xlsx?Expires=1667215815&GoogleAccessId=firebase-adminsdk-sl39b%40nytro-caliber.iam.gserviceaccount.com&Signature=BTUVb1TTOI7%2BX%2B5QPIt%2BoNlaspMVsUI1CKn6rL%2Fw9t1LwJ8hDpnTfXyZ0NPkZPdAV%2FPCgU65%2FtRSE2vpNZea%2BV%2BNcITksdOtlixKWCCOmVv4qB2G0M230hRe2sfTlmfr8V0Sfh367t1RV6T0CHw%2Fdkw4giTLqLePrTORigJfFrMxEYgMnpAFn9GAtL%2BBcHphrOlwfhKeR8lPK%2BN8z4mAuyL8IgKYo%2BaMpfy1yuI4SUL%2BjDRBtO4oFJDnAI%2Fp%2B2TgzNxkSVfITa82FXAzqLfsX7vUW9O6Ak%2FmK%2FCa6VSsFqgW5E4W4FPVnTHmJi3Q33tt5POXnAARU0ye6yjFtuQ4rw%3D%3D'

resp = requests.get(resume_url)
with tempfile.TemporaryFile() as file:
    file.write(resp.content)
    file.seek(0)
    base64str = base64.b64encode(file.read()).decode('UTF-8')
    import pdb; pdb.set_trace()