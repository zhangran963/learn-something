### Proxy
对目标对象的某些属性做的操作拦截, 包括 读取(get)/设置(set)/运行(apply) 等;

1. get: 拦截某个属性的读取操作
    * 目标对象
    * 属性名
    * ?proxy实例(也是this)
    ```js
        const person = {
            name: '张三'
        }
        let proxyPerson = new Proxy(person, {
            get(target, key, receiver){
                if(key in target){
                    console.log(`通过 proxy 读取 ${key}`);
                    return target[key];
                }else{
                    throw ReferenceError(`属性${key}不存在`)
                }
            }
        })

        console.log(proxyPerson.name)
        console.log(proxyPerson.names)
        /**
         * 注: 读取的对象是 proxy 实例(proxyPerson); 直接读取原对象(person), 不会经过代理;
         * /
    ```
    ![tu](http://ww1.sinaimg.cn/large/006tNc79gy1g5rxoz6l2zj30je0aumxh.jpg)


2. set: 拦截某个属性的赋值操作
    * 目标对象
    * 属性名
    * 属性值
    * ?proxy实例(也是this)
    ```js
        const person = {
            name: '张三'
        }
        let proxyPerson = new Proxy(person, {
            get(target, key, receiver){
                return target[key];
            },
            set(target, key, value, receiver){
                if(key in target){
                    return Reflect.set(target, key, value, receiver)
                }else{
                    throw ReferenceError(`属性${key}不存在`)
                }
            }
        })

        proxyPerson.name = '新名字'
        console.log(proxyPerson.name)
    ```
    ![proxy的 set属性](http://ww2.sinaimg.cn/large/006tNc79gy1g5ry2loh6gj30ns02ot8k.jpg)