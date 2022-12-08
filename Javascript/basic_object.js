// 物件 object
//key value

var person = {
    name:"小白",
    age:23,
    is_male:true,
    print_name:function(){
        document.write(this.name);    // this 指的是這個物件person

    }
};

document.write(person.name);
document.write("<br/>");

person.print_name();

var phrase = "hello";
document.write(phrase.length);      // 其實在js 每個變數都是物件 
document.write("<br/>");

// 真實世界的物件
var movie = {
    title:"刻在你心底的名字",
    maker:"氧氣電影",
    duration:114,
    actors:[
        {
            name:"陳旱森",
            age:24,
            sex:"male"
        },
        {
            name:"曾靖華",
            age:23,
            sex:"female"
        }
    ]
};

document.write(movie.title);
document.write("<br/>");

document.write(movie.actors[1].name);
document.write("<br/>");