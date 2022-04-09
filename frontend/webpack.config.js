const { VueLoaderPlugin } = require('vue-loader');　　　　
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  entry:'./src/index.ts',
  mode: 'development',
  output: {
    // path: `${__dirname}/dist`,
    publicPath: 'http://127.0.0.1:5500/event_project/frontend/dist/',
    filename: 'main.js',
  },
  resolve:{　　　　　　　　　　　　　　　　　　
    extensions: [".vue", ".js",".ts"],
  },
  module:{
    rules:[
      {　　　　　　　　　　　　　　　　　　　　
        test: /\.vue$/,
        loader: 'vue-loader'
      },
      {　　　　　　　　　　　　　//追加
        test: /\.ts$/,
        exclude: /node_modules/,
        loader: 'ts-loader',
        options: {
          appendTsSuffixTo: [/\.vue$/],
        },
      },
    ]
  },
  plugins: [
    new VueLoaderPlugin(),
    new BundleTracker({filename: './webpack-stats.json'})　　　　　　　　　　　　　　　　　　　
  ],
}