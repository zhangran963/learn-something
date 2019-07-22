const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const UglifyJSPlugin = require('uglifyjs-webpack-plugin');
const OptimizeCssAssetsPlugin = require('optimize-css-assets-webpack-plugin')
const CleanWebpackPlugin = require('clean-webpack-plugin');

module.exports = {
	entry: {
		index: "./src/index.js"
	},
	output: {
		path: path.resolve(__dirname, "dist"),
		filename: "js/[name].[hash].bundle.js"
    },
    module: {
        rules: [{
            // 高级语法 => ES5
            test: /\.js$/,
            exclude: /(node_modules|bower_components)/,
            use: {
                loader: 'babel-loader',
                options: {
                    presets: ['@babel/preset-env'],
                    babelrc: false
                }
            }
        }, {
            // css文件
            test: /\.css$/,
            use: [{
                loader: MiniCssExtractPlugin.loader,
                options: {
                    publicPath: '../'
                }
            },{
                loader: 'css-loader',
                options: {
                    url: true,
                    modules: 'global'
                }
            }]
        },{
            // 处理 html 文件中的 url 
            test: /\.html$/,
            use: [{
                loader: 'html-loader',
                options: {
                    attrs: [
                        'img:src',
                        'link:href',
                        'video:src',
                        'video:poster'
                    ]
                }
            }]
        },{
            // 用 file-loader 处理特殊文件路径
            test: /icon256\.png$/,
            use: [{
                loader: 'file-loader',
                options: {
                    name(file){
                        return "[path][name].[ext]?[hash]";
                    }
                }
            }]
        }, {
            // url-loader = file-loader + 转换base64能力
            test: /\.(png|jpg|gif|svg|eot|ttf|woff|woff2|mp4|ico)$/,
            exclude: /icon256\.png$/,
            use: [{
                loader: 'url-loader',
                options: {
                    limit: 8192,
                    name(file){
                        return '[path][name].[ext]?[hash]';
                    }
                }
            }]
        }]
    },
    plugins: [
        // 清除dist
        new CleanWebpackPlugin( {
            root: __dirname,
            verbose: true
        }),
        // 自动在 html 中添加 script link;
        new HtmlWebpackPlugin({
            minify: {
                collapseWhitespace: true,
            },
            chunks: ['index'],
            filename: 'indexs.html',
            template: './src/layout/index.html'
        }),
        // css 文件独立出来
        new MiniCssExtractPlugin({
            filename: 'css/[name].[hash].css'
        })
    ],
    optimization: {
        minimizer: [
            // 压缩
            new UglifyJSPlugin({
                cache: true,
                parallel: true,
                sourceMap: true
            }),
            new OptimizeCssAssetsPlugin({})
        ]
    },
    devtool: 'source-map'
};