import hashlib

from _datetime import datetime

from App.ext import db


# class Grade(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     g_name = db.Column(db.String(16))

class Home(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    img = db.Column(db.String(200))
    name = db.Column(db.String(32))
    trackid = db.Column(db.Integer, default=1)


    __abstract__ = True


class HomeWheel(Home):

    __tablename__ = "axf_wheel"


class Nav(Home):

    __tablename__ = "axf_nav"


class MustBuy(Home):

    __tablename__ = "axf_mustbuy"


class HomeShop(Home):

    __tablename__ = "axf_shop"


"""
trackid,name,img,categoryid,brandname,
img1,childcid1,productid1,longname1,price1,marketprice1,
img2,childcid2,productid2,longname2,price2,marketprice2,
img3,childcid3,productid3,longname3,price3,marketprice3,
"21782","零食大趴","http://img01.bqstatic.com//upload/activity/2017031018205492.jpg@90Q.jpg","103532","爱鲜蜂",
"http://img01.bqstatic.com/upload/goods/201/701/1916/20170119164159_996462.jpg@200w_200h_90Q","103533","118824","爱鲜蜂·特小凤西瓜1.5-2.5kg/粒","25.80","25.8",
"""


class MainShow(Home):
    categoryid = db.Column(db.Integer, default=1)
    brandname = db.Column(db.String(16))

    img1 = db.Column(db.String(200))
    childcid1 = db.Column(db.Integer, default=1)
    productid1 = db.Column(db.Integer, default=1)
    longname1 = db.Column(db.String(255))
    price1 = db.Column(db.Float, default=1)
    marketprice1 = db.Column(db.Float, default=1)

    img2 = db.Column(db.String(200))
    childcid2 = db.Column(db.Integer, default=1)
    productid2 = db.Column(db.Integer, default=1)
    longname2 = db.Column(db.String(255))
    price2 = db.Column(db.Float, default=1)
    marketprice2 = db.Column(db.Float, default=1)

    img3 = db.Column(db.String(200))
    childcid3 = db.Column(db.Integer, default=1)
    productid3 = db.Column(db.Integer, default=1)
    longname3 = db.Column(db.String(255))
    price3 = db.Column(db.Float, default=1)
    marketprice3 = db.Column(db.Float, default=1)


    __tablename__ = "axf_mainshow"


"""
闪购
typeid,typename,childtypenames,typesort
"""


class FoodType(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    typeid = db.Column(db.Integer, default=1)
    typename = db.Column(db.String(16))
    childtypenames = db.Column(db.String(200))
    typesort = db.Column(db.Integer, default=1)


    __tablename__ = "axf_foodtypes"


"""
axf_goods

productid,productimg,productname,productlongname,
isxf,pmdesc,specifics,price,marketprice,categoryid,
childcid,childcidname,dealerid,storenums,productnum,*******

"11951","http://img01.bqstatic.com/upload/goods/000/001/1951/0000011951_63930.jpg@200w_200h_90Q","","乐吧薯片鲜虾味50.0g",
0,0,"50g",2.00,2.500000,103541,
103543,"膨化食品","4858",200,4);
"""


class Good(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    productid = db.Column(db.Integer, default=1)
    productimg = db.Column(db.String(256))
    productname = db.Column(db.String(128))
    productlongname = db.Column(db.String(256))
    isxf = db.Column(db.BOOLEAN, default=False)
    pmdesc = db.Column(db.BOOLEAN, default=False)
    specifics = db.Column(db.String(32))
    price = db.Column(db.Float, default=1)
    marketprice = db.Column(db.Float, default=1)
    categoryid = db.Column(db.Integer, default=1)
    childcid = db.Column(db.Integer, default=1)
    childcidname = db.Column(db.String(128))
    dealerid = db.Column(db.Integer, default=1)
    storenums = db.Column(db.Integer, default=1)
    productnum = db.Column(db.Integer, default=1)

    __tablename__ = "axf_goods"


"""
用户表:
用户账号  
用户密码 
头像路径
用户等级
token值


购物车表：
用户id    商品id   数量   总价    是否选中    图片    长名字   属于哪个订单    isDelete


订单表：
订单id(唯一的)  用户id   进度  

"""


class UserModel(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    u_name = db.Column(db.String(32), unique=True)
    u_password = db.Column(db.String(128))
    u_email = db.Column(db.String(64), unique=True)
    u_icon = db.Column(db.String(255))  # *******************图片
    is_delete = db.Column(db.BOOLEAN, default=False)
    is_active = db.Column(db.BOOLEAN, default=False)

    __tablename__ = "axf_user"

    def set_password(self, password):
        self.u_password = self.generate_hash(password)

    def generate_hash(self, password):
        sha = hashlib.sha512()
        sha.update(password.encode("utf-8"))

        return sha.hexdigest()

    def check_password(self, password):
        return self.u_password == self.generate_hash(password)


# class CarModel(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     c_goods_num = db.Column(db.Integer, default=1)
#     c_goods_select = db.Column(db.BOOLEAN, default=True)
#     c_goods = db.Column(db.Integer, db.ForeignKey("good.id"))
#     c_user = db.Column(db.Integer, db.ForeignKey("usermodel.id"))
#
#
#     __tablename__ = "axf_cart"
#
#
# class OrderModel(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     o_user = db.Column(db.Integer, db.ForeignKey("usermodel.id"))
#     """
#     0  已下单   1 已下单,未付款   2 已下单,已付款,未收货
#
#     """
#     o_status = db.Column(db.Integer, default=1)
#
#     o_time = db.Column(db.DATETIME, index=True, default=datetime.utcnow)
#     o_price = db.Column(db.Float, default=0)
#
#     class Meta:
#         db_table = "axf_order"
#
#
# class OrderGoods(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     o_order_num = db.Column(db.Integer, db.ForeignKey("ordermodel.id"))
#     o_goods = db.Column(db.Integer, db.ForeignKey("good.id"))
#     o_goods_num = db.Column(db.Integer, default=1)
#
#
#     __tablename__ = "axf_ordergoods"
#
#





