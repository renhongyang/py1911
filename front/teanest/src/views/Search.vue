<template>
    <div class="search">
        <div class="header">
            <van-nav-bar
                    id="search"
                    left-arrow
                    @click-left="onClickLeft"
                    @click-right="onClickRight"
            >
                <input v-model="value" id="searchinput" slot="title" placeholder="请输入搜索内容" />

                <van-icon name="search" slot="right" ></van-icon>>
            </van-nav-bar>
        </div>

        <div class="other">
            <p>历史搜索</p>
            <div class="searchhot">
                <van-tag  mark plain class='searchitem' @click="searchHot(item)" v-for="item in searchHistory" type="primary">{{item}}</van-tag>
                <van-button color="#7232dd" plain size="large" @click="claerhistory">清除搜索历史</van-button>
            </div>

            <p>热门搜索</p>
            <div class="searchhot">
                <van-tag round plain class='searchitem' @click="searchHot(item)" v-for="item in hotsearch" type="danger">{{item}}</van-tag>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data(){
            return{
                value:"",
                hotsearch:["中茶","大益","下关","七彩云南","八角亭","紫砂"],
                historySearch: JSON.parse(localStorage.getItem("historySearch"))||[]
            }
        },
        computed:{
            searchHistory(){
                // let now = localStorage.getItem("historySearch");
                return this.historySearch

            }
        },
        methods: {
            onClickLeft() {
                this.$router.go(-1)
            },
            onClickRight() {
                if(this.value.length<=0){
                    this.$toast("请输入搜索内容")
                }
                else{
                    this.$toast(`搜索了${this.value}`);
                    this.historySearch.unshift(this.value);
                    console.log(this.historySearch);
                    localStorage.setItem("historySearch",JSON.stringify(this.historySearch));
                    this.value=""
                }

            },
            searchHot(item){
                this.$toast(`搜索了${item}`);

            },
            claerhistory(){
                this.historySearch=[];
            }
        }
    }
</script>


<style scoped="scoped" lang="less">
    .header{

        #search{
            background-color: #f2f2f2;
        }
        #searchinput{
            height: 30px;
            line-height: 30px;
            border: none;
        }
    }
    .other{
        img{
            width: 100%;
        }
        .searchhot{
            padding: 20px;
            display: flex;
            flex-wrap: wrap;
            .searchitem{
                margin: 10px;
                padding: 10px;
            }
        }
    }
</style>
