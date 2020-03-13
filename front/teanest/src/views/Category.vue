<template>
    <div class="category">
        <div class="header">
            <van-nav-bar
                    title="商品分类"
                    @click-left="onClickLeft"
                    @click-right="onClickRight">
                <van-icon name="arrow-left" slot="left" color="#000000" size="20"></van-icon>
                <van-icon name="search" slot="right" color="#000000" size="20"></van-icon>
            </van-nav-bar>
            <img src="http://www.chawo.com/wap/images/chawo-logo.png">

        </div>
        <div class="con">
            <div class="con-header" >
<!--                <van-sidebar class="active_box" v-model="activeKey">-->
<!--                    <van-sidebar-item  v-for="(name,index) in names" :title="name">-->
<!--                    </van-sidebar-item>-->
<!--                </van-sidebar>-->
                <van-tabs>
                    <van-tab v-for="(item,index) in categorys" :title="item.title">

                        <div class="con-brands" v-if="index===0">
                            <div class="brands" v-for="(item,index) in brands"  @click="search(item)">
                                <!--                    <router-link :to="'/category/'+item.brand_id">-->
                                <img :src="item.img" alt="">
                                <p>{{item.name}}</p>
                                <!--                    </router-link>-->
                            </div>
                        </div>


                        <div class="tea" v-if="index===1">
                            <div v-for="(tea,index) in goods" v-if="tea.category === 2" >
                                <router-link :to="'/detail/'+tea.id+'/'">
                                    <van-card
                                            :price="tea.prise"
                                            :desc="tea.desc"
                                            :title="tea.name"
                                            :thumb="tea.img">
                                        <div slot="tags" class="tags">
                                            <van-tag plain type="danger">销量：{{tea.sellnum}}</van-tag>
                                        </div>
                                    </van-card>
                                </router-link>
                                <br>
                            </div>
                        </div>

                        <div class="tea" v-if="index===2">
                            <div v-for="(tea,index) in goods" v-if="tea.category === 3" >
                                <router-link :to="'/detail/'+tea.id+'/'">
                                <van-card
                                        :price="tea.prise"
                                        :desc="tea.desc"
                                        :title="tea.name"
                                        :thumb="tea.img">
                                    <div slot="tags" class="tags">
                                        <van-tag plain type="danger">销量：{{tea.sellnum}}</van-tag>
                                    </div>
                                </van-card>
                                </router-link>
                                <br>
                            </div>
                        </div>


                        <div class="tea" v-if="index===3">
                            <div v-for="(tea,index) in goods" v-if="tea.category === 4" @click="GoDetail">
                                <router-link :to="'/detail/'+tea.id+'/'">
                                <van-card
                                        :price="tea.prise"
                                        :desc="tea.desc"
                                        :title="tea.name"
                                        :thumb="tea.img">
                                    <div slot="tags" class="tags">
                                        <van-tag plain type="danger">销量：{{tea.sellnum}}</van-tag>
                                    </div>
                                </van-card>
                                </router-link>
                                <br>
                            </div>
                        </div>

                        <div class="tea" v-if="index===4">
                            <div v-for="(tea,index) in goods" v-if="tea.category === 5" @click="GoDetail">
                                <van-card
                                        :price="tea.prise"
                                        :desc="tea.desc"
                                        :title="tea.name"
                                        :thumb="tea.img">
                                    <div slot="tags" class="tags">
                                        <van-tag plain type="danger">销量：{{tea.sellnum}}</van-tag>
                                    </div>
                                </van-card>
                                <br>
                            </div>
                        </div>

                        <div class="tea" v-if="index===5">
                            <div v-for="(tea,index) in goods" v-if="tea.category === 6" @click="GoDetail">
                                <van-card
                                        :price="tea.prise"
                                        :desc="tea.desc"
                                        :title="tea.name"
                                        :thumb="tea.img">
                                    <div slot="tags" class="tags">
                                        <van-tag plain type="danger">销量：{{tea.sellnum}}</van-tag>
                                    </div>
                                </van-card>
                                <br>
                            </div>
                        </div>

                        <div class="tea" v-if="index===6">
                            <div v-for="(tea,index) in goods" v-if="tea.category === 7" @click="GoDetail">
                                <van-card
                                        :price="tea.prise"
                                        :desc="tea.desc"
                                        :title="tea.name"
                                        :thumb="tea.img">
                                    <div slot="tags" class="tags">
                                        <van-tag plain type="danger">销量：{{tea.sellnum}}</van-tag>
                                    </div>
                                </van-card>
                                <br>
                            </div>
                        </div>

                        <div class="tea" v-if="index===7">
                            <div v-for="(tea,index) in goods" v-if="tea.category === 8" @click="GoDetail">
                                <van-card
                                        :price="tea.prise"
                                        :desc="tea.desc"
                                        :title="tea.name"
                                        :thumb="tea.img">
                                    <div slot="tags" class="tags">
                                        <van-tag plain type="danger">销量：{{tea.sellnum}}</van-tag>
                                    </div>
                                </van-card>
                                <br>
                            </div>
                        </div>

                        <div class="tea" v-if="index===8">
                            <div v-for="(tea,index) in goods" v-if="tea.category === 9" @click="GoDetail">
                                <van-card
                                        :price="tea.prise"
                                        :desc="tea.desc"
                                        :title="tea.name"
                                        :thumb="tea.img">
                                    <div slot="tags" class="tags">
                                        <van-tag plain type="danger">销量：{{tea.sellnum}}</van-tag>
                                    </div>
                                </van-card>
                                <br>
                            </div>
                        </div>

                        <div class="tea" v-if="index===9">
                            <div v-for="(tea,index) in goods" v-if="tea.category === 10" @click="GoDetail">
                                <van-card
                                        :price="tea.prise"
                                        :desc="tea.desc"
                                        :title="tea.name"
                                        :thumb="tea.img">
                                    <div slot="tags" class="tags">
                                        <van-tag plain type="danger">销量：{{tea.sellnum}}</van-tag>
                                    </div>
                                </van-card>
                                <br>
                            </div>
                        </div>

                        <div class="tea" v-if="index===10">
                            <div v-for="(tea,index) in goods" v-if="tea.category === 11" @click="GoDetail">
                                <van-card
                                        :price="tea.prise"
                                        :desc="tea.desc"
                                        :title="tea.name"
                                        :thumb="tea.img">
                                    <div slot="tags" class="tags">
                                        <van-tag plain type="danger">销量：{{tea.sellnum}}</van-tag>
                                    </div>
                                </van-card>
                                <br>
                            </div>
                        </div>


                    </van-tab>
                </van-tabs>
            </div>
        </div>
    </div>


</template>

<script>
    export default {
        name: 'category',
        components: {

        },
        data(){
            return{
                activeKey: "",
                vulue:"",
                categorys:[],
                brands:[],
                goods:[]


        }

        },
        methods: {
            onClickLeft() {
                this.$router.go(-1);
            },
            onClickRight() {
                this.$router.push("/search");
            },
            // onChange(index) {
            //     console.log(index,this.activeKey);
            // }
            search(item){
                this.$toast(`搜索了${item.name}`);
            },
            GoDetail(){
                this.$router.push("/detail")
            }
        },
        created() {

            this.$http({
                url: `http://127.0.0.1:8000/api/v1/categorys/`,
                method: "get"
            }).then(res=>{
                // console.log(res.data,111);
                if (res.data.code === 200)
                    console.log(res.data.code,333);
                this.categorys = res.data;
                // console.log(this.categorys,222);
            }).catch(err=>{
                console.log("发生错误",err)
            });

            this.$http({
                url: `http://127.0.0.1:8000/api/v1/brands/`,
                method: "get"
            }).then(res=>{
                // console.log(res.data,111);
                if (res.data.code === 200)
                    console.log(res.data.code,333);
                this.brands = res.data;
                // console.log(this.brands,222);
            }).catch(err=>{
                console.log("发生错误",err)
            });

            this.$http({
                url: `http://127.0.0.1:8000/api/v1/goods/`,
                method: "get"
            }).then(res=>{
                // console.log(res.data,111);
                if (res.data.code === 200)
                    console.log(res.data.code,333);
                this.goods = res.data;
                // console.log(this.goods,222);
            }).catch(err=>{
                console.log("发生错误",err)
            });

        }

    }
</script>


<style scoped="scoped" lang="less">
    .header{
        background-color: #f2f2f2;
        color: #000000;

        img{
            z-index: 5 ;
            width: 50px;
            position: absolute;
            top: 10px;
            left: 50px;

        }
    }

    .con-brands{
        display: flex;
        width: 100%;
        flex-wrap: wrap;
        justify-content: space-around;
    }


</style>