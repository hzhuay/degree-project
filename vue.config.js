module.exports = {
    publicPath: './',
    // outputDir:'dist',
    assetsDir:'static',
    configureWebpack: {
        // externals: { AMap: 'AMap' },
        resolve: {
            alias: {
                'assets': '@/assets',
                'components': '@/components',
                'views': '@/views',
                'common': '@/common',
                'network': '@/network'
            }
        }
    },
    devServer: {
        open: true,
        proxy: {//解决跨域问题
            '/api': {
                // 此处的写法，目的是为了 将 /api 替换成 https://autumnfish.cn/
                target: 'http://localhost:5000',
                // 允许跨域
                changeOrigin: true,
                ws: true,
                pathRewrite: {
                    '^/api': '/'
                }
            }
        }
    },
};
