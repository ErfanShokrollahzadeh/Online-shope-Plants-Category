const { defineConfig } = require("@vue/cli-service");
const path = require("path");

module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: {
      "/api": {
        target: "http://localhost:8000",
        changeOrigin: true,
      },
    },
    allowedHosts: "all",
  },
  configureWebpack: {
    output: {
      clean: true,
    },
    optimization: {
      splitChunks: {
        chunks: "all",
      },
    },
    resolve: {
      alias: {
        "@": path.resolve(__dirname, "src"),
      },
    },
  },
  chainWebpack: (config) => {
    config.module
      .rule("js")
      .use("babel-loader")
      .tap((options) => {
        // Disable cache to prevent permission issues
        options.cacheDirectory = false;
        return options;
      });
  },
});
