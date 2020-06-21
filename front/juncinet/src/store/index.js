import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({

  state: {
    goodList:[],
    flag:"",
  },

  getters:{

    getGoodList(state){
      return state.goodList
    }
  },

  mutations: {

    addGood(state,good){
      let canAdd=true;
      let index=-1;
      state.goodList.forEach((item,i)=>{
        if(item.id===good.id){
          canAdd=false;
          index=i;
        }
      });
      if (canAdd){
        state.goodList.push(good);
      }
      else {
        state.goodList[index].num+=good.num;
      }
    },
    removeGood(state,index){
      state.goodList.splice(index,1)
    },
    ChangeGoodNum(state,index_num){

      state.goodList[index_num[0]].num=index_num[1];

    }
  },

  actions: {
  },

  modules: {
  }
})