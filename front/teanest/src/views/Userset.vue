<template>
    <div class="userset">
        <div class="header">
            <van-nav-bar
                    title="用户设置"
                    left-arrow
                    @click-left="onClickLeft">
                <van-icon name="wap-home-o" slot="left"  color="black" size="18px"></van-icon>

                <van-image class="header-img"
                           width="50px"
                           height="1rem"
                           src="http://www.chawo.com/wap/images/chawo-logo.png"
                           slot="right"
                >
                </van-image>
            </van-nav-bar>
        </div>
        <div class="con">
            <van-collapse v-model="activeNames">
                <van-collapse-item title="修改用户昵称" name="1">修改用户昵称</van-collapse-item>
                <van-collapse-item title="修改登陆密码" name="2">修改登陆密码</van-collapse-item>
                <van-collapse-item title="修改绑定手机号" name="3">修改绑定手机号</van-collapse-item>
            </van-collapse>

        </div>
    </div>
</template>

<script>
    export default {
        name: "Userset",
        data(){
            return{
                activeNames: ['1'],

            }

        },methods:{
            onClickLeft() {
                this.$router.push("/");

            },
        }
    }
</script>

<style scoped="scoped" lang="less">
    .header{
        width: 100%;
        height:30px;
        background-color:beige;
    }

</style>