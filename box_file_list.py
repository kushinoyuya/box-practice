from boxsdk import JWTAuth
from boxsdk import Client

"""
処理ロジック
①BOXAPIを認証する設定ファイルを指定する
②対象のBOXID(folder-id)を指定する
③BOXID(folder-id)の配下のディレクトリを取得する
④[result_yyyymmddss.txt]に出力させる
"""
config_file =

auth = JWTAuth.from_settings_file('./API-TEST1_config.json')
client = Client(auth)

def log_file(parameter_list):
    pass

def box_file_list(parameter_list):
    pass

if __name__ == "__main__":
    pass
