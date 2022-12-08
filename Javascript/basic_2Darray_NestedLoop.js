// 2維陣列 

var number = [
    [1,2,3],
    [4,5,6]
    ,[7,8,9]
    ,[0]
];

document.write(number[0][0]);
document.write("<br/>");


//巢狀迴圈
for(var i =0; i <4; i++){
    for(var j=0; j<3; j++){
        document.write("i:"+i+"j:"+j);
        document.write("<br/>");
    }
};


//練習
for(var i=0;i<number.length; i++){                 // i小於 number[i]的長度
    for(var j=0; j<number[i].length; j++){         // j 小於number[i][j]的長度
        document.write(number[i][j]);
    }
    document.write("<br/>")
}


