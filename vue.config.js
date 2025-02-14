module.exports = {
  chainWebpack: (config) => {
    config.module
      .rule("js")
      .use("babel-loader")
      .tap((options) => {
        // Disable cache to bypass permission issues
        options.cacheDirectory = false;
        return options;
      });
  },
};
