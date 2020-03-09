<template>
    <div class="login">
        <div class="header">
            <van-nav-bar
                    title="登录"
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
        <van-divider :style="{ borderColor: 'black', border:2, marginTop:10}"></van-divider>

        <div class="center">
            <van-tabs v-model="active">
                <van-tab>
                    <div slot="title" >
                        <van-icon name="phone-circle-o" color="#ff0000" size="18px"/>手机登录
                    </div>
                    <div class="phologin">
                        <span style="font-size: 14px;color: #b3b3b3;line-height:50px">使用手机号和验证码登录！</span>
                        <van-cell-group>
                            <van-field
                                    v-model="phone"
                                    label="手机号"
                                    required
                                    clearable
                                    placeholder="请输入11位手机号"
                            >
                            </van-field>
                            <van-field
                                    v-model="sms"
                                    center
                                    required
                                    clearable
                                    label="短信验证码"
                                    placeholder="请输入6位短信验证码"
                            >
                                <van-button slot="button" size="small" type="primary">发送验证码</van-button>
                            </van-field>
                        </van-cell-group>
                    </div>
                    <LoginPage></LoginPage>
                    <div>
                        <div class="logbot">
                            <van-checkbox v-model="checked" checked-color="#07c160">保存密码30天</van-checkbox>
                            <van-button type="info" size="small" plain hairline  to="/forgotpwd">忘记密码</van-button>
                        </div>
                        <br>
                        <van-button round type="danger" size="large" @click="login_phone">登录</van-button>
                        <br>
                        <br>
                        <van-button round type="danger" size="large" plain hairline to="/regist">注册</van-button>
                    </div>
                </van-tab>

                <van-tab>
                    <div slot="title">
                        <van-icon name="user-circle-o" color="#ff0000" size="18px"/>普通登录
                    </div>
                    <div class="norlogin">
                        <span style="font-size: 14px;color: #b3b3b3;line-height:50px">用户登录！</span>
                        <van-cell-group>
                            <van-field
                                    v-model="loginusername"
                                    required
                                    clearable
                                    label="用户名"
                                    placeholder="请输入用户名/已注册的手机号">
                            </van-field>

                            <van-field
                                    v-model="loginpassword"
                                    type="password"
                                    label="密码"
                                    placeholder="请输入登录密码"
                                    required>
                            </van-field>
                        </van-cell-group>
                    </div>
                    <LoginPage></LoginPage>
                    <div>
                        <div class="logbot">
                            <van-checkbox v-model="checked" checked-color="#07c160">保存密码30天</van-checkbox>
                            <van-button type="info" size="small" plain hairline  to="/forgotpwd">忘记密码</van-button>
                        </div>
                        <br>
                        <van-button round type="danger" size="large" @click="login_normal">登录</van-button>
                        <br>
                        <br>
                        <van-button round type="danger" size="large" plain hairline to="/regist">注册</van-button>
                    </div>
                </van-tab>
            </van-tabs>
        </div>
    </div>

</template>

<script>
    import LoginPage from '@/components/LoginPage.vue'
    export default {
        name: "Mine",
        components:{
            LoginPage
        },
        data(){
            return{
                active: 2,
                phone:"",
                sms:"",
                loginusername:"",
                loginpassword:"",
                checked:false,
                // islogin:localStorage.setItem("login")

            }
        },
        methods: {
            onClickLeft() {
                this.$router.push("/");
                // this.$toast('返回首页');
            },
            login_phone(){
                if(this.phone.length!==11||this.sms.length!==6||this.checked!==true){
                    this.$toast("必填项不能为空！或者输入有误")
                }else {
                    localStorage.setItem("login",true);
                    // if(this.$route.query.t){
                    //     this.$router.push(this.$route.query.t);
                    // }
                    this.$toast("登陆成功！");
                    this.$router.push("/mine");
                }

            },
            login_normal(){
                if(this.loginusername.length<=0||this.loginpassword.length<=6||this.checked!==true){
                    this.$toast("必填项不能为空！或者输入有误，请重新输入！")
                }else {
                    localStorage.setItem("login",true);
                    // if(this.$route.query.t){
                    //     this.$router.push(this.$route.query.t);
                    // }

                    this.$toast("登陆成功！");
                    this.$router.push("/mine");

                }

            },

        },
        params:['flag']

    }
</script>

<style scoped="scoped" lang="less">
    .header{
        width: 100%;
        height:30px;
        background-color:beige;
    }
    .logbot{
        display: flex;
        justify-content: space-around;
    }

</style>