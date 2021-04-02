import axios from 'axios'

export function request(config) {
    // 创建axios实例
    const instance = axios.create({
        baseURL: 'http://localhost:5000',
        timeout: 5000
    })

    // 请求拦截器
    // instance.interceptors.request.use(con => {
    //     // 这里可以对请求的配置进行修改，比如说config不符合服务器要求
    //     // 或者每次发送网络请求时，都希望在前端界面中显示一个图标
    //     // 某些网络网络请求，比如说登录时需要token，可以在前端验证
    //     // 拦截下来的请求配置一定要返回回去，不然请求就无法完成
    //     return con;
    // }, err => {
    //     console.log(err);
    // })

    // 响应拦截器
    instance.interceptors.response.use(res => {
        // console.log(res)
        return res.data;
    }, err => {
        console.log(err);
    })

    // 发送网络请求
    return instance(config);
}

/*
使用方式
request({
    url: '/home',
    method: "POST"
}).then(res => {
    console.log(res);
}).catch(err => {
    console.log(err);
})
 */

/*
有异步操作时，需要使用Promise，链式编程代替嵌套式回调
new Promise((resolve, reject) => {
    // 异步操作，比如网络请求

    // 把网络请求到的数据data放入resolve中，就会调用then()
    resolve(data)

    // 如果失败的话，就把错误信息传入reject
    reject(err)
}).then((data) => {
    // 对数据进行处理
}).catch((err) => {
    // 对错误进行处理
})

Promise有三种状态：Pending, Fulfilled, Rejected

new Promise((resolve, reject) => {
    // 异步操作
}).then(res => {
    // 第一步处理，把res处理为newRes
    return newRes;
}).then(res => {
    // 第二步操作
    // 可以抛出异常进入catch函数
    throw 'error'
}).catch(err => {

})

axios.all(axios({}), axios({})).then()

 */
