const path = require('path');

const UglifyJSPlugin = require('uglifyjs-webpack-plugin')

const config = {
  plugins: [ new UglifyJSPlugin() ] 
}

module.exports = {
  entry: './masaProduction/js/main.jsx',
  output: {
    path: path.join(__dirname, '/masaProduction/static/js/'),
    filename: 'bundle.js',
  },
  module: {
    loaders: [
      {
        // Test for js or jsx files
        test: /\.jsx?$/,
        loader: 'babel-loader',
        query: {
          // Convert ES6 syntax to ES5 for browser compatibility
          presets: ['es2015', 'react'],
        },
      },
    ],
  },
  resolve: {
    extensions: ['.js', '.jsx'],
  },
};
