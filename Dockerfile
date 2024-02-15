# Pythonのベースイメージを指定
FROM python:3.9

# 作業ディレクトリを設定
WORKDIR /app

# Poetryをインストール
RUN curl -sSL https://install.python-poetry.org | python3 -

# Poetryのパスを設定（Docker内でPoetryを使用するために必要）
ENV PATH="${PATH}:/root/.local/bin"

# # アプリケーションの依存関係ファイルをコピー
# COPY pyproject.toml poetry.lock* /app/

# # 依存関係をインストール
# RUN poetry config virtualenvs.create false \
#     && poetry install --no-interaction --no-ansi

# アプリケーションのコードをコピー
# COPY . /app

# アプリケーションを起動するコマンド（Docker Composeファイルで上書きされます）
# CMD ["poetry", "run", "python", "main.py"]
