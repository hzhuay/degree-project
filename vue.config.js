module.exports = {
    // publicPath: './',
    // outputDir:'dist',
    // assetsDir:'static',
    configureWebpack: {
        // externals: { AMap: 'AMap' },
        resolve: {
            alias: {
                'assets': '@/assets',
                'components': '@/components',
                'views': '@/views',
            }
        }
    },
    devServer: {
        port: '8080',
        open: true,
        proxy: {//解决跨域问题
            '/webapi': {
                // 此处的写法，目的是为了 将 /api 替换成 https://autumnfish.cn/
                target: '127.0.0.1:8080',
                // 允许跨域
                changeOrigin: true,
                ws: true,
                pathRewrite: {
                    '^/webapi': ''
                }
            }
        }
    }
};
