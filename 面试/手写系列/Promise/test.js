

const sleep = (time=0) => new Promise((res, rej)=> setTimeout(res, time))
const { Promise } = require('./Promise-my-class')

new Promise((res, rej) => {
  /**
   * 在浏览器中表现良好
   * 在 Node 中, 总是 sleep/setTimeout 之后再触发 res/rej
   */
  sleep(1000).then(_ => {
    res('成功参数')
  })
  rej('失败参数')
}).then((arg) => {
  console.log('>>> 成功:', arg);
}, (err) => {
  console.log('>>> 失败:', err);
})