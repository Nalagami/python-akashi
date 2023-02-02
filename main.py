import requests
import datetime

cooperation = "/"
URL = "https://atnd.ak4.jp/api" + cooperation
TOKEN = ""

# 従業員情報取得
def get_employee_information(token, url):
    EMPLOYEE_ID=""
    EMPLOYEE_INFORMATION_URL = url + "/staffs"
    
    payload = {"token":token, "target":token}

    result = requests.get(EMPLOYEE_INFORMATION_URL, params=payload)

    if result.status_code != requests.codes.ok:
        print("ステータスコード200以外が帰ってきました")
        return 1

    print(result)
    
    return result

# 打刻関数
def engraving(token, url, type="11", stampedAt=datetime.datetime.now().strftime('%y/%m/%d %H:%M:%S'), timezone="+09:00"):
    """
    AKASHIで打刻する関数

    Parameters
    ----------
    token : String
        AKASHI APIトークン
    url : String
        AKASHI APIエンドポイント
    type : String
        打刻種別
    stampedAt : datetime
        打刻時間(yyyy/mm/dd HH:MM:SS 形式)
    timezone : String
        タイムゾーン

    Return
    ----------
    result : Response
    """
    ENGRAVING_URL = url + "/stamps"

    payload = {"token":token, "type": type, "stampedAt": stampedAt, "timezone": timezone}

    result = requests.post(ENGRAVING_URL, params=payload)

    if result.status_code != requests.codes.ok:
        print("ステータスコード200以外が帰ってきました")
        return 1

    return result