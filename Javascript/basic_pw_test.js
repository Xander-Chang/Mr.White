// 密碼檢驗測試

var password = 123456;
var input;
var count = 0;
var limit = 3;
var out = false

while(password != input && !out){
    count ++;
    if(count<=limit){
        input = prompt("請輸入密碼");
    }
    else{
        out = true
    }
}

if(out){
    alert("超出輸入次數");
}    
else{
    alert("登入成功");
}








