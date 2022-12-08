// class
/*
var phone1 = {
    number:"123",
    year:2020,
    is_waterproof:false,
    phone_age:function(){
        return 2021-this.year
    }
}

var phone2 = {
    number:"456",
    year:2018,
    is_waterproof:false,
    phone_age:function(){
        return 2021-this.year
    }
}

var phone3 = {
    number:"789",
    year:2018,
    is_waterproof:true,
    phone_age:function(){
        return 2021-this.year
    }
}
*/                      

class Phone{                                             // 物件有共通點  寫成class
    constructor(number,year,is_waterproof){
        this.number = number;
        this.year = year;
        this.is_waterproof = is_waterproof;
    }
    phone_age(){
        return 2021 - this.year;
    }
};

var phone1 = new Phone("123", 2020, false);              //創建 新手機 的物件
document.write(phone1.number, "<br/>");
document.write(phone1.year, "<br/>");
document.write(phone1.is_waterproof, "<br/>");

var phone2 = new Phone("456",2018, false);
document.write(phone2.number, "<br/>");
document.write(phone2.year, "<br/>");
document.write(phone2.is_waterproof, "<br/>");

