const path = require('path');
var webpack = require("webpack");
var ExtractTextPlugin = require("extract-text-webpack-plugin");

module.exports = {
  entry: './masaProduction/js/main.jsx',
  output: {
    path: path.join(__dirname, '/masaProduction/static/js/'),
    filename: 'bundle.js',
  },
  module: {
    rules: [
      {
        // Test for js or jsx files
        test: /\.jsx?$/,
        loader: 'babel-loader',
        query: {
          // Convert ES6 syntax to ES5 for browser compatibility
          presets: ['es2015', 'react'] }
      },
      { test: /\.css$/, loader: "style-loader!css-loader" },
      { test: /\.png$/, loader: "url-loader?limit=100000" },
      { test: /\.jpg$/, loader: "file-loader" }
    ],
  },
  resolve: {
    extensions: ['.js', '.jsx', '.css'],
  },
  plugins: [
    new ExtractTextPlugin("style.css", { allChunks: true })
  ]
};