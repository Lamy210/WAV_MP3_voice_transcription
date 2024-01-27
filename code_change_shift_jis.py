import os
import glob

def main():
    # 対象ファイルの一覧を取得
    filenames = glob.glob('*.mp3')

    # ファイル名をUTF-8でエンコード
    for filename in filenames:
        encoded_filename = filename.encode('utf-8')

    # ファイル名を変更
    for filename in filenames:
        os.rename(filename, encoded_filename.decode())

if __name__ == "__main__":
    main()

