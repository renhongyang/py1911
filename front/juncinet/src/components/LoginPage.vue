<template>
    <div class="login">
        <van-divider :style="{ color: '#343434', borderColor: '#000000', padding: '0 16px' }">
            合作账号登录
        </van-divider>
        <div id="qqLoginBtn">
            <a href="https://connect.qq.com/manage.html#/"><img src="../assets/qq.png" alt=""></a>
        </div>
        <van-divider :style="{ color: '#343434', borderColor: '#000000', padding: '0 16px' }">
            账号登录
        </van-divider>

<!--        <div class="phologin" v-show="phoshow">-->
<!--            <span style="font-size: 14px;color: #b3b3b3;line-height:50px">使用手机号和验证码登录！</span>-->
<!--            <van-cell-group>-->
<!--                <van-field-->
<!--                        v-model="phone"-->
<!--                        label="手机号"-->
<!--                        required-->
<!--                        clearable-->
<!--                        placeholder="请输入手机号"-->
<!--                >-->
<!--                </van-field>-->
<!--                <van-field-->
<!--                        v-model="sms"-->
<!--                        center-->
<!--                        required-->
<!--                        clearable-->
<!--                        label="短信验证码"-->
<!--                        placeholder="请输入短信验证码"-->
<!--                >-->
<!--                    <van-button slot="button" size="small" type="primary">发送验证码</van-button>-->
<!--                </van-field>-->
<!--            </van-cell-group>-->

<!--        </div>-->

<!--        <div class="norlogin" v-show="norshow">-->
<!--            <span style="font-size: 14px;color: #b3b3b3;line-height:50px">用户登录！</span>-->
<!--            <van-cell-group>-->
<!--                <van-field-->
<!--                        v-model="loginusername"-->
<!--                        required-->
<!--                        clearable-->
<!--                        label="用户名"-->
<!--                        placeholder="请输入用户名/已注册的手机号">-->
<!--                </van-field>-->

<!--                <van-field-->
<!--                        v-model="loginpassword"-->
<!--                        type="password"-->
<!--                        label="密码"-->
<!--                        placeholder="请输入登录密码"-->
<!--                        required>-->
<!--                </van-field>-->
<!--            </van-cell-group>-->
<!--        </div>-->

<!--        <div>-->
<!--            <div class="logbot">-->
<!--                <van-checkbox v-model="checked" checked-color="#07c160">保存密码30天</van-checkbox>-->
<!--                <van-button type="info" size="small" plain hairline  to="/forgotpwd">忘记密码</van-button>-->
<!--            </div>-->
<!--            <br>-->
<!--            <van-button round type="danger" size="large" @click="login">登录</van-button>-->
<!--            <br>-->
<!--            <br>-->
<!--            <van-button round type="danger" size="large" plain hairline to="/regist">注册</van-button>-->
<!--        </div>-->

    </div>
</template>

<script>
    export default {
        name: "LoginPage",
        data(){
        return{
            // loginusername:"",
            // loginpassword:"",
            // phone:"",
            // sms:"",
            // norshow:false,
            // phoshow:false,
            checked: false

        }
    },
        // methods:{
        //     GoQQ(){
        //     // this.$router.link("https://xui.ptlogin2.qq.com/cgi-bin/xlogin?appid=716027609&pt_3rd_aid=101175351&daid=383&pt_skey_valid=0&style=35&s_url=http%3A%2F%2Fconnect.qq.com&refer_cgi=authorize&which=&response_type=code&client_id=101175351&redirect_uri=https://www.chawo.com/data/resource/api/qq/return_url.php&state=apiaHR0cDovL3d3dy5jaGF3by5jb20vd2FwL3RtcGwvbWVtYmVyL21lbWJlci5odG1s&display=mobile&scope=get_user_info")
        //        this.$router.push("/")
        //         },

            // login(){
            //     if(this.loginusername<=0||this.loginpassword<=0||this.phone!==11||this.sms!==6||this.checked!==true){
            //         this.$toast("必填项不能为空！")
            //     }else {
            //         this.$toast("登陆成功！")
            //     }
            //
            // },
        // }
    }



</script>

<style scoped="scoped" lang="less">
    /*.logbot{*/
    /*    display: flex;*/
    /*    justify-content: space-around;*/
    /*}*/


</style>