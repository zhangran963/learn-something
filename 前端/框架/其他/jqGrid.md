### 配置

1. `$("#grid1").jqGrid({ /* xxx */ })` 初始化;
2. 配置文件`bootstrap.min.css`,`ui.jqgrid-bootstrap.css`,`ui.jqgrid-bootstrap-ui.css`,`ui.jqgrid.css`,`jquery.min.js`,`bootstrap.min.js`,`jquery.jqGrid.min.js`,`grid.locale-cn.js`;
3. `var myprop = $("#gridid").jqGrid('getColProp', '数据名');` 获取列;
4. `var myprop = $("#gridid").jqGrid('setColProp', 'name1', {index:'newindex',...});` 设置列;
5. 编写js之前需要写
```
$.jgrid.defaults.width = 780;
$.jgrid.defaults.responsive = true;
$.jgrid.defaults.styleUI = 'Bootstrap';
```
6. `sortorder: asc` :升序(asc)或降序(desc)



### colModel配置:
1. 定义标题的顺序:1.colnames 2.colModel—label 3.colModel—name;
2. `name:'数据属性名'`:定义列;
3. `width:120`:定义宽度;
4. `aligh:center`:设置位置;
5. `formatter`:对列进行格式化时设置的函数名或者类型eg:`integer`,`email`,`link`,`checkbox`;
6.  给formatter设置函数
```
function formatRating(cellValue, options, rowObject){
    cellValue:此处的值;
    options:列对象的值;
    rowObject:行对象的设置内容;
    return "显示内容";
}
```
7. `formatoptions—defaultValue`:设置无内容时的默认值
8. `formatoptions—thousandsSeparator`:设置千分位的分隔符;
9. `formatoptions—suffix`:设置后缀名,例如'USD';
10. `sortable` 取消排序, 不显示箭头;


### 在线json数据
```
{   
    'userdata':{"xxx":"","yyy":"yy"},  /*页脚数据*/
    'rows': [  /*行数据rows*/
        {xxx:xxx,yyy:yyy},
        {xxx:xxx,yyy:yyy},
    ]
}
```

### 卸载jqGrid
`$.jgrid.gridUnload("stationStateTable");` 其中填写的内容是id值;

### 更改宽度
`$("#stationStateTable").jqGrid('setGridWidth', width);`

**添加数据**
`$("#rainfallTable0")[0].addJSONData(newData);`

** 更新数据 **
`jQuery("#grid_id").trigger("reloadGrid");`

** 清除数据 **
`jQuery("#grid_id").trigger("clearGridData");`

** 自定义json **
```
jsonReader:{
    root: 'data'
},
```
** 加载完成 **
```
loadComplete: function(){
    console.log("加载完了");
    $("#rainfallTable0").jqGrid("clearGridData");
}
```

** 读取数据 **
```
$('#rainfallTable0').jqGrid('getRowData');
```

** 更新数据 **
```
$('#rainfallTable0').jqGrid('clearGridData').jqGrid('setGridParam', {data: newdata, datatype: 'local'}).trigger('reloadGrid');
```

** 显示进度条 **
```
$("#rainfallTable0")[0].grid.beginReq();  //开始时间条
$("#rainfallTable0")[0].grid.endReq();  //结束时间条
```
