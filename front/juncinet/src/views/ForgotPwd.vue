<template>
    <div class="forgetpwd">
        <div class="header">
            <van-nav-bar
                    title="找回密码"
                    left-arrow
                    right-text="登录"
                    @click-left="onClickLeft"
                    @click-right="onClickRight">
                <van-icon name="wap-home-o" slot="left"  color="black" size="18px"></van-icon>
<!--                <div class="header-img">-->
            </van-nav-bar>
            <img src="../assets/name.png">
        </div>
        <van-divider :style="{ borderColor: 'black', border:2, marginTop:10}"></van-divider>

        <div class="phologin">
            <van-cell-group>
                <van-field
                        v-model="phone"
                        label="手机号"
                        required
                        clearable
                        placeholder="请输入手机号"
                >
                </van-field>
                <van-field
                        v-model="sms"
                        required
                        clearable
                        label="验证码"
                        placeholder="请输入下图验证码"
                >
                </van-field>
            </van-cell-group>
                <p>
                    <van-image
                            width="100px"
                            height="2rem"
                            src="http://www.chawo.com/mobile/index.php?act=seccode&op=makecode&k=3186f3bbe30c7dbc1b9316f10f8bb888&t=0.7773955887630102"
                            slot="right"
                    >
                    </van-image>
                </p>
            <br>
            <van-button slot="button" size="large" type="danger" plain hairline>请求接收短信验证码</van-button>
            <p style="font-size: 14px;color: #b3b3b3;line-height:50px">请填写已绑定发手机号！</p>
        </div>
    </div>
</template>

<script>
    export default {
        name: "ForgotPwd",
        data(){
            return{
                phone:"",
                sms:""

            }

        },
        methods: {
            onClickLeft() {
                this.$router.push("/");
            },
            onClickRight() {
                this.$router.push("/login");
            },
        }
    }
</script>

<style scoped="scoped" lang="less">
    .header{
        line-height: 30px;
        width: 100%;
        height:30px;
        background-color:beige;
        img{
            z-index: 5 ;
            width: 50px;
            position: absolute;
            top: 15px;
            left: 50px;
        }
    }
    .header-img{
        margin-right: 30px;

    }

</style>
