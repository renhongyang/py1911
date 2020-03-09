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
                    <van-tab v-for="(name,index) in names" :title="name">
<!--                        <p>{{name}}</p>-->
                        <div class="con-brands" v-if="index===0">
                            <div class="brands" v-for="(item,index) in brands_list" @click="search(item)">
                                <!--                    <router-link :to="'/category/'+item.brand_id">-->
                                <img :src="item.brand_pic" alt="">
                                <p>{{item.brand_name}}</p>
                                <!--                    </router-link>-->
                            </div>
                        </div>

                        <div class="tea" v-if="index===1">
                            <div v-for="(tea,index) in puer_tea" @click="GoDetail">
                                <van-card
                                        :price="tea.prise"
                                        :desc="tea.desc"
                                        :title="tea.name"
                                        :thumb="tea.tea_img">
                                    <div slot="tags" class="tags">
                                        <van-tag plain type="danger">销量：{{tea.number}}</van-tag>
                                    </div>
                                </van-card>
                                <br>
                            </div>
                        </div>

                        <div class="tea" v-if="index===2" >
                            <div v-for="(tea,index) in red_tea" @click="GoDetail">
                                <van-card
                                        :price="tea.prise"
                                        :desc="tea.desc"
                                        :title="tea.name"
                                        :thumb="tea.tea_img">
                                    <div slot="tags" class="tags">
                                        <van-tag plain type="danger">销量：{{tea.number}}</van-tag>
                                    </div>
                                </van-card>
                                <br>
                            </div>
                        </div>

                        <div class="tea" v-if="index===3" >
                            <div v-for="(tea,index) in green_tea" @click="GoDetail">
                                <van-card
                                        :price="tea.prise"
                                        :desc="tea.desc"
                                        :title="tea.name"
                                        :thumb="tea.tea_img">
                                    <div slot="tags" class="tags">
                                        <van-tag plain type="danger">销量：{{tea.number}}</van-tag>
                                    </div>
                                </van-card>
                                <br>
                            </div>
                        </div>

                        <div class="tea" v-if="index===4" >
                            <div v-for="(tea,index) in wul_tea" @click="GoDetail">
                                <van-card
                                        :price="tea.prise"
                                        :desc="tea.desc"
                                        :title="tea.name"
                                        :thumb="tea.tea_img">
                                    <div slot="tags" class="tags">
                                        <van-tag plain type="danger">销量：{{tea.number}}</van-tag>
                                    </div>
                                </van-card>
                                <br>
                            </div>
                        </div>

                        <div class="tea" v-if="index===5" >
                            <div v-for="(tea,index) in black_tea" @click="GoDetail">
                                <van-card
                                        :price="tea.prise"
                                        :desc="tea.desc"
                                        :title="tea.name"
                                        :thumb="tea.tea_img">
                                    <div slot="tags" class="tags">
                                        <van-tag plain type="danger">销量：{{tea.number}}</van-tag>
                                    </div>
                                </van-card>
                                <br>
                            </div>
                        </div>

                        <div class="tea" v-if="index===6" >
                            <div v-for="(tea,index) in white_tea" @click="GoDetail">
                                <van-card
                                        :price="tea.prise"
                                        :desc="tea.desc"
                                        :title="tea.name"
                                        :thumb="tea.tea_img">
                                    <div slot="tags" class="tags">
                                        <van-tag plain type="danger">销量：{{tea.number}}</van-tag>
                                    </div>
                                </van-card>
                                <br>
                            </div>
                        </div>


                        <div class="tea" v-if="index===7" >
                            <div v-for="(tea,index) in flowers_tea" @click="GoDetail">
                                <van-card
                                        :price="tea.prise"
                                        :desc="tea.desc"
                                        :title="tea.name"
                                        :thumb="tea.tea_img">
                                    <div slot="tags" class="tags">
                                        <van-tag plain type="danger">销量：{{tea.number}}</van-tag>
                                    </div>
                                </van-card>
                                <br>
                            </div>
                        </div>

                        <div class="tea" v-if="index===8" >
                            <div v-for="(tea,index) in tea_books" @click="GoDetail">
                                <van-card
                                        :price="tea.prise"
                                        :desc="tea.desc"
                                        :title="tea.name"
                                        :thumb="tea.tea_img">
                                    <div slot="tags" class="tags">
                                        <van-tag plain type="danger">销量：{{tea.number}}</van-tag>
                                    </div>
                                </van-card>
                                <br>
                            </div>
                        </div>


                        <div class="tea" v-if="index===9" >
                            <div v-for="(tea,index) in tea_gao" @click="GoDetail">
                                <van-card
                                        :price="tea.prise"
                                        :desc="tea.desc"
                                        :title="tea.name"
                                        :thumb="tea.tea_img">
                                    <div slot="tags" class="tags">
                                        <van-tag plain type="danger">销量：{{tea.number}}</van-tag>
                                    </div>
                                </van-card>
                                <br>
                            </div>
                        </div>

                        <div class="tea" v-if="index===10" >
                            <div v-for="(tea,index) in tea_tools" @click="GoDetail">
                                <van-card
                                        :price="tea.prise"
                                        :desc="tea.desc"
                                        :title="tea.name"
                                        :thumb="tea.tea_img">
                                    <div slot="tags" class="tags">
                                        <van-tag plain type="danger">销量：{{tea.number}}</van-tag>
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
    import {brands,puer_tea,red_tea,green_tea,wul_tea,black_tea,white_tea,flowers_tea,tea_tools,tea_gao,tea_books} from '../datas.js'
    export default {
        name: 'category',
        components: {

        },
        data(){
            return{
                activeKey: "",
                vulue:"",
                brands_list: null,
                names:["品牌推荐","普洱茶","红茶","绿茶","乌龙茶","黑茶","白茶","花草茶","茶书","茶膏","茶具"],
                puer_tea:null,
                red_tea:null,
                green_tea:null,
                wul_tea:null,
                black_tea:null,
                white_tea:null,
                flowers_tea:null,
                tea_tools:null,
                tea_gao:null,
                tea_books:null

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
                this.$toast(`搜索了${item.brand_name}`);
            },
            GoDetail(){
                this.$router.push("/detail")
            }
        },
        created() {
            this.brands_list=brands.datas.brand_list;
            this.puer_tea=puer_tea;
            this.red_tea=red_tea;
            this.green_tea=green_tea;
            this.wul_tea=wul_tea;
             this.black_tea=black_tea;
             this.white_tea=white_tea;
             this.flowers_tea=flowers_tea;
             this.tea_books=tea_books;
             this.tea_gao=tea_gao;
             this.tea_tools=tea_tools;
            // console.log(this.brands_list);


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