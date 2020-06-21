<template>
    <div class="order">
        <div class="header">
            <van-nav-bar
                    title="确认订单"
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
            <van-button color="#7232dd" plain @click="removeit(index)">删除订单</van-button>
        </div>

        <div v-for="(item,index) in $store.getters.getGoodList">
            <van-submit-bar
                    :price="item.price*item.num*100"
                    button-text="确认支付"
                    @submit="onSubmit"
            >
                <van-checkbox v-model="checked">全选</van-checkbox>
            </van-submit-bar>

        </div>
    </div>
</template>

<script>
    export default {
        name: "Order",
        methods:{
            onClickLeft() {

                this.$router.go(-1);
            },
            onClickRight() {

                this.$router.push("/mine")
            },
            onSubmit(){
                this.$toast("确认支付")
            },
            removeit(index){
                this.$store.commit("removeGood",index);
            },
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

</style>