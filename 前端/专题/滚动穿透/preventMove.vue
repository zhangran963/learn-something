<template>
  <div class="page-prevent-move">
    <!-- 页面中, 内容多, 需要滚动 -->
    <p>弹窗时, 禁止滑动</p>
    <p>弹窗时, 禁止滑动</p>
    <p>弹窗时, 禁止滑动</p>
    <p>弹窗时, 禁止滑动</p>
    <p>弹窗时, 禁止滑动</p>
    <p>弹窗时, 禁止滑动</p>
    <p>弹窗时, 禁止滑动</p>
    <p>弹窗时, 禁止滑动</p>
    <p>弹窗时, 禁止滑动</p>
    <p>弹窗时, 禁止滑动</p>
    <p>弹窗时, 禁止滑动</p>
    <p>弹窗时, 禁止滑动</p>
    <p>弹窗时, 禁止滑动</p>
    <p>弹窗时, 禁止滑动</p>
    <p>弹窗时, 禁止滑动</p>
    <p>弹窗时, 禁止滑动</p>
    <p>弹窗时, 禁止滑动</p>
    

    <!-- 弹窗盒子: 禁止全部move -->
    <div class="popup" v-if="show" @touchmove.prevent>

      <!-- 弹窗里的内容盒子: 接受到move后,不再冒泡 -->
      <!-- 两种情况 -->
      <!-- 1. 内容少, 本身不用滚动 -->
      <!-- 2. 内容多, 需要滚动 -->
      <div class="content" @touchmove.stop="contentMoveHandler">
        <p>内容</p>
        <p>内容</p>
        <p>内容</p>
        <p>内容</p>
        <p>内容</p>
        <p>内容</p>
        <p>内容</p>
        <p>内容</p>
        <p>内容</p>
        <p>内容</p>
        <p>内容</p>
        <p>内容</p>
        <p>内容</p>
        <p>内容</p>
        <p>内容</p>
        <p>内容</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data: () => ({
    show: true
  }),
  methods: {
    /**
     * 盒子内容不用滚动时的处理
     */
    contentMoveHandler(e){
      const element = e.currentTarget;

      /* scrollHeight: Math.max(某元素内部内容的全部高度, 自身高度) */
      /* clientHeight: 某元素自身的实际高度 */
      /* 一般有: clientHeight <= scrollHeight */
      if(element.scrollHeight === element.clientHeight){
        /* 不支持滑动, 屏蔽滑动行为 */
        e.preventDefault()
      }
    }
  }
};
</script>

<style lang="css" scoped>
/* 弹窗 */
.popup{
  position: fixed;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  z-index: 10;
  background-color: rgba(0, 0, 0, 0.65);

  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}
/* 弹窗中的内容盒子 */
.popup .content{
  width: 80vw;
  height: 50vh;
  background-color: white;
  overflow-y: scroll;
}
.popup .content p{
  background-color: lightblue;
}
</style>
