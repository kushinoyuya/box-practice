from boxsdk import JWTAuth
from boxsdk import Client

"""
処理ロジック
・BOXAPIを認証する設定ファイルを指定する
・環境変数でgitにアップロードしない設定
・対象のBOXID(folder-id)を指定する
・BOXID(folder-id)の配下のディレクトリを取得する
・[result_yyyymmddss.txt]に出力させる
"""




auth = JWTAuth.from_settings_file('./API-TEST1_config.json')
client = Client(auth)

def log_file(parameter_list):
    pass

def box_file_list(parameter_list):
    pass

if __name__ == "__main__":
    pass
