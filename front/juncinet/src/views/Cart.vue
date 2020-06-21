<template>
    <div class="cart">
        <div class="header">
            <van-nav-bar
                    title="购物车"
                    @click-left="onClickLeft"
                    @click-right="onClickRight">
                <van-icon name="arrow-left" slot="left" color="#000000" size="20"></van-icon>
                <van-icon name="user-o" slot="right" color="#000000" size="20"></van-icon>
            </van-nav-bar>
            <img src="../assets/name.png">
        </div>

        <div v-for="(item,index) in $store.getters.getGoodList">
            <van-card
                      :num="item.num"
                      :title="item.name"
                      :price="item.price"
                      desc="精品好瓷"
                      :thumb="item.img"
            >
                <van-stepper @change="change(index,item.num)" v-model="item.num" slot="bottom" ></van-stepper>
            </van-card>
        </div>

        <div v-for="(item,index) in $store.getters.getGoodList">
            <van-button color="#7232dd" plain @click="removeit(index)">删除商品</van-button>
        </div>

        <div v-for="(item,index) in $store.getters.getGoodList">
            <van-submit-bar
                    :price="item.price*item.num*100"
                    button-text="提交订单"
                    @submit="onSubmit"
            >
                <van-checkbox v-model="checked">全选</van-checkbox>
                                <span slot="tip">
                                你的收货地址不支持同城送, <span @click="goMine">修改地址</span>
                                </span>
            </van-submit-bar>

        </div>

        <div class="footer" v-if="!islogin">
            <van-cell title="登录后享受更多优惠" value="去登录" @click="goLogin" ></van-cell>
        </div>


    </div>
</template>
<script>
    export	default{
        data(){
            return{
                islogin:localStorage.getItem("login"),
                checked:false,

            }
        },
        methods:{
            change(index,num){
                // console.log(num,index);
                this.$store.commit("ChangeGoodNum",[index,num]);

            },
            removeit(index){
                this.$store.commit("removeGood",index);
            },
            onClickLeft() {

                this.$router.go(-1);
            },
            onClickRight() {

                this.$router.push("/mine")
            },
            onSubmit(){
                this.$router.push("/order")
            },
            goLogin(){
                this.flag=false;
                this.$router.push("/login");
                // localStorage.setItem("login");
            },
            goMine(){
                this.$router.push("/mine")
            }
        },
        created() {

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
    .cart{
        width: 100%;
        .footer{
        display: block;
        margin-bottom: -30px;
        background-color: #adadad;
    }
    }


</style>