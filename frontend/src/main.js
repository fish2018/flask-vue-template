import Vue from 'vue'

import 'normalize.css/normalize.css'// A modern alternative to CSS resets

import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import locale from 'element-ui/lib/locale/lang/en' // lang i18n

import '@/styles/index.scss' // global css

import App from './App'
import router from './router'
import store from './store'

import '@/icons' // icon
import '@/permission' // permission control

Vue.use(ElementUI, { locale })
Vue.config.productionTip = false

Vue.directive('move', {
  inserted: function(a) {
    // 鼠标按下事件
    a.onmousedown = function(e) {
      var disX = e.clientX - a.offsetLeft
      var disY = e.clientY - a.offsetTop

      if (a.setCapture) {
        a.setCapture()
      }
      // 鼠标移动事件-----给文档流绑定移动事件
      document.onmousemove = function(e) {
        e.preventDefault()
        var L = e.clientX - disX
        var T = e.clientY - disY

        L = Math.min(Math.max(L, 0), document.documentElement.clientWidth - a.offsetWidth)
        T = Math.min(Math.max(T, 0), document.documentElement.clientHeight - a.offsetHeight)

        a.style.left = L + 'px'
        a.style.top = T + 'px'
      }
      // 鼠标离开事件
      document.onmouseup = function() {
        document.onmousemove = document.onmousedown = null
        if (a.releaseCapture) {
          a.releaseCapture()// 拖动后在解除事件锁定
        }
      }
    }
  }
})

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
})
