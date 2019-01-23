1. `border-width: 0.5px;`
    * 只在 retina 版 iphone中生效, Android 手机中不适用;
    * outline 同样效果;
2. 通过 `transform:scale(倍数)` 的形式;
```less
// all
.border-1px {
    position: relative;

    &::after{
        content: "";
        position: absolute;
        left: 0;
        top: 0;
        width: 200%;
        height: 200%;
        border: 1px solid black;
        border-radius: 16px;
        transform-origin: 0 0;
        transform: scale(0.33);
    }
}


// left
.border-left-1px {
    position: relative;

    &::after{
        content: "";
        position: absolute;
        left: 0;
        top: 0;
        bottom: 0;
        // 处理1: 宽度+背景色
        //width: 1px;
        //background-color: black;
        // 处理2: 某一边的border
        border-left: 1px solid #333;
        -webkit-transform-origin: 0 0;
        // 起始点 0 0
        transform-origin: 0 0;
        -webkit-transform: scaleX(0.5);
        // 对 X 方向缩放
        transform: scaleX(0.5);
    }
}

// right
.border-right-1px {
    position: relative;

    &::after{
        content: "";
        position: absolute;
        right: 0;
        top: 0;
        bottom: 0;
        border-left: 1px solid #333;
        -webkit-transform-origin: 100% 0;
        transform-origin: 100% 0;
        -webkit-transform: scale(0.5);
        transform: scaleX(0.5);
    }
}

// top
.border-top-1px {
    position: relative;

    &::after{
        content: "";
        position: absolute;
        left: 0;
        right: 0;
        top: 0;
        // 处理1: 高度+背景色
        // height: 1px;
        // backgrond-color: black;
        // 处理2: 某一边的border
        border-top: 1px solid black;
        // 起始点 0 0
        -webkit-transform-origin: 0 0;
        transform-origin: 0 0;
        -webkit-transform: scaleY(0.5);
        // 对 Y 方向缩放
        transform: scaleY(0.5);
    }
}

// bottom
.border-bottom-1px {
    position: relative;

    &::after{
        content: "";
        position: absolute;
        left: 0;
        right: 0;
        bottom: 0;
        border-top: 1px solid black;
        -webkit-transform-origin: 0 0;
        transform-origin: 0 100%;
        -webkit-transform: scaleY(0.5);
        // 对 Y 方向缩放
        transform: scaleY(0.5);
    }
}
```