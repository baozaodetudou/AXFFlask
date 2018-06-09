from flask import Blueprint, render_template

from App.ext import db
from App.models import HomeWheel, Nav, MustBuy, HomeShop, MainShow

blue = Blueprint("first_blue", __name__)





def init_blue(app):

    app.register_blueprint(blueprint=blue)


ALL_TYPE = "0"
"""
排序规则
0   综合排序
1   价格升序
2   价格降序
"""
ORDER_TOTLA = "0"
PRICE_ASC = "1"
PRICE_DSC = "2"

@blue.route("/home/")
def home():
    title = "首页"

    wheels = HomeWheel.query.all()

    navlist = Nav.query.all()

    mustbuyList = MustBuy.query.all()

    shops = HomeShop.query.all()
    shop0_1 = shops[0:1]
    shop1_3 = shops[1:3]
    shop3_7 = shops[3:7]
    shop7_11 = shops[7:11]

    mainshows = MainShow.query.all()

    data = {
        "wheels": wheels,
        "navList": navlist,
        "mustbuyList": mustbuyList,
        "shop0_1": shop0_1,
        "shop1_3": shop1_3,
        "shop3_7": shop3_7,
        "shop7_11": shop7_11,
        "mainshows": mainshows,
        "title": title,

    }
    # return render_template("home/home.html", data=data)
    return "55555"


# def market(request):
#     return redirect(reverse("axf:market_with_parmas", kwargs={"categoryid": 104749, "childcid": 0, "order_ruler": 0}))
#
#
# def market_with_parmas(request, categoryid, childcid, order_ruler):
#     title = "闪购"
#     foodtypes = FoodType.objects.all()
#     # 判断分类类型
#     if childcid == ALL_TYPE:
#         foods = Food.objects.filter(categoryid=categoryid)
#     else:
#         foods = Food.objects.filter(categoryid=categoryid).filter(childcid=childcid)
#
#     # 排序
#     if order_ruler == ORDER_TOTLA:
#         pass
#     elif order_ruler == PRICE_ASC:
#         foods = foods.order_by("price")
#     elif order_ruler == PRICE_DSC:
#         foods = foods.order_by("-price")
#
#     try:
#         userid = request.session.get("user_id")
#         cartmodels = CarModel.objects.filter(c_user_id=userid)
#
#         tmp = []
#         for food in foods:
#             for cartmodel in cartmodels:
#                 if cartmodel.c_goods_id == food.id:
#                     food.view = cartmodel.c_goods_num
#
#         # for food in foods:
#         #     print(food.view)
#
#     except BaseException as e:
#         print(e)
#
#
#     finally:
#
#         try:
#             foodtps = FoodType.objects.get(typeid=categoryid)
#             childtypenames = foodtps.childtypenames
#             childtypenames_list = childtypenames.split("#")
#             child_type_list = []
#             for childtypename in childtypenames_list:
#                 child_type_list.append(childtypename.split(":"))
#
#             data = {
#                 "foodtypes": foodtypes,
#                 "foods": foods,
#                 "categoryid": int(categoryid),
#                 "child_type_list": child_type_list,
#                 "childcid": childcid,
#                 "order_ruler": order_ruler,
#                 "title": title,
#             }
#
#             return render(request, "market/market.html", context=data)
#         except BaseException as e:
#
#             print(e)
#
#             return redirect(reverse("axf:market"))
#
#
# def cart(request):
#     userid = request.session.get("user_id")
#
#     try:
#         user = UserModel.objects.get(pk=userid)
#
#         cartmodels = user.carmodel_set.all()
#         is_all_select = True
#
#         for cartmodel in cartmodels:
#             if not cartmodel.c_goods_select:
#                 is_all_select = False
#                 break
#
#         title = "购物车"
#         data = {
#             "title": title,
#             "cartmodels": cartmodels,
#             "is_all_select": is_all_select,
#             "total_price": total_price(userid),
#         }
#         return render(request, "cart/cart.html", context=data)
#     except BaseException as e:
#
#         print(e)
#
#         return redirect(reverse("axf:user_login"))
#
#
# def mine(request):
#     title = "我的"
#
#     is_login = False
#
#     data = {
#         "title": title,
#         "is_login": is_login
#     }
#
#     try:
#         userid = request.session.get("user_id")
#
#         # data = {
#         #     "title": "用户注册",
#         #     "is_login": is_login,
#         # }
#
#         if userid:
#             user = UserModel.objects.get(pk=userid)
#
#             data["is_login"] = True
#             data["user_icon"] = "/static/upload/" + user.u_icon.url
#             data["user_name"] = user.u_name
#
#             ordered_count = OrderModel.objects.filter(o_user=user).filter(o_status=order_status.ORDERED).count()
#             if ordered_count > 0:
#                 data["order_count"] = ordered_count
#             wait_count = OrderModel.objects.filter(o_user=user).filter(o_status=order_status.PAYED).count()
#             print(wait_count)
#             if ordered_count > 0:
#                 data["wait_count"] = wait_count
#
#         return render(request, "mine/mine.html", context=data)
#     except BaseException as e:
#         return render(request, "mine/mine.html", context=data)
#
#
# def user_register(request):
#     if request.method == "GET":
#         is_login = False
#
#         data = {
#             "title": "用户注册",
#             "is_login": is_login,
#         }
#
#         return render(request, "user/user_register.html", context=data)
#
#     if request.method == "POST":
#         username = request.POST.get("u_name")
#         password = request.POST.get("u_password")
#         useremail = request.POST.get("u_email")
#         userfile = request.FILES.get("u_icon")
#
#         user = UserModel()
#         user.u_name = username
#         user.u_email = useremail
#         user.u_icon = userfile
#         user.set_password(password)
#
#         user.save()
#         request.session["user_id"] = user.id
#
#         userid = str(user.id)
#         email = user.u_email
#
#         send_email(username, email, userid)
#
#         return redirect(reverse("axf:mine"))
#
#
# def log_out(request):
#     request.session.flush()
#     return redirect(reverse("axf:mine"))
#
#
# def check_user(request):
#     username = request.GET.get("u_name")
#     users = UserModel.objects.filter(u_name=username)
#
#     data = {
#         "stats": 200,
#         "msg": "ok",
#     }
#
#     if users.exists():
#         data["stats"] = "801"
#         data["msg"] = "该用户名已被占用"
#     else:
#         data["msg"] = "该用户可用"
#
#     return JsonResponse(data)
#
#
# def check_email(request):
#     useremail = request.GET.get("useremail")
#     # print("zoudaole ***************")
#     users = UserModel.objects.filter(u_email=useremail)
#
#     data = {
#         "status": 200,
#         "msg": "ok",
#     }
#
#     if users.exists():
#         data["status"] = "801"
#         data["msg"] = "该邮箱不可用"
#     else:
#         data["msg"] = "该邮箱可用"
#
#     return JsonResponse(data)
#
#
# def user_login(request):
#     if request.method == "GET":
#
#         msg = request.session.get("user_msg")
#         if not msg:
#             msg = "请您登录"
#         data = {
#             "title": "用户登录",
#             "msg": msg,
#         }
#         return render(request, "user/user_login.html", context=data)
#     elif request.method == "POST":
#         user_name = request.POST.get("u_name")
#         user_password = request.POST.get("u_password")
#         # print(user_name)
#
#         try:
#             u_name_indata = UserModel.objects.get(u_name=user_name)
#
#             if u_name_indata.check_password(user_password):
#
#                 if not u_name_indata.is_active:
#                     request.session["user_msg"] = "用户未激活"
#                 else:
#                     request.session["user_id"] = u_name_indata.id
#                     return redirect(reverse("axf:mine"))
#             else:
#                 request.session["user_msg"] = "密码错误"
#
#             return redirect(reverse("axf:user_login"))
#
#         except BaseException as e:
#
#             request.session["user_msg"] = "用户不存在"
#             print(e)
#             return redirect(reverse("axf:user_login"))
#
#
# def send_email(username, email, userid):
#     subject = "python test"
#     message = "do you remember me?"
#
#     token = str(uuid.uuid4())
#     # 用户加密
#     cache.set(token, userid, 60 * 60)
#
#     recipient_list = [email]
#
#     temp = loader.get_template("user/user_active.html")
#
#     data = {
#         "username": username,
#         "active_url": "http://127.0.0.1:8003/axf/activeuser/?token=" + token,
#     }
#
#     temp_data = temp.render(data)
#
#     send_mail(subject, message, "15664477239@163.com", recipient_list, html_message=temp_data)
#
#     return HttpResponse("邮件发送成功%s" % subject)
#
#
# def active_user(request):
#     u_token = request.GET.get("token")
#
#     user_id = cache.get(u_token)
#     cache.delete(u_token)
#     try:
#         user = UserModel.objects.get(pk=user_id)
#
#         user.is_active = True
#         user.save()
#
#         return HttpResponse("用户激活成功")
#     except BaseException as e:
#
#         print(e)
#
#         return HttpResponse("该用户未注册")
#
#
# def add_to_cart(request):
#     goodsid = request.GET.get("goodsid")
#
#     userid = request.session.get("user_id")
#
#     data = {
#         "status": "200",
#         "msg": "ok,"
#
#     }
#
#     if not userid:
#         data["status"] = "302"
#         data["msg"] = "not login"
#     else:
#         # 数据添加
#         cartmodels = CarModel.objects.filter(c_goods_id=goodsid).filter(c_user_id=userid)
#         if cartmodels.exists():
#             cartmodel = cartmodels.first()
#
#             cartmodel.c_goods_num = cartmodel.c_goods_num + 1
#             cartmodel.save()
#         else:
#             cartmodel = CarModel()
#
#             cartmodel.c_goods = Food.objects.filter(pk=goodsid).first()
#
#             cartmodel.c_user = UserModel.objects.filter(pk=userid).first()
#             # 这一句报错  模型  设置成图片格式了
#             cartmodel.save()
#
#         data["goods_num"] = cartmodel.c_goods_num
#
#     return JsonResponse(data)
#
#
# def del_to_cart(request):
#     goodsid = request.GET.get("goodsid")
#
#     userid = request.session.get("user_id")
#
#     data = {
#         "status": "200",
#         "msg": "ok",
#         "goods_num": 0,
#
#     }
#
#     if not userid:
#         data["status"] = "302"
#         data["msg"] = "not login"
#     else:
#         # 数据添加
#         cartmodels = CarModel.objects.filter(c_goods_id=goodsid).filter(c_user_id=userid)
#         if cartmodels.exists():
#             cartmodel = cartmodels.first()
#             if cartmodel.c_goods_num >= 1:
#
#                 cartmodel.c_goods_num = cartmodel.c_goods_num - 1
#                 cartmodel.save()
#             else:
#                 cartmodel.delete()
#
#             # else:
#             #     cartmodel = CarModel()
#             #
#             #     cartmodel.c_goods = Food.objects.filter(pk=goodsid).first()
#             #
#             #     cartmodel.c_user = UserModel.objects.filter(pk=userid).first()
#             #     # 这一句报错  模型  设置成图片格式了
#             #     cartmodel.save()
#
#             data["goods_num"] = cartmodel.c_goods_num
#
#     return JsonResponse(data)
#
#
# def car_add(request):
#     cartid = request.GET.get("cartid")
#
#     try:
#         cart_model = CarModel.objects.get(pk=cartid)
#         userid = request.session.get("user_id")
#
#         data = {
#             "status": "200",
#             "msg": "ok",
#             "total_price": total_price(userid)
#         }
#
#         cart_model.c_goods_num = cart_model.c_goods_num + 1
#         cart_model.save()
#
#         data["goods_num"] = cart_model.c_goods_num
#
#         return JsonResponse(data)
#     except BaseException as e:
#         print(e)
#
#         data = {
#             "status": "202",  # not find cart*********代码可追加
#         }
#
#         return JsonResponse(data)
#
#
# def car_del(request):
#     cartid = request.GET.get("cartid")
#
#     try:
#
#         cart_model = CarModel.objects.get(pk=cartid)  # **********同上********
#
#         userid = request.session.get("user_id")
#
#         data = {
#             "status": "200",
#             "msg": "ok",
#             "total_price": total_price(userid),
#         }
#
#         if cart_model.c_goods_num == 1:
#             cart_model.delete()
#             data["goods_num"] = 0
#         else:
#             cart_model.c_goods_num = cart_model.c_goods_num - 1
#             cart_model.save()
#
#             data["goods_num"] = cart_model.c_goods_num
#
#         return JsonResponse(data)
#     except BaseException as e:
#         print(e)
#         data = {
#             "status": "200",
#         }
#         return JsonResponse(data)
#
#
# def change_cart_status(request):
#     cartid = request.GET.get("cartid")
#
#     try:
#         cartmodel = CarModel.objects.get(pk=cartid)
#         cartmodel.c_goods_select = not cartmodel.c_goods_select
#         cartmodel.save()
#
#         is_all_select = True
#
#         userid = request.session.get("user_id")
#
#         cartmodels = CarModel.objects.filter(c_user_id=userid).filter(c_goods_select=False)
#
#         if cartmodels.exists():
#             is_all_select = False
#
#         data = {
#             "status": "200",
#             "msg": "ok",
#             "is_select": cartmodel.c_goods_select,
#             "is_all_select": is_all_select,
#             "total_price": total_price(userid)
#         }
#
#         return JsonResponse(data)
#
#     except BaseException as e:
#         print(e)
#         return redirect(reverse("axf:home"))
#
#
# def change_carts_status(request):
#     carts = request.GET.get("carts")
#     car_list = carts.split("#")
#
#     select = request.GET.get('select')
#
#     if select == "true":
#         is_select = True
#     else:
#         is_select = False
#
#     try:
#         for cart in car_list:
#             cartmodel = CarModel.objects.get(pk=cart)
#             cartmodel.c_goods_select = is_select
#             cartmodel.save()
#
#         userid = request.session.get("user_id")
#
#         data = {
#             "msg": "ok",
#             "status": "200",
#             "total_price": total_price(userid),
#
#         }
#
#         return JsonResponse(data)
#     except BaseException as e:
#         print(e)
#         data = {
#             "status": "202",  # 查找购物车出错
#         }
#         return JsonResponse(data)
#
#
# # 总价
# def total_price(userid):
#     cartmodels = CarModel.objects.filter(c_user_id=userid).filter(c_goods_select=True)
#
#     total = 0
#     for cartmodel in cartmodels:
#         total += cartmodel.c_goods_num * cartmodel.c_goods.price
#
#     return "{:.2f}".format(total)
#
#
# # 生成订单
# def make_order(request):
#     carts = request.GET.get("carts")
#     cart_list = carts.split("#")
#
#     userid = request.session.get("user_id")
#
#     try:
#         user = UserModel.objects.get(pk=userid)
#
#         # 生成订单
#         order = OrderModel()
#         order.o_user = user
#         order.o_price = total_price(userid)
#
#         order.save()
#
#         for cartid in cart_list:
#             # 拿出购物车的数据
#             cartmodel = CarModel.objects.get(pk=cartid)
#             # 将数据导入
#             ordergoods = OrderGoods()
#             ordergoods.o_order_num = order
#             ordergoods.o_goods = cartmodel.c_goods
#             ordergoods.o_goods_num = cartmodel.c_goods_num
#             # 订单保存
#             ordergoods.save()
#             cartmodel.delete()
#
#         data = {
#             "status": "200",
#             "msg": "ok",
#             "orderid": order.id,
#         }
#
#         return JsonResponse(data)
#     except BaseException as e:
#
#         print(e)
#         request.session.flush()
#
#         return redirect(reverse("axf:user_login"))
#
#
# def order_info(request):
#     orderid = request.GET.get("order_id")
#
#     try:
#
#         order = OrderModel.objects.get(pk=orderid)
#
#         # ordergoods = OrderGoods.objects.get(o_order_num=order)
#
#         data = {
#             "order": order,
#             # "ordergoods": ordergoods,
#         }
#
#         return render(request, "order/orderinfo.html", context=data)
#     except BaseException as e:
#         print(e)
#
#         return redirect(reverse("axf:cart"))
#
#
# def alipay(request):
#     orderid = request.GET.get("orderid")
#
#     try:
#
#         order = OrderModel.objects.get(pk=orderid)
#         order.o_status = order_status.PAYED
#         order.save()
#
#         data = {
#             "status": "200",
#         }
#
#         return JsonResponse(data)
#     except BaseException as e:
#         print(e)
#
#         data = {
#             "status": "202",
#         }
#
#         return JsonResponse(data)
#
#
# def order_pay(request):
#     status = request.GET.get("status")
#     userid = request.session.get("user_id")
#
#     if not userid:
#         return redirect(reverse("axf:user_login"))
#
#     if status:
#         orders = OrderModel.objects.filter(o_user_id=userid).filter(o_status=status)
#     else:
#         orders = OrderModel.objects.filter(o_user_id=userid)
#
#     data = {
#         "orders": orders,
#     }
#     if status == "0":
#         return render(request, "order/orderlist.html", context=data)
#     elif status == "1":
#         return render(request, "order/orderlist_pay.html", context=data)

