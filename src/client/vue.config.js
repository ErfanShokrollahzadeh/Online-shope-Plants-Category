const { defineConfig } = require('@vue/cli-service')
const path = require('path')

module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true
      }
    },
    allowedHosts: 'all'
  },
  configureWebpack: {
    output: {
      clean: true
    },
    optimization: {
      splitChunks: {
        chunks: 'all'
      }
    },
    resolve: {
      alias: {
        '@': path.resolve(__dirname, 'src')
      }
    }
  }
})
