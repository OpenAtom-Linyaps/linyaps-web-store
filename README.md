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

```bash
kubectl create deployment linglong-web-store --image=hub.deepin.com/wuhan_v23_linglong/linglong-web-store:develop-snipe
```

- 使用 18081 端口提供服务，连接到容器的 80 端口

```bash
kubectl expose deployment linglong-web-store --type=NodePort --port=18081 --target-port=80
```
