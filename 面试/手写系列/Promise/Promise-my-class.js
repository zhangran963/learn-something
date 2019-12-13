const PENDING = 'pending'
const FULFILLED = 'fulfilled'
const REJECTED = 'rejected'

class Promise {
  constructor(executor) {
    this.state = PENDING;
    this.value = undefined;
    this.reason = undefined;

    this.onResolvedCallbacks = [];
    this.onRejectedCallbacks = [];

    // resolve, 其中包含 成功后的处理
    let resolve = (value) => {
      // console.log('>>> resolve:', this.state, value, this.onResolvedCallbacks.length);
      if (this.state === PENDING) {
        this.state = FULFILLED;
        this.value = value;
        // 执行, 一般只有一个函数
        this.onResolvedCallbacks.forEach(fn => fn());
      }
    };
    // reject, 其中包含 失败后的处理
    let reject = (reason) => {
      // console.log('>>> reject:', this.state);
      if (this.state === PENDING) {
        this.state = REJECTED;
        this.reason = reason;
        this.onRejectedCallbacks.forEach(fn => fn());
      }
    };

    try {
      // 执行函数, 用户 new Promsie中执行 或 .then中自动执行
      executor(resolve, reject);
    } catch (err) {
      reject(err);
    }
  }

  // then
  then(onFulfilled, onRejected) {
    // 函数默认值
    onFulfilled = typeof onFulfilled === 'function' ? onFulfilled : value => value;
    onRejected = typeof onRejected === 'function' ? onRejected : err => { throw err };

    let nextPromise = new Promise((resolve, reject) => {

      if (this.state === FULFILLED) {
        // 成功
        setTimeout(() => {
          try {
            let x = onFulfilled(this.value);
            resolvePromise(nextPromise, x, resolve, reject);
          } catch (e) {
            reject(e);
          }
        }, 0);
      } else if (this.state === REJECTED) {
        // 失败
        setTimeout(() => {
          try {
            let x = onRejected(this.reason);
            resolvePromise(nextPromise, x, resolve, reject);
          } catch (e) {
            reject(e);
          }
        }, 0);
      } else if (this.state === PENDING) {
        // 进行中
        // 什么时候执行呢?
        // console.log('>>> push:');
        this.onResolvedCallbacks.push(() => {
          // 此段函数, 在new Promise(函数)中 resolve 中执行
          setTimeout(() => {
            try {
              // this.value, new Promise(函数)中通过 resolve 获得的值
              // 执行succFunc函数
              let x = onFulfilled(this.value);
              // 一般可以 resolve(x), 为了处理 Promise 类的返回对象, 需要处理 Promise
              resolvePromise(nextPromise, x, resolve, reject);
            } catch (e) {
              reject(e);
            }
          }, 0);
        });
        // 
        this.onRejectedCallbacks.push(() => {
          // 此段函数, 在new Promise(函数)中 reject 中执行
          setTimeout(() => {
            try {
              // this.value, (函数)中通过 resolve 获得的值
              let x = onRejected(this.reason);
              // 一般可以 resolve(x), 为了处理 Promise 类的返回对象, 需要处理 Promise
              resolvePromise(nextPromise, x, resolve, reject);
            } catch (e) {
              reject(e);
            }
          }, 0)
        });
      }
    })

    return nextPromise;
  }
  catch(fn) {
    return this.then(null, fn);
  }

  static resolve(val) {
    return new Promise((res, rej) => {
      res(val)
    })
  }

  static reject(val) {
    return new Promise((res, rej) => {
      rej(val)
    })
  }


  static race(promises) {
    return new Promise((res, rej) => {
      for (let i = 0; i < promises.length; i++) {
        // 某一个较快的 Promise 处理了 res 或 rej
        promises[i].then(res, rej)
      }
    })
  }

  //all方法(获取所有的promise，都执行then，把结果放到数组，一起返回)
  static all(promises) {
    // 任一错误, 即触发失败
    // 所有成功, 才触发成功, 按顺序返回成功的数据
    let arr = []

    let collectData = (res, index, data) => {
      arr[index] = data
      if (arr.length === promises.length) {
        res(arr)
      }
    }

    return new Promise((res, rej) => {
      promises.forEach((promise, index) => {
        // 缺陷: 多层 Promise 未解析到最后的 then 再返回
        // Promise化
        if (!(promise instanceof Promise)) {
          promise = Promise.resolve(promise)
        }
        promise.then(collectData.bind(null, res, index), rej)
      })
    })
  }
}

// 处理函数
function resolvePromise(nextPromise, x, resolve, reject) {
  if (x === nextPromise) {
    return reject(new TypeError('Chaining cycle detected for promise'));
  }

  let called;  // 是否继续循环执行
  if (x != null && (typeof x === 'object' || typeof x === 'function')) {
    try {
      // x是 类Promise的对象
      let then = x.then;
      if (typeof then === 'function') {
        // 循环执行 resolvedPromise, 直至都解开.then
        then.call(x, y => {
          if (called) return;
          called = true;
          resolvePromise(nextPromise, y, resolve, reject);
        }, err => {
          if (called) return;
          called = true;
          reject(err);
        })
      } else {
        // 循环执行结束, 返回最终值
        resolve(x);
      }
    } catch (e) {
      if (called) return;
      called = true;
      reject(e);
    }
  } else {
    // 返回最终值
    resolve(x);
  }
}


module.exports = {
  Promise
}
