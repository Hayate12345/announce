import subprocess

# 読み上げたいテキストを指定
text_to_speak = "これからファッションSNS機能の紹介をします。"

# macOSのsayコマンドを呼び出してテキストを読み上げる
subprocess.call(['say', '-r', '0', text_to_speak]) 
