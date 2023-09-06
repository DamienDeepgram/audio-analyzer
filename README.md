# audio-quality-analyzer

Forked from: [spectrum-analyzer](https://github.com/edwardball/academo.org/tree/master/demos/spectrum-analyzer)

![Screenshot](https://github.com/DamienDeepgram/audio-quality-analyzer/raw/main/images/screenshot.png)

## Running

Install http-server [https://www.npmjs.com/package/http-server](https://www.npmjs.com/package/http-server)

```
npm i http-server -g
```

Serve the page from the root of the repo

```
http-server
```

Access the page in the browser

[https://localhost:8080](https://localhost:8080)

## Backend

There is a backend running you can use but if you want to run your own you need to update the url [here](https://github.com/DamienDeepgram/audio-quality-analyzer/blob/main/js/demo.js#L2) to localhost

Install Deps

```
pip install Flask
pip install flask_cors
pip install mutagen
pip install SoundFile
```

Running the python API

```
python3 main.py
```