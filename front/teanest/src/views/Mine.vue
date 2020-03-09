<template>
    <div class="mine" >
        <div class="header">
                <van-nav-bar
                    title="我的页面"
                    right-text="登录"
                    @click-left="onClickLeft"
                    @click-right="onClickRight">
                <van-icon name="arrow-left" slot="left" color="#000000" size="20"></van-icon>
<!--                <van-icon name="ellipsis" slot="right" color="#000000" size="16" ></van-icon>-->
                </van-nav-bar>
<!--                <van-popup v-model="show"  round position="top" :style="{ height: '20%' }">-->
<!--                    扩展内容-->
<!--                </van-popup>-->
        </div>
            <div class="member-top">
                <div  v-if="!islogin">
                    <img src="//www.chawo.com/data/upload/shop/common/default_user_portrait.gif" alt="">
                    <p>未登录用户<span style="color:aquamarine;font-size: 10px">非会员</span></p>
                </div>

                <div  v-else>
                    <img src="../assets/headimg.png" alt="">
                    <p>茶友小白<span style="color:aquamarine;font-size: 10px">普通会员</span>
                        <van-button color="#ff0000" size="mini" @click="changeState">{{issign?"已签到":"签到"}}</van-button></p>
                </div>

            </div>



            <div class="member-collect">
                <van-tabs type="card" @click="onClick">
                    <van-tab title="商品收藏"></van-tab>
                    <van-tab title="店铺收藏"></van-tab>
                    <van-tab title="我的足迹"></van-tab>
                </van-tabs>
            </div>

        <div class="my_order">
            <div>
                <van-nav-bar
                        title="我的订单"
                        right-text="查看全部订单"
                >
<!--                    <van-icon name="arrow" slot="right"  color="#000000" size="20"></van-icon>-->
                    <van-icon name="balance-list-o" slot="left"  color="#1989fa" size="25"></van-icon>
                </van-nav-bar>
            </div>

            <div class="imgs">
                <van-grid :column-num="6" >

                    <van-grid-item
                            icon="paid"
                            text="待付款"
                    >
                    </van-grid-item>

                    <van-grid-item

                            icon="gift-card-o"
                            text="待收货"
                    >
                    </van-grid-item>

                    <van-grid-item

                            icon="logistics"
                            text="待自提"
                    >
                    </van-grid-item>

                    <van-grid-item

                            icon="edit"
                            text="待评价"
                    >
                    </van-grid-item>

                    <van-grid-item

                            icon="cash-back-record"
                            text="退款/退货"
                    >
                    </van-grid-item>
                    <van-grid-item
                            icon="points"
                            text="积分订单">
<!--                            url="http://www.chawo.com/wap/tmpl/product_list.html?xianshi=1"-->
                    </van-grid-item>

                </van-grid>
            </div>
        </div>

        <div class="my_money">
            <div>
                <van-nav-bar
                        title="我的财产"
                        right-text="查看全部财产"
                >
                    <!--                    <van-icon name="arrow" slot="right"  color="#000000" size="20"></van-icon>-->
                    <van-icon name="balance-o" slot="left"  color="#1989fa" size="25"></van-icon>
                </van-nav-bar>
            </div>

            <div class="imgs">
                <van-grid :column-num="3" >

                    <van-grid-item
                            icon="refund-o"
                            text="代金券" >
<!--                            to="/"-->

                    </van-grid-item>

                    <van-grid-item

                            icon="discount"
                            text="折扣券"
                    >
                    </van-grid-item>

                    <van-grid-item

                            icon="points"
                            text="积分"
                    >
                    </van-grid-item>
                </van-grid>
            </div>
        </div>
                <van-divider :style="{borderColor: '#f75c5c', padding: '0 5px',marginTop:'-5px' }"></van-divider>
        <div class="address" @click="address_show=!address_show">
            <van-nav-bar
                    title="收货地址管理"
            >
                <van-icon name="arrow" slot="right"  color="#000000" size="25"></van-icon>
                <van-icon name="location-o" slot="left"  color="#1989fa" size="25"></van-icon>
            </van-nav-bar>

            <div v-show="address_show">
                <van-address-list
                        v-model="chosenAddressId"
                        :list="list"
                        :disabled-list="disabledList"
                        disabled-text="以下地址超出配送范围"
                        default-tag-text="默认"
                        @add="onAdd"
                        @edit="onEdit"
                >
                </van-address-list>
            </div>

            <div class="addmore" v-show="showmore">
                <van-address-edit
                        :area-list="areaList"
                        show-postal
                        show-delete
                        show-set-default
                        show-search-result
                        :search-result="searchResult"
                        :area-columns-placeholder="['请选择', '请选择', '请选择']"
                        @save="onSave"
                        @delete="onDelete"
                        @change-detail="onChangeDetail"
                ></van-address-edit>
            </div>

        </div>

        <van-divider :style="{borderColor: '#f75c5c', padding: '0 5px' }"></van-divider>
        <div class="userset">
            <van-nav-bar
                    title="用户设置"
            >
                <van-icon name="arrow" slot="right"  color="#000000" size="25" @click="Gouserset"></van-icon>
                <van-icon name="setting-o" slot="left"  color="#1989fa" size="25"></van-icon>

            </van-nav-bar>

        </div>
        <van-divider :style="{borderColor: '#f75c5c', padding: '0 5px' }"></van-divider>
        <div class="loginout">
            <van-button type="primary" size="large" color="#7232dd" plain @click="loginout">注销账户</van-button>

        </div>


        <br><br><br><br><br>



    </div>

</template>

<script>
    export default {
        inject:['reload'],
        data(){
            return{
                islogin:localStorage.getItem("login"),
                show: false,
                showmore:false,
                issign:localStorage.getItem("sign"),
                showset:false,
                active: "",
                address_show:false,
                chosenAddressId: '1',
                areaList:{
                    province_list: {
                        110000: '北京市',
                        120000: '天津市'
                    },
                    city_list: {
                        110100: '北京市',
                        110200: '县',
                        120100: '天津市',
                        120200: '县'
                    },
                    // county_list: {
                    //     110101: '东城区',
                    //     110102: '西城区',
                    //     110105: '朝阳区',
                    //     110106: '丰台区'
                    //     120101: '和平区',
                    //     120102: '河东区',
                    //     120103: '河西区',
                    //     120104: '南开区',
                    //     120105: '河北区',
                    // }
                },
                searchResult: [],
                list: [
                    {
                        id: '1',
                        name: '张三',
                        tel: '13000000000',
                        address: '浙江省杭州市西湖区文三路 138 号东方通信大厦 7 楼 501 室'
                    },
                    {
                        id: '2',
                        name: '李四',
                        tel: '1310000000',
                        address: '浙江省杭州市拱墅区莫干山路 50 号'
                    }
                ],
                disabledList: [
                    {
                        id: '3',
                        name: '王五',
                        tel: '1320000000',
                        address: '浙江省杭州市滨江区江南大道 15 号'
                    }
                ]

            }

        },
        methods:{
            onClickLeft() {
                this.$router.go(-1);
            },
            onClickRight() {
                this.$router.push("/login");
            },
            changeState() {
                // this.islogin=true;
                localStorage.setItem("sign","true");
                this.reload();
                // this.$router.go(0);
                    // 页面刷新
                // location.reload()
                },
            onClick(title) {
                this.$toast("点击了",title);
            },
            onAdd() {
               this.showmore=!this.showmore;
                this.$toast("点击了新增地址");
            },

            onEdit(item, index) {
               this.$toast('编辑地址:' + index);
            },
            Gouserset(){
                this.$router.push("/userset")
            },
            loginout(){
                localStorage.removeItem("login");
                localStorage.removeItem("sign");
                this.$router.push("/login")
            },
            onSave() {
                Toast('save');
            },
            onDelete() {
                Toast('delete');
            },
            onChangeDetail(val) {
                if (val) {
                    this.searchResult = [{
                        name: '黄龙万科中心',
                        address: '杭州市西湖区'
                    }];
                } else {
                    this.searchResult = [];
                }
            },

         },
    }

</script>


<style scoped="scoped" lang="less">
    .member-top {
        background-color: #f75c5c;
        background-image: url(http://www.chawo.com/wap/images/member_top_bg.png);
        background-size: cover;
        text-align: center;
        width: 100%;
        height: 176px;


        img{
            /*display: block;*/
            width: 100px;
            border-radius: 50%;
            border: #f2f2f2 solid;
        }
        p{
            margin-top: -1px;
        }
    }
    .member-collect{
        margin-top: -30px;
    }
    .my_order{
        display: block;
        width: 100%;
        .imgs{
            margin-top: -15px;
        }

    }


</style>