Shaper to google translate
---
### what is this?
WIP

### how to install
1. clone repository
```
git clone https://github.com/masakiaota/translate.git
cd translate/
```

2. start app
if you already installed `flask`, following command will be available.
```
python3 run.py # at `translate/`
```

if you are docker user, following command will be available.
```
docker build -t shaper_to_gt . # make docker image at `translate/`
docker run -p 5000:5000 --rm -it shaper_to_gt # run at any directory
```
`docker run` command is available at any directory. So I recommend you to make docker image.

3. go to browser

Enter address.
```
http://0.0.0.0:5000/
```

### how to use
WIP

### 参考
論文をGoogle翻訳にかける時に便利なWebApp「Shaper」を公開しました
http://dream-exp.hatenablog.com/entry/2017/07/22/shaper



