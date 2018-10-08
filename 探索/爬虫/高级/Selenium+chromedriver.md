* Selenium: `pip3 install selenium`
* chromedriver: 下载驱动`https://sites.google.com/a/chromium.org/chromedriver/downloads`


```py
from selenium import webdriver


driver_path = r"/Users/ran/Downloads/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)

driver.get("https://www.baidu.com")

time.sleep(5)   # 稍作延时

driver.close()  # 关闭页签
driver.quit()   # 退出浏览器
```

### 获取页面元素
* ``
```py
submitTag = driver.find_element_by_id("submit")  # 通过 ID

submitTag = driver.find_element_by_class_name("submit")  # 通过class

submitTag = driver.find_element_by_name("submit")  # 通过 name

submitTag = driver.find_element_by_tag_name("submit")  # 通过 TagName

submitTag = driver.find_element_by_xpath("//submit")  # 通过 xpath 语法

submitTag = driver.find_element_by_css_selector("")  # 通过 ID

# 以上所有版本都有 elements 形式
# 如:submitTag = driver.find_elements_by_class_name("submit")  # 通过class
```



### 表单元素
* 常用元素 `input button checkbox select`

```py
inputTag.send_keys("python")  # 给 input元素添加值
inputTag.clear()        # 清除值

buttonTag.click()   # 点击事件

selectTag.select_by_index( 1 )  # 选中某一项, 从0开始
selectTag.select_by_value( "http://" )  # 根据 option 的 value 值
selectTag.select_by_visible_text( "显示内容" )  # 根据 显示的值
selectTag.deselect_all()   # 取消选中
```


### 行为链
```py
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver_path = r"/Users/ran/Downloads/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)

driver.get("https://www.baidu.com")

# 定义 input输入框 和 提交按钮
inputTag = driver.find_element_by_id("kw")
submitBtn = driver.find_element_by_id("su")

# 定义 action 和 一步一步的行为
action = ActionChains(driver)
action.move_to_element(inputTag)
action.send_keys_to_element(inputTag, "python")
action.move_to_element(submitBtn)
action.click(submitBtn)
action.perform() # 开始执行
```
* 其他行为 api
    * `click_and_hold(element)`: 点击但不放松
    * `context_click(element)`: 右键点击
    * `double_click(element)`: 双击



### Cookie 操作
```py
# 获取所有的 cookie
for cookie in driver.get_cookies():
    print(cookie)

# 根据 key 值获取 value
# value 值是 cookie 内容里面的 name 对应的值
value = driver.get_cookie(key)

# 删除所有 cookie
driver.delete_all_cookies()

# 删除某个 cookie
driver.delete_cookie(key)
```


### 多页签

```py
# 打开新页面
self.driver.execure_script("window.open('https://www.douban.com')")

driver.current_url  # 当前页面

driver.window_handles[1]  # 获取当前窗口组(从0开始)
driver.switch_to_window( driver.window_handles[1] )  # 切换到第二个窗口
```


### 使用代理服务器
```py
# 设置代理
options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://182.111.64.7:36323")

driver_path = r"/Users/ran/Downloads/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path,chrome_options=options)  # 使用代理

driver.get("http://httpbin.org/ip")  # 在访问的网页中显示此代理的 IP
```