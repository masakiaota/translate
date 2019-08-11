# https://qiita.com/nanakenashi/items/cbe8e8ef878121638514から参考

# ベースイメージの指定
FROM python:3.5.2-alpine

RUN pip install --upgrade pip &&\
    pip install flask

# （コンテナ内で作業する場合）必要なパッケージをインストール
RUN apk update &&\
    apk add bash fish vim tmux git tree

ADD . /

# ENTRYPOINT ["/usr/bin/fish"]
ENTRYPOINT ["python","run.py"]



