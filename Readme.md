## DES Labs frontpage

Just a simple frontpage for now, static ip links will be replaced

## Footprint display

To run local server:

    # Python 2.X
    python -m SimpleHTTPServer

    # Python 3.X
    python -m http.server

Using Node.js

    npm install http-server -g

then

    http-server .

## Docker

To run from docker

    docker build -t frontpage .


    docker run -d -p 80:80 frontpage
