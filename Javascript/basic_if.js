// if 判斷式

//範例1
//如果肚子餓,我就去吃飯
var hungry = true;
if(hungry){
    document.write("範例1:我就去吃飯");
};
document.write("<br/>");

//範例2
//如果 今天下雨 我就開車去上班
//否則 我就走路去上班
var rain = true;
if(rain){
    document.write("範例2 開車去上班");
}else{
    document.write("範例2 走路去上班");
};
document.write("<br/>");

/*
範例3
如果 你考一百分
    我給你1000元
或是如果 你考80分以上
    我給你500元
或是如果 你考86分以上
    我給你300元
否則 
    你給我 300元
*/
var score = 100;
if (score == 100){
    document.write("範例3 我給你1000元");
}else if (score >= 80){
    document.write("範例3 我給你500元");
}else if (score >= 60){
    document.write("範例3 我給你300元");
}else {
    document.write("範例3 你給我300元");
};
document.write("<br/>");

/*
範例4
如果 你考一百分 且 今天下雨
    我給你1000元

否則 
    你給我 100元
*/
var score = 100;
var rain = true;
if (score== 100 && rain){
    document.write("範例4 我給你1000元");
}else{
    document.write("範例4 你給我300元");
};
document.write("<br/>");

/*
範例5
如果 你考一百分 或 今天下雨
    我給你1000元

否則 
    你給我 100元
*/
var score = 10;
var rain = false;
if (score== 100 || rain){
    document.write("範例4 我給你1000元");
}else{
    document.write("範例4 你給我300元");
};
document.write("<br/>");

/*
範例6
如果 你考一百分 或 今天沒有下雨
    我給你1000元

否則 
    你給我 100元
*/
var score = 10;
var rain = false;
if (score== 100 || !rain){
    document.write("範例4 我給你1000元");
}else{
    document.write("範例4 你給我300元");
};
document.write("<br/>");


/*
練習
設定一個函數 max_num
可以傳入三個數字
判斷哪一個是最大的
*/
var num1 = prompt("請輸入第一個數字");
var num2 = prompt("請輸入第二個數字");
var num3 = prompt("請輸入第三個數字");

function max_num(num1, num2, num3){
    if(num1>num2 && num1>num3){
        document.write(num1, "是最大的");
    }else if (num2>num1 && num2>num3){
        document.write(num2, "是最大的");
    }else{
        document.write(num3, "是最大的")
    }
}

max_num(num1, num2, num3);
document.write("<br/>");

