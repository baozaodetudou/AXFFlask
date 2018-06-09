from django.conf.urls import url

from Axf import views

urlpatterns = [
    url(r"^home/", views.home, name="home"),
    url(r"^market/", views.market, name="market"),
    url(r"^marketwithparams/(?P<categoryid>\d+)/(?P<childcid>\d+)/(?P<order_ruler>\d+)/", views.market_with_parmas, name="market_with_parmas"),
    url(r"^cart/", views.cart, name="cart"),
    url(r"^mine/", views.mine, name="mine"),
    url(r"^userregister/", views.user_register, name="user_register"),
    url(r"^userlogout/", views.log_out, name="log_out"),
    url(r"^checkuser/", views.check_user, name="check_out"),
    url(r"^checkemail/", views.check_email, name="check_email"),
    url(r"^userlogin/", views.user_login, name="user_login"),
    url(r"^addtocart/", views.add_to_cart, name="add_to_cart"),
    url(r"^deltocart/", views.del_to_cart, name="del_to_cart"),
    url(r"^cartadd/", views.car_add, name="car_add"),
    url(r"^cartdel/", views.car_del, name="car_del"),
    url(r"^changecartstatus", views.change_cart_status, name="change_cart_status"),
    url(r"^changecartsstatus", views.change_carts_status, name="chang_carts_status"),
    url(r"^makeorder/", views.make_order, name="make_order"),
    url(r"^alipay/", views.alipay, name="alipay"),
    url(r"^roderpay/", views.order_pay, name="order_pay"),

    url(r"^orderinfo/", views.order_info, name="order_info"),
   

#     邮箱配置
    url(r"^activeuser/", views.active_user, name="active_user")



]



