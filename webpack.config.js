const path = require("path");
const CopyPlugin = require("copy-webpack-plugin");
const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = {
  mode: process.env.NODE_ENV || "development",
  devtool: false,
  entry: {
    content: path.join(__dirname, "src/content.ts"),
    background: path.join(__dirname, "src/background.ts"),
    popup: path.join(__dirname, "src/popup.tsx"),
  },
  output: {
    path: path.join(__dirname, "dist/src"),
    filename: "[name].js",
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ["style-loader", "css-loader"],
        exclude: /node_modules/,
      },
      {
        test: /\.(ts|tsx)$/,
        use: "ts-loader",
        exclude: /node_modules/,
      },
    ],
  },
  resolve: {
    extensions: [".ts", ".js", ".tsx"],
  },
  plugins: [
    new HtmlWebpackPlugin({
      inject: "body",
      filename: "../popup.html",
      template: "./public/popup.html",
      chunks: ["popup"],
    }),
    new CopyPlugin([
      {
        from: "./public/manifest.json",
        to: "./../",
      },
    ]),
  ],
};
