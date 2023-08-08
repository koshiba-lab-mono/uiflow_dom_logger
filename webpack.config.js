const path = require("path");
const CopyPlugin = require("copy-webpack-plugin");

module.exports = {
  mode: process.env.NODE_ENV || "development",
  devtool: false,
  entry: {
    content: path.join(__dirname, "src/content.ts"),
    background: path.join(__dirname, "src/background.ts"),
    popup: path.join(__dirname, "src/popup.ts"),
  },
  output: {
    path: path.join(__dirname, "dist/src"),
    filename: "[name].js",
  },
  module: {
    rules: [
      {
        test: /\.ts$/,
        use: "ts-loader",
        exclude: /node_modules/,
      },
    ],
  },
  resolve: {
    extensions: [".ts", ".js"],
  },
  plugins: [new CopyPlugin([{ from: ".", to: "../" }], { context: "public" })],
};
