# Pythonのベースイメージを指定
FROM python:3.9

# 作業ディレクトリを設定
WORKDIR /app

# Poetryをインストール
RUN curl -sSL https://install.python-poetry.org | python3 -

# Poetryのパスを設定（Docker内でPoetryを使用するために必要）
ENV PATH="${PATH}:/root/.local/bin"
