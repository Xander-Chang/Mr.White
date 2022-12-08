// while 迴圈

var i = 1;

while(i <= 3){
    document.write(i);
    document.write("<br/>");
    i++;                    // i = i+1
};

document.write("<br/>");

do{
    document.write(i);
    document.write("<br/>");
    i++;                    // 上面迴圈的最後是3 這裡又+1
}while(i <= 3)              // 變成 4 , 不符合條件結束迴圈


