!pip install pydub
import glob
import os
from google.colab import drive
from pydub import AudioSegment

# Google Driveをマウント
drive.mount('/content/drive')

# pydubをインポート
from pydub.silence import split_on_silence

# 入力ディレクトリと出力ディレクトリを指定
input_dir = '/content/drive/MyDrive/touhoku_mukashibanashi'
output_dir = '/content/drive/MyDrive/touhoku_mukashibanashi/touhoku_mukashibanashi_5sec'

# 出力ディレクトリが存在しない場合は作成
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 入力ディレクトリ内の音声ファイルを取得
input_files = glob.glob(os.path.join(input_dir, '*.wav'))

# 5秒ごとに音声を区切って保存
for input_file in input_files:
    # 音声ファイルを読み込み
    audio = AudioSegment.from_wav(input_file)

    # 5秒ごとに区切る
    segment_duration = 5 * 1000  # 5秒をミリ秒に変換
    for i, start in enumerate(range(0, len(audio), segment_duration)):
        # 5秒ごとの部分音声を切り出し
        segment = audio[start:start + segment_duration]

        # 出力ファイル名を作成
        output_file = os.path.join(output_dir, f'{os.path.basename(input_file)}_{i + 1}.wav')

        # 出力ファイルが既に存在する場合、適切なファイル名を生成
        if os.path.exists(output_file):
            base, ext = os.path.splitext(output_file)
            output_file = f'{base}_{i + 1}{ext}'

        # 部分音声を保存
        segment.export(output_file, format="wav")

print("処理が完了しました。")
