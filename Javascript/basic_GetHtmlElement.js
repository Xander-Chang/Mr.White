// 如何取得 html 元素
// window 是全域物件  因此沒有必要寫出來
window.document.write("跟 document.write 一樣 <br/>");

var a = 123;
window.document.write(window.a, "<br/>");


var h1 = document.getElementById("header");
// console.log(h1);
h1.innerText = "Xander";
h1.style.backgroundColor = "red";
h1.style.color = "blue";

var link = document.getElementById("link");
console.log(link)
link.href = "https://amazon.com";
link.innerText = "Amazon";



