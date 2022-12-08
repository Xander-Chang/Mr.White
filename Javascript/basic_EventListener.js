// Event Listener


// 方法一   寫函式在html 裡面
/*
function handle_click(element){
    //alert("叫你按就按啊?");
    console.log(element);
    element.innerText = "按屁啊!";
    element.style.color = "red";
}
*/


//方法二 
var btn = document.getElementById("btn");
btn.addEventListener("click", function(){
    //alert("叫你按就按啊?");
    this.innerText = "按屁啊!";
    this.style.color = "red";

});

// 查看滑鼠是否滑過圖片
var img = document.getElementById("img");

img.addEventListener("mouseover", function(){   //滑鼠滑入 mouseover
    this.src = "新馬辣.jfif";
});

img.addEventListener("mouseout", function(){   //滑鼠滑出 mouseout
    this.src = "馬辣.jpg";
});
