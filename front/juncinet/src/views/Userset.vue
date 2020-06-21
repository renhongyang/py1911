<template>
    <div class="userset">
        <div class="header">
            <van-nav-bar
                    title="用户设置"
                    left-arrow
                    @click-left="onClickLeft">
                <van-icon name="wap-home-o" slot="left"  color="black" size="18px"></van-icon>

            </van-nav-bar>
            <img src="../assets/name.png">
        </div>

        <div class="con" v-if="userinfo">
            <h2>修改信息</h2>
            <van-collapse v-model="activeNames">
                <van-collapse-item title="修改用户名" name="1">
                    <van-field v-model="userinfo.username" type="tel" label="用户名:" />
                </van-collapse-item>
                <van-collapse-item title="修改登陆密码" name="2">
                    <van-field v-model="userinfo.password" type="password" label="密码:" />
                </van-collapse-item>
                <van-collapse-item title="修改绑定手机号" name="3">
                    <van-field v-model="userinfo.telephone" type="tel" label="手机号:" />
                </van-collapse-item>

                <van-collapse-item title="修改邮箱号" name="4">
                    <van-field v-model="userinfo.email" type="email" label="邮箱:" />
                </van-collapse-item>

            </van-collapse>
            <van-button @click="modify" round block type="info" native-type="submit">
            修改信息
            </van-button>
        </div>

    </div>

</template>

<script>
    export default{
        name: "Userset",
        data(){
            return{
                activeNames: ['1'],
                userinfo:null,
            }
        },
        methods:{
            modify(){
                // console.log("++");
                this.$api.modifyUserInfo({
                    userinfo:this.userinfo
                }).then(res=>{
                    console.log("更改成功",res);
                    this.$toast("更改成功")
                }).catch(err=>{
                    console.log("更改出错",err);
                })
            },
            onClickLeft() {
                this.$router.push("/");
            }
        },
        created() {
            this.$api.getUserinfo().then(res=>{
                console.log("个人信息",res);
                this.userinfo=res.data;
                this.$jsCookie.set("userinfo",res.data)
            }).catch(err=>{
                console.log("出错了");
            })
        },


    }
</script>

<style scoped="scoped" lang="less">
    .header{
        width: 100%;
        height:30px;
        background-color:beige;
        img{
            z-index: 5 ;
            width: 50px;
            position: absolute;
            top: 15px;
            right: 50px;
        }
    }

</style>