function Left(str, n){
	if (n <= 0)
	    return "";
	else if (n > String(str).length)
	    return str;
	else
	    return String(str).substring(0,n);
}
function Right(str, n){
    if (n <= 0)
       return "";
    else if (n > String(str).length)
       return str;
    else {
       var iLen = String(str).length;
       return String(str).substring(iLen, iLen - n);
    }
}

var D = new Date();
var T = D.getTime();
//ZZ = (D.getFullYear()*100+D.getMonth()+1)*100+D.getDate();
YY = D.getFullYear();
MM = Right("0"+(D.getMonth()+1),2);
dd = Right("0"+D.getDate(),2);

hh = Right("0"+D.getHours(),2);
mm = Right("0"+D.getMinutes(),2);
ss = Right("0"+D.getSeconds(),2);

saida = YY+"-"+MM+"-"+dd+"_"+hh+"-"+mm+"-"+ss;
WScript.Echo( 'set YYYYMMDD='+ saida );

