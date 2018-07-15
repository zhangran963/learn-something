坐标转换`ol.proj.fromLonLat([-90, 40])` eg:`center: ol.proj.fromLonLat([-90, 40])`;
最大是`ol.proj.fromLonLat([90,90])`,变成`(90*111319.49079327358,90*2*111319.49079327358)`

得到经纬度:`ol.coordinate.toStringHDMS(ol.proj.transform(
            xxx , 'EPSG:3857', 'EPSG:4326'))`

四舍五入经纬度: `ol.coordinate.toStringXY( xxx , 3)`

给边界做转换 `boundingExtent = ol.proj.transformExtent([10,10,30,40], ol.proj.get('EPSG:4326'), ol.proj.get('EPSG:3857'));`


map获取或设置中心点
```
var view = map.getView();
var mapCenter = view.getCenter();
mapCenter[0] += 50000;
view.setCenter(mapCenter);
map.render();
```
`map.getView().setCenter([xxx,yyy])` 设置中心(移动)

`map.getView().fit( [-14500000, 2000000, -4500000, 7000000],map.getSize());` 使地图大小和显示区域自适应;

`map.getView().animate({zoom: map.getView().getZoom(),center: [(mapProperty.maxW+mapProperty.minW)/2+1000000,(mapProperty.maxH+mapProperty.minH)/2]});` 通过animate形式设置位置

`map.getLayers().getArray()[0].setVisible(true);` (先设置layers不可见)设置layers可见;


得到大小
`map.getSize()` 获得数组,页面显示的DOM的大小;

设置位置
`map.getView().setCenter([-12573476.208221529, 5300621.372044271])`

获得source设置项
`map.getLayers().getArray()[0].getSource().getParams()`其中, 获取source需要用`.getArray()[0]`处理一下;
