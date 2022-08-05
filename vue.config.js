module.exports = {
  chainWebpack: config => {
    config.plugin('html').tap(args => {
      args[0].title = 'Linglong Web Store';
      return args;
    });
  },
  configureWebpack: {
    devtool: 'source-map'
  }
};
