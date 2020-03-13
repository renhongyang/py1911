<template>
    <div class="regist">
        <div class="header">
            <van-nav-bar
                    title="账号注册"
                    left-arrow
                    right-text="登录"
                    @click-left="onClickLeft"
                    @click-right="onClickRight">
                <van-icon name="wap-home-o" slot="left"  color="black" size="18px"></van-icon>
                <!--                <div class="header-img">-->
                <van-image
                        width="50px"
                        height="1.2rem"
                        src="http://www.chawo.com/wap/images/chawo-logo.png"
                        slot="left"
                >
                </van-image>
                <!--                </div>-->
            </van-nav-bar>
        </div>
        <van-divider :style="{ borderColor: 'black', border:2, marginTop:10}"></van-divider>

        <div class="phologin">
            <van-cell-group>
                <van-field
                        v-model="username"
                        required
                        clearable
                        label="用户名"
                        placeholder="请输入用户名">
                </van-field>
                <van-field
                        v-model="telephone"
                        label="手机号"
                        required
                        clearable
                        placeholder="请输入11位手机号"
                >
                </van-field>
                <van-field
                        v-model="sms"
                        required
                        clearable
                        label="验证码"
                        placeholder="请输入6位短信验证码">
                    <van-button slot="button" size="small" type="danger" plain hairline>发送验证码</van-button>-->
                </van-field>
                <van-field
                    v-model="password"
                    type="password"
                    label="密码"
                    placeholder="请输入密码"
                    required>
                  </van-field>
                <van-field
                        v-model="password1"
                        type="password"
                        label="密码"
                        placeholder="请再次输入密码"
                        required>
                </van-field>
            </van-cell-group>
            <br>
            <div class="logbot">
                <van-checkbox v-model="checked" checked-color="#07c160">同意</van-checkbox>
                <a href="http://www.chawo.com/wap/tmpl/member/document.html">用户注册协议</a>
            </div>
            <br>
            <van-button slot="button" size="large" type="danger" plain hairline @click="register">注册</van-button>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Regist",
        data(){
            return{
                username:"",
                password:"",
                password1:"",
                telephone:"",
                sms:"",
                checked: false

            }

        },
        methods: {
            onClickLeft() {
                this.$router.push("/");
            },
            onClickRight() {
                this.$router.push("/login/");
            },
            register() {
                if(this.username.length<=0||this.password.length<6||this.password1.length<6||this.password!==this.password1||this.telephone.length!==11||this.sms.length!==6||this.checked!==true){
                    this.$toast("必填项不能为空！或者输入有误！")
                }else {
                    // this.$toast("注册成功！");
                    this.$api.regist({
                        username:this.username,
                        password:this.password,
                        password1:this.password1,
                        telephone:this.telephone
                    }).then(res=>{
                        this.$router.push("/login/")
                    }).catch(err=>{
                        this.$toast("注册失败")
                    })
                }
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
    }
    .header-img{
        margin-right: 30px;

    }
    .logbot{
        display: flex;
        justify-content: center;
        a{
            color: #ffb400;
        }
    }

</style>
