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
                {{search}}

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
                search:[],
                hotsearch:["孔家钧窑","红远钧窑","茗钧堂","正玉钧窑","凤山钧窑","钧宝坊","钧都坊","开元钧窑","垕彩实业"],
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
                    this.$http({
                        url: `http://127.0.0.1:8000/api/v1/goods/?search=value`,
                        method: "get"
                    }).then(res=>{
                        console.log(res.data,111);
                        if (res.data.code === 200)
                            console.log(res.data.code,333);
                        this.search = res.data;
                        console.log(this.search,222);
                    }).catch(err=>{
                        console.log("发生错误",err)
                    });
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
