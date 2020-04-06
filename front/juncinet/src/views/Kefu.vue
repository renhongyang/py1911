<template>
    <div class="kefu">
        <div class="header">
            <van-nav-bar
                    title="联系客服"
                    @click-left="onClickLeft"
                    @click-right="onClickRight">
                <van-icon name="arrow-left" slot="left" color="#000000" size="20"></van-icon>
                <van-icon name="more-o" slot="right" color="#000000" size="20"></van-icon>
            </van-nav-bar>
            <img src="../assets/name.png">
        </div>

        <div class="con">
            <h1>这里是客服中心</h1>
            <div class="contact">
                <div class="mt10">电话: <a href="tel:087166666655">0123-6666 6655</a></div>
                <div class="mt10">客服微信: 123456</div>
                <div class="mt10">客服QQ: 4001234567</div>
                <div class="mt10"><img src="../assets/timg.jpg" class="qrcode"></div>
            </div>

        </div>

    </div>
</template>

<script>
    export default {
        name: "Kefu",

        methods:{
            onClickLeft() {
                this.$router.go(-1);
            },
            onClickRight() {
                this.$router.push("/mine");
            },
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