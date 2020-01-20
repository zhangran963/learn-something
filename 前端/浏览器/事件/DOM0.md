### DOM0级绑定的事件
* `参数 event`: 事件对象
* `参数 parentNode`: 发起事件元素的父元素
* `with`参数, 指定后面包含的元素的 变量所挂载到的对象
```html
<body>
  页面内容
  <form id="form">
    <input>
    <img src="" onerror="print(event, parentNode)">
  </form>

  <script>
    /**
     * 将函数绑定到img元素上
     * @param event 事件
     * @param parentNode 父DOM, 此处是 form
     */
    function print(event, parentNode){
      console.log('* event', event)
      console.log('* parentNode', parentNode)
      with(parentNode){
        /* form:DOM */
        console.log('* ', parentNode /* form.parentNode === body */)
      }
    }
  </script>
</body>
```



