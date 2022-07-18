# store-webui

## Project setup
```
yarn install
```

### Compiles and hot-reloads for development
```
yarn serve
```

### Compiles and minifies for production
```
yarn build
```

### Lints and fixes files
```
yarn lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

## Dockfile

```bash
docker build -t hub.deepin.com/wuhan_v23_linglong/linglong-web-store:develop-snipe .
```

```bash
docker run --rm -it  -p 80:80/tcp hub.deepin.com/wuhan_v23_linglong/linglong-web-store:develop-snipe
```
