import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Category from '../views/Category.vue'
import Detail from '../views/Detail.vue'
import Search from '../views/Search.vue'
import Cart from '../views/Cart.vue'
import Mine from '../views/Mine.vue'
import Regist from '../views/Regist.vue'
import ForgotPwd from "../views/ForgotPwd"
import Login from "../views/Login"
import Kefu from "../views/Kefu"
import Userset from "../views/Userset";


Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
    meta:{
      tabbar:true
    }
  },

  {
    path: '/category',
    name: 'category',
    component: Category,
    meta:{
      tabbar:true
    }
  },
  {
    path: '/detail',
    name: 'detail',
    component: Detail
  },
  {
    path: '/search',
    name: 'search',
    component: Search
  },
  {
    path: '/cart',
    name: 'cart',
    component: Cart,
    meta:{
      tabbar:true
    }
  },
  {
    path: '/mine',
    name: 'mine',
    component: Mine,
    meta:{
      auth:true,
      tabbar:true
    }
  },
  {
    path: '/regist',
    name: 'regist',
    component: Regist,
    meta:{
      tabbar:false
    }
  },
  {
    path: '/forgotpwd',
    name: 'forgotpwd',
    component: ForgotPwd,
    meta:{
      tabbar:true
    }

  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/kefu',
    name: 'kefu',
    component: Kefu
  },
  {
    path: '/userset',
    name: 'userset',
    component: Userset
  },

];

const router = new VueRouter({
  routes,
  scrollBehavior(){
    return{
      x:0,
      y:0
    }
  }
});

// router.beforeEach(function (t,f,n) {
//   if(t.meta.auth){
//     let  r=localStorage.getItem("login");
//     if(r){
//       n();
//     }
//     else {
//       n("/login?t="+t.path)
//     }
//   }
//   else {
//     n();
//     // n（next）表示这个函数下一步要干什么
//   }
//
// });


export default router


