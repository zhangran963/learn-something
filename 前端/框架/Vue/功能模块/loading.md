### 带有延迟关闭的 loading
```js
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(ElementUI);

/**
 * 带有延迟关闭的 loading
 */
import { Loading } from 'element-ui';
Vue.prototype.$loadings = {
    loading: null,
    timer: 0,
    show(text=''){
        this.loading = Loading.service({fullscreen: true, text,})

        this.timer = 0;
        setInterval(()=>{ this.timer+=10 }, 10);
    },
    close(){
        console.log(this.timer)
        // 最长时间
        if(this.timer>=2000){
            this.loading.close();
            this.timer = 0;
        }else{
            setTimeout(this.close.bind(this), 100);
        }
    }
}
```