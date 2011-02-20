var BrowserDetect={init:function(){this.browser=this.searchString(this.dataBrowser)||"An unknown browser";this.version=this.searchVersion(navigator.userAgent)||this.searchVersion(navigator.appVersion)||"an unknown version";this.OS=this.searchString(this.dataOS)||"an unknown OS";},searchString:function(data){for(var i=0;i<data.length;i++){var dataString=data[i].string;var dataProp=data[i].prop;this.versionSearchString=data[i].versionSearch||data[i].identity;if(dataString){if(dataString.indexOf(data[i].subString)!=-1)
return data[i].identity;}
else if(dataProp)
return data[i].identity;}},searchVersion:function(dataString){var index=dataString.indexOf(this.versionSearchString);if(index==-1)return;return parseFloat(dataString.substring(index+this.versionSearchString.length+1));},dataBrowser:[{string:navigator.userAgent,subString:"Chrome",identity:"Chrome"},{string:navigator.userAgent,subString:"OmniWeb",versionSearch:"OmniWeb/",identity:"OmniWeb"},{string:navigator.vendor,subString:"Apple",identity:"Safari",versionSearch:"Version"},{prop:window.opera,identity:"Opera"},{string:navigator.vendor,subString:"iCab",identity:"iCab"},{string:navigator.vendor,subString:"KDE",identity:"Konqueror"},{string:navigator.userAgent,subString:"Firefox",identity:"Firefox"},{string:navigator.vendor,subString:"Camino",identity:"Camino"},{string:navigator.userAgent,subString:"Netscape",identity:"Netscape"},{string:navigator.userAgent,subString:"MSIE",identity:"Explorer",versionSearch:"MSIE"},{string:navigator.userAgent,subString:"Gecko",identity:"Mozilla",versionSearch:"rv"},{string:navigator.userAgent,subString:"Mozilla",identity:"Netscape",versionSearch:"Mozilla"}],dataOS:[{string:navigator.platform,subString:"Win",identity:"Windows"},{string:navigator.platform,subString:"Mac",identity:"Mac"},{string:navigator.userAgent,subString:"iPhone",identity:"iPhone/iPod"},{string:navigator.userAgent,subString:"iPad",identity:"iPad"},{string:navigator.platform,subString:"Linux",identity:"Linux"}]};BrowserDetect.init();function createCookie(name,value,days){var expires;if(days){var date=new Date();date.setTime(date.getTime()+(days*24*60*60*1000));expires="; expires="+date.toGMTString();}
else expires="";document.cookie=name+"="+value+expires+"; path=/";}
function readCookie(name){var nameEQ=name+"=";var ca=document.cookie.split(';');for(var i=0;i<ca.length;i++){var c=ca[i];while(c.charAt(0)==' ')c=c.substring(1,c.length);if(c.indexOf(nameEQ)==0)return c.substring(nameEQ.length,c.length);}
return null;}
function eraseCookie(name){createCookie(name,"",-1);}
function areCookiesEnabled(){var r=false;createCookie("testing","Hello",1);if(readCookie("testing")!=null){r=true;eraseCookie("testing");}
return r;}
var swfobject=function(){var UNDEF="undefined",OBJECT="object",SHOCKWAVE_FLASH="Shockwave Flash",SHOCKWAVE_FLASH_AX="ShockwaveFlash.ShockwaveFlash",FLASH_MIME_TYPE="application/x-shockwave-flash",EXPRESS_INSTALL_ID="SWFObjectExprInst",ON_READY_STATE_CHANGE="onreadystatechange",win=window,doc=document,nav=navigator,plugin=false,domLoadFnArr=[main],regObjArr=[],objIdArr=[],listenersArr=[],storedAltContent,storedAltContentId,storedCallbackFn,storedCallbackObj,isDomLoaded=false,isExpressInstallActive=false,dynamicStylesheet,dynamicStylesheetMedia,autoHideShow=true,ua=function(){var w3cdom=typeof doc.getElementById!=UNDEF&&typeof doc.getElementsByTagName!=UNDEF&&typeof doc.createElement!=UNDEF,u=nav.userAgent.toLowerCase(),p=nav.platform.toLowerCase(),windows=p?/win/.test(p):/win/.test(u),mac=p?/mac/.test(p):/mac/.test(u),webkit=/webkit/.test(u)?parseFloat(u.replace(/^.*webkit\/(\d+(\.\d+)?).*$/,"$1")):false,ie=!+"\v1",playerVersion=[0,0,0],d=null;if(typeof nav.plugins!=UNDEF&&typeof nav.plugins[SHOCKWAVE_FLASH]==OBJECT){d=nav.plugins[SHOCKWAVE_FLASH].description;if(d&&!(typeof nav.mimeTypes!=UNDEF&&nav.mimeTypes[FLASH_MIME_TYPE]&&!nav.mimeTypes[FLASH_MIME_TYPE].enabledPlugin)){plugin=true;ie=false;d=d.replace(/^.*\s+(\S+\s+\S+$)/,"$1");playerVersion[0]=parseInt(d.replace(/^(.*)\..*$/,"$1"),10);playerVersion[1]=parseInt(d.replace(/^.*\.(.*)\s.*$/,"$1"),10);playerVersion[2]=/[a-zA-Z]/.test(d)?parseInt(d.replace(/^.*[a-zA-Z]+(.*)$/,"$1"),10):0;}}
else if(typeof win.ActiveXObject!=UNDEF){try{var a=new ActiveXObject(SHOCKWAVE_FLASH_AX);if(a){d=a.GetVariable("$version");if(d){ie=true;d=d.split(" ")[1].split(",");playerVersion=[parseInt(d[0],10),parseInt(d[1],10),parseInt(d[2],10)];}}}
catch(e){}}
return{w3:w3cdom,pv:playerVersion,wk:webkit,ie:ie,win:windows,mac:mac};}(),onDomLoad=function(){if(!ua.w3){return;}
if((typeof doc.readyState!=UNDEF&&doc.readyState=="complete")||(typeof doc.readyState==UNDEF&&(doc.getElementsByTagName("body")[0]||doc.body))){callDomLoadFunctions();}
if(!isDomLoaded){if(typeof doc.addEventListener!=UNDEF){doc.addEventListener("DOMContentLoaded",callDomLoadFunctions,false);}
if(ua.ie&&ua.win){doc.attachEvent(ON_READY_STATE_CHANGE,function(){if(doc.readyState=="complete"){doc.detachEvent(ON_READY_STATE_CHANGE,arguments.callee);callDomLoadFunctions();}});if(win==top){(function(){if(isDomLoaded){return;}
try{doc.documentElement.doScroll("left");}
catch(e){setTimeout(arguments.callee,0);return;}
callDomLoadFunctions();})();}}
if(ua.wk){(function(){if(isDomLoaded){return;}
if(!/loaded|complete/.test(doc.readyState)){setTimeout(arguments.callee,0);return;}
callDomLoadFunctions();})();}
addLoadEvent(callDomLoadFunctions);}}();function callDomLoadFunctions(){if(isDomLoaded){return;}
try{var t=doc.getElementsByTagName("body")[0].appendChild(createElement("span"));t.parentNode.removeChild(t);}
catch(e){return;}
isDomLoaded=true;var dl=domLoadFnArr.length;for(var i=0;i<dl;i++){domLoadFnArr[i]();}}
function addDomLoadEvent(fn){if(isDomLoaded){fn();}
else{domLoadFnArr[domLoadFnArr.length]=fn;}}
function addLoadEvent(fn){if(typeof win.addEventListener!=UNDEF){win.addEventListener("load",fn,false);}
else if(typeof doc.addEventListener!=UNDEF){doc.addEventListener("load",fn,false);}
else if(typeof win.attachEvent!=UNDEF){addListener(win,"onload",fn);}
else if(typeof win.onload=="function"){var fnOld=win.onload;win.onload=function(){fnOld();fn();};}
else{win.onload=fn;}}
function main(){if(plugin){testPlayerVersion();}
else{matchVersions();}}
function testPlayerVersion(){var b=doc.getElementsByTagName("body")[0];var o=createElement(OBJECT);o.setAttribute("type",FLASH_MIME_TYPE);var t=b.appendChild(o);if(t){var counter=0;(function(){if(typeof t.GetVariable!=UNDEF){var d=t.GetVariable("$version");if(d){d=d.split(" ")[1].split(",");ua.pv=[parseInt(d[0],10),parseInt(d[1],10),parseInt(d[2],10)];}}
else if(counter<10){counter++;setTimeout(arguments.callee,10);return;}
b.removeChild(o);t=null;matchVersions();})();}
else{matchVersions();}}
function matchVersions(){var rl=regObjArr.length;if(rl>0){for(var i=0;i<rl;i++){var id=regObjArr[i].id;var cb=regObjArr[i].callbackFn;var cbObj={success:false,id:id};if(ua.pv[0]>0){var obj=getElementById(id);if(obj){if(hasPlayerVersion(regObjArr[i].swfVersion)&&!(ua.wk&&ua.wk<312)){setVisibility(id,true);if(cb){cbObj.success=true;cbObj.ref=getObjectById(id);cb(cbObj);}}
else if(regObjArr[i].expressInstall&&canExpressInstall()){var att={};att.data=regObjArr[i].expressInstall;att.width=obj.getAttribute("width")||"0";att.height=obj.getAttribute("height")||"0";if(obj.getAttribute("class")){att.styleclass=obj.getAttribute("class");}
if(obj.getAttribute("align")){att.align=obj.getAttribute("align");}
var par={};var p=obj.getElementsByTagName("param");var pl=p.length;for(var j=0;j<pl;j++){if(p[j].getAttribute("name").toLowerCase()!="movie"){par[p[j].getAttribute("name")]=p[j].getAttribute("value");}}
showExpressInstall(att,par,id,cb);}
else{displayAltContent(obj);if(cb){cb(cbObj);}}}}
else{setVisibility(id,true);if(cb){var o=getObjectById(id);if(o&&typeof o.SetVariable!=UNDEF){cbObj.success=true;cbObj.ref=o;}
cb(cbObj);}}}}}
function getObjectById(objectIdStr){var r=null;var o=getElementById(objectIdStr);if(o&&o.nodeName=="OBJECT"){if(typeof o.SetVariable!=UNDEF){r=o;}
else{var n=o.getElementsByTagName(OBJECT)[0];if(n){r=n;}}}
return r;}
function canExpressInstall(){return!isExpressInstallActive&&hasPlayerVersion("6.0.65")&&(ua.win||ua.mac)&&!(ua.wk&&ua.wk<312);}
function showExpressInstall(att,par,replaceElemIdStr,callbackFn){isExpressInstallActive=true;storedCallbackFn=callbackFn||null;storedCallbackObj={success:false,id:replaceElemIdStr};var obj=getElementById(replaceElemIdStr);if(obj){if(obj.nodeName=="OBJECT"){storedAltContent=abstractAltContent(obj);storedAltContentId=null;}
else{storedAltContent=obj;storedAltContentId=replaceElemIdStr;}
att.id=EXPRESS_INSTALL_ID;if(typeof att.width==UNDEF||(!/%$/.test(att.width)&&parseInt(att.width,10)<310)){att.width="310";}
if(typeof att.height==UNDEF||(!/%$/.test(att.height)&&parseInt(att.height,10)<137)){att.height="137";}
doc.title=doc.title.slice(0,47)+" - Flash Player Installation";var pt=ua.ie&&ua.win?"ActiveX":"PlugIn",fv="MMredirectURL="+win.location.toString().replace(/&/g,"%26")+"&MMplayerType="+pt+"&MMdoctitle="+doc.title;if(typeof par.flashvars!=UNDEF){par.flashvars+="&"+fv;}
else{par.flashvars=fv;}
if(ua.ie&&ua.win&&obj.readyState!=4){var newObj=createElement("div");replaceElemIdStr+="SWFObjectNew";newObj.setAttribute("id",replaceElemIdStr);obj.parentNode.insertBefore(newObj,obj);obj.style.display="none";(function(){if(obj.readyState==4){obj.parentNode.removeChild(obj);}
else{setTimeout(arguments.callee,10);}})();}
createSWF(att,par,replaceElemIdStr);}}
function displayAltContent(obj){if(ua.ie&&ua.win&&obj.readyState!=4){var el=createElement("div");obj.parentNode.insertBefore(el,obj);el.parentNode.replaceChild(abstractAltContent(obj),el);obj.style.display="none";(function(){if(obj.readyState==4){obj.parentNode.removeChild(obj);}
else{setTimeout(arguments.callee,10);}})();}
else{obj.parentNode.replaceChild(abstractAltContent(obj),obj);}}
function abstractAltContent(obj){var ac=createElement("div");if(ua.win&&ua.ie){ac.innerHTML=obj.innerHTML;}
else{var nestedObj=obj.getElementsByTagName(OBJECT)[0];if(nestedObj){var c=nestedObj.childNodes;if(c){var cl=c.length;for(var i=0;i<cl;i++){if(!(c[i].nodeType==1&&c[i].nodeName=="PARAM")&&!(c[i].nodeType==8)){ac.appendChild(c[i].cloneNode(true));}}}}}
return ac;}
function createSWF(attObj,parObj,id){var r,el=getElementById(id);if(ua.wk&&ua.wk<312){return r;}
if(el){if(typeof attObj.id==UNDEF){attObj.id=id;}
if(ua.ie&&ua.win){var att="";for(var i in attObj){if(attObj[i]!=Object.prototype[i]){if(i.toLowerCase()=="data"){parObj.movie=attObj[i];}
else if(i.toLowerCase()=="styleclass"){att+=' class="'+attObj[i]+'"';}
else if(i.toLowerCase()!="classid"){att+=' '+i+'="'+attObj[i]+'"';}}}
var par="";for(var j in parObj){if(parObj[j]!=Object.prototype[j]){par+='<param name="'+j+'" value="'+parObj[j]+'" />';}}
el.outerHTML='<object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000"'+att+'>'+par+'</object>';objIdArr[objIdArr.length]=attObj.id;r=getElementById(attObj.id);}
else{var o=createElement(OBJECT);o.setAttribute("type",FLASH_MIME_TYPE);for(var m in attObj){if(attObj[m]!=Object.prototype[m]){if(m.toLowerCase()=="styleclass"){o.setAttribute("class",attObj[m]);}
else if(m.toLowerCase()!="classid"){o.setAttribute(m,attObj[m]);}}}
for(var n in parObj){if(parObj[n]!=Object.prototype[n]&&n.toLowerCase()!="movie"){createObjParam(o,n,parObj[n]);}}
el.parentNode.replaceChild(o,el);r=o;}}
return r;}
function createObjParam(el,pName,pValue){var p=createElement("param");p.setAttribute("name",pName);p.setAttribute("value",pValue);el.appendChild(p);}
function removeSWF(id){var obj=getElementById(id);if(obj&&obj.nodeName=="OBJECT"){if(ua.ie&&ua.win){obj.style.display="none";(function(){if(obj.readyState==4){removeObjectInIE(id);}
else{setTimeout(arguments.callee,10);}})();}
else{obj.parentNode.removeChild(obj);}}}
function removeObjectInIE(id){var obj=getElementById(id);if(obj){for(var i in obj){if(typeof obj[i]=="function"){obj[i]=null;}}
obj.parentNode.removeChild(obj);}}
function getElementById(id){var el=null;try{el=doc.getElementById(id);}
catch(e){}
return el;}
function createElement(el){return doc.createElement(el);}
function addListener(target,eventType,fn){target.attachEvent(eventType,fn);listenersArr[listenersArr.length]=[target,eventType,fn];}
function hasPlayerVersion(rv){var pv=ua.pv,v=rv.split(".");v[0]=parseInt(v[0],10);v[1]=parseInt(v[1],10)||0;v[2]=parseInt(v[2],10)||0;return(pv[0]>v[0]||(pv[0]==v[0]&&pv[1]>v[1])||(pv[0]==v[0]&&pv[1]==v[1]&&pv[2]>=v[2]))?true:false;}
function createCSS(sel,decl,media,newStyle){if(ua.ie&&ua.mac){return;}
var h=doc.getElementsByTagName("head")[0];if(!h){return;}
var m=(media&&typeof media=="string")?media:"screen";if(newStyle){dynamicStylesheet=null;dynamicStylesheetMedia=null;}
if(!dynamicStylesheet||dynamicStylesheetMedia!=m){var s=createElement("style");s.setAttribute("type","text/css");s.setAttribute("media",m);dynamicStylesheet=h.appendChild(s);if(ua.ie&&ua.win&&typeof doc.styleSheets!=UNDEF&&doc.styleSheets.length>0){dynamicStylesheet=doc.styleSheets[doc.styleSheets.length-1];}
dynamicStylesheetMedia=m;}
if(ua.ie&&ua.win){if(dynamicStylesheet&&typeof dynamicStylesheet.addRule==OBJECT){dynamicStylesheet.addRule(sel,decl);}}
else{if(dynamicStylesheet&&typeof doc.createTextNode!=UNDEF){dynamicStylesheet.appendChild(doc.createTextNode(sel+" {"+decl+"}"));}}}
function setVisibility(id,isVisible){if(!autoHideShow){return;}
var v=isVisible?"visible":"hidden";if(isDomLoaded&&getElementById(id)){getElementById(id).style.visibility=v;}
else{createCSS("#"+id,"visibility:"+v);}}
function urlEncodeIfNecessary(s){var regex=/[\\\"<>\.;]/;var hasBadChars=regex.exec(s)!=null;return hasBadChars&&typeof encodeURIComponent!=UNDEF?encodeURIComponent(s):s;}
var cleanup=function(){if(ua.ie&&ua.win){window.attachEvent("onunload",function(){var ll=listenersArr.length;for(var i=0;i<ll;i++){listenersArr[i][0].detachEvent(listenersArr[i][1],listenersArr[i][2]);}
var il=objIdArr.length;for(var j=0;j<il;j++){removeSWF(objIdArr[j]);}
for(var k in ua){ua[k]=null;}
ua=null;for(var l in swfobject){swfobject[l]=null;}
swfobject=null;});}}();return{registerObject:function(objectIdStr,swfVersionStr,xiSwfUrlStr,callbackFn){if(ua.w3&&objectIdStr&&swfVersionStr){var regObj={};regObj.id=objectIdStr;regObj.swfVersion=swfVersionStr;regObj.expressInstall=xiSwfUrlStr;regObj.callbackFn=callbackFn;regObjArr[regObjArr.length]=regObj;setVisibility(objectIdStr,false);}
else if(callbackFn){callbackFn({success:false,id:objectIdStr});}},getObjectById:function(objectIdStr){if(ua.w3){return getObjectById(objectIdStr);}},embedSWF:function(swfUrlStr,replaceElemIdStr,widthStr,heightStr,swfVersionStr,xiSwfUrlStr,flashvarsObj,parObj,attObj,callbackFn){var callbackObj={success:false,id:replaceElemIdStr};if(ua.w3&&!(ua.wk&&ua.wk<312)&&swfUrlStr&&replaceElemIdStr&&widthStr&&heightStr&&swfVersionStr){setVisibility(replaceElemIdStr,false);addDomLoadEvent(function(){widthStr+="";heightStr+="";var att={};if(attObj&&typeof attObj===OBJECT){for(var i in attObj){att[i]=attObj[i];}}
att.data=swfUrlStr;att.width=widthStr;att.height=heightStr;var par={};if(parObj&&typeof parObj===OBJECT){for(var j in parObj){par[j]=parObj[j];}}
if(flashvarsObj&&typeof flashvarsObj===OBJECT){for(var k in flashvarsObj){if(typeof par.flashvars!=UNDEF){par.flashvars+="&"+k+"="+flashvarsObj[k];}
else{par.flashvars=k+"="+flashvarsObj[k];}}}
if(hasPlayerVersion(swfVersionStr)){var obj=createSWF(att,par,replaceElemIdStr);if(att.id==replaceElemIdStr){setVisibility(replaceElemIdStr,true);}
callbackObj.success=true;callbackObj.ref=obj;}
else if(xiSwfUrlStr&&canExpressInstall()){att.data=xiSwfUrlStr;showExpressInstall(att,par,replaceElemIdStr,callbackFn);return;}
else{setVisibility(replaceElemIdStr,true);}
if(callbackFn){callbackFn(callbackObj);}});}
else if(callbackFn){callbackFn(callbackObj);}},switchOffAutoHideShow:function(){autoHideShow=false;},ua:ua,getFlashPlayerVersion:function(){return{major:ua.pv[0],minor:ua.pv[1],release:ua.pv[2]};},hasFlashPlayerVersion:hasPlayerVersion,createSWF:function(attObj,parObj,replaceElemIdStr){if(ua.w3){return createSWF(attObj,parObj,replaceElemIdStr);}
else{return undefined;}},showExpressInstall:function(att,par,replaceElemIdStr,callbackFn){if(ua.w3&&canExpressInstall()){showExpressInstall(att,par,replaceElemIdStr,callbackFn);}},removeSWF:function(objElemIdStr){if(ua.w3){removeSWF(objElemIdStr);}},createCSS:function(selStr,declStr,mediaStr,newStyleBoolean){if(ua.w3){createCSS(selStr,declStr,mediaStr,newStyleBoolean);}},addDomLoadEvent:addDomLoadEvent,addLoadEvent:addLoadEvent,getQueryParamValue:function(param){var q=doc.location.search||doc.location.hash;if(q){if(/\?/.test(q)){q=q.split("?")[1];}
if(param==null){return urlEncodeIfNecessary(q);}
var pairs=q.split("&");for(var i=0;i<pairs.length;i++){if(pairs[i].substring(0,pairs[i].indexOf("="))==param){return urlEncodeIfNecessary(pairs[i].substring((pairs[i].indexOf("=")+1)));}}}
return"";},expressInstallCallback:function(){if(isExpressInstallActive){var obj=getElementById(EXPRESS_INSTALL_ID);if(obj&&storedAltContent){obj.parentNode.replaceChild(storedAltContent,obj);if(storedAltContentId){setVisibility(storedAltContentId,true);if(ua.ie&&ua.win){storedAltContent.style.display="block";}}
if(storedCallbackFn){storedCallbackFn(storedCallbackObj);}}
isExpressInstallActive=false;}}};}();var HEMISPHERE_SOUTH='SOUTH';var HEMISPHERE_NORTH='NORTH';var HEMISPHERE_UNKNOWN='N/A';var olson={}
olson.timezones={'-720,0':new TimeZone('-12:00','Etc/GMT+12',false),'-660,0':new TimeZone('-11:00','Pacific/Pago_Pago',false),'-600,1':new TimeZone('-11:00','America/Adak',true),'-660,1,s':new TimeZone('-11:00','Pacific/Apia',true),'-600,0':new TimeZone('-10:00','Pacific/Honolulu',false),'-570,0':new TimeZone('-10:30','Pacific/Marquesas',false),'-540,0':new TimeZone('-09:00','Pacific/Gambier',false),'-540,1':new TimeZone('-09:00','America/Anchorage',true),'-480,1':new TimeZone('-08:00','America/Los_Angeles',true),'-480,0':new TimeZone('-08:00','Pacific/Pitcairn',false),'-420,0':new TimeZone('-07:00','America/Phoenix',false),'-420,1':new TimeZone('-07:00','America/Denver',true),'-360,0':new TimeZone('-06:00','America/Guatemala',false),'-360,1':new TimeZone('-06:00','America/Chicago',true),'-360,1,s':new TimeZone('-06:00','Pacific/Easter',true),'-300,0':new TimeZone('-05:00','America/Bogota',false),'-300,1':new TimeZone('-05:00','America/New_York',true),'-270,0':new TimeZone('-04:30','America/Caracas',false),'-240,1':new TimeZone('-04:00','America/Halifax',true),'-240,0':new TimeZone('-04:00','America/Santo_Domingo',false),'-240,1,s':new TimeZone('-04:00','America/Asuncion',true),'-210,1':new TimeZone('-03:30','America/St_Johns',true),'-180,1':new TimeZone('-03:00','America/Godthab',true),'-180,0':new TimeZone('-03:00','America/Argentina/Buenos_Aires,',false),'-180,1,s':new TimeZone('-03:00','America/Montevideo',true),'-120,0':new TimeZone('-02:00','America/Noronha',false),'-120,1':new TimeZone('-02:00','Etc/GMT+2',true),'-60,1':new TimeZone('-01:00','Atlantic/Azores',true),'-60,0':new TimeZone('-01:00','Atlantic/Cape_Verde',false),'0,0':new TimeZone('00:00','Africa/Casablanca',false),'0,1':new TimeZone('00:00','Europe/London',true),'60,1':new TimeZone('+01:00','Europe/Berlin',true),'60,0':new TimeZone('+01:00','Africa/Lagos',false),'60,1,s':new TimeZone('+01:00','Africa/Windhoek',true),'120,1':new TimeZone('+02:00','Asia/Beirut',true),'120,0':new TimeZone('+02:00','Africa/Johannesburg',false),'180,1':new TimeZone('+03:00','Europe/Moscow',true),'180,0':new TimeZone('+03:00','Asia/Baghdad',false),'210,1':new TimeZone('+03:30','Asia/Tehran',true),'240,0':new TimeZone('+04:00','Asia/Dubai',false),'240,1':new TimeZone('+04:00','Asia/Yerevan',true),'270,0':new TimeZone('+04:30','Asia/Kabul',false),'300,1':new TimeZone('+05:00','Asia/Yekaterinburg',true),'300,0':new TimeZone('+05:00','Asia/Karachi',false),'330,0':new TimeZone('+05:30','Asia/Kolkata',false),'345,0':new TimeZone('+05:45','Asia/Kathmandu',false),'360,0':new TimeZone('+06:00','Asia/Dhaka',false),'360,1':new TimeZone('+06:00','Asia/Omsk',true),'390,0':new TimeZone('+06:30','Asia/Rangoon',false),'420,1':new TimeZone('+07:00','Asia/Krasnoyarsk',true),'420,0':new TimeZone('+07:00','Asia/Jakarta',false),'480,0':new TimeZone('+08:00','Asia/Shanghai',false),'480,1':new TimeZone('+08:00','Asia/Irkutsk',true),'525,0':new TimeZone('+08:45','Australia/Eucla',true),'525,1,s':new TimeZone('+08:45','Australia/Eucla',true),'540,1':new TimeZone('+09:00','Asia/Yakutsk',true),'540,0':new TimeZone('+09:00','Asia/Tokyo',false),'570,0':new TimeZone('+09:30','Australia/Darwin',false),'570,1,s':new TimeZone('+09:30','Australia/Adelaide',true),'600,0':new TimeZone('+10:00','Australia/Brisbane',false),'600,1':new TimeZone('+10:00','Asia/Vladivostok',true),'600,1,s':new TimeZone('+10:00','Australia/Sydney',true),'630,1,s':new TimeZone('+10:30','Australia/Lord_Howe',true),'660,1':new TimeZone('+11:00','Asia/Kamchatka',true),'660,0':new TimeZone('+11:00','Pacific/Noumea',false),'690,0':new TimeZone('+11:30','Pacific/Norfolk',false),'720,1,s':new TimeZone('+12:00','Pacific/Auckland',true),'720,0':new TimeZone('+12:00','Pacific/Tarawa',false),'765,1,s':new TimeZone('+12:45','Pacific/Chatham',true),'780,0':new TimeZone('+13:00','Pacific/Tongatapu',false),'840,0':new TimeZone('+14:00','Pacific/Kiritimati',false)}
olson.dst_start_dates={'America/Denver':new Date(2011,2,13,3,0,0,0),'America/Mazatlan':new Date(2011,3,3,3,0,0,0),'America/Chicago':new Date(2011,2,13,3,0,0,0),'America/Mexico_City':new Date(2011,3,3,3,0,0,0),'Atlantic/Stanley':new Date(2011,8,4,7,0,0,0),'America/Asuncion':new Date(2011,9,2,3,0,0,0),'America/Santiago':new Date(2011,9,9,3,0,0,0),'America/Campo_Grande':new Date(2011,9,16,5,0,0,0),'America/Montevideo':new Date(2011,9,2,3,0,0,0),'America/Sao_Paolo':new Date(2011,9,16,5,0,0,0),'America/Los_Angeles':new Date(2011,2,13,8,0,0,0),'America/Santa_Isabel':new Date(2011,3,5,8,0,0,0),'America/Havana':new Date(2011,2,13,2,0,0,0),'America/New_York':new Date(2011,2,13,7,0,0,0),'Asia/Gaza':new Date(2011,2,26,23,0,0,0),'Asia/Beirut':new Date(2011,2,27,1,0,0,0),'Europe/Minsk':new Date(2011,2,27,3,0,0,0),'Europe/Istanbul':new Date(2011,2,27,7,0,0,0),'Asia/Damascus':new Date(2011,3,1,2,0,0,0),'Asia/Jerusalem':new Date(2011,3,1,6,0,0,0),'Africa/Cairo':new Date(2011,3,29,4,0,0,0),'Asia/Yerevan':new Date(2011,2,27,4,0,0,0),'Asia/Baku':new Date(2011,2,27,8,0,0,0),'Pacific/Auckland':new Date(2011,8,26,7,0,0,0),'Pacific/Fiji':new Date(2010,11,29,23,0,0,0),'America/Halifax':new Date(2011,2,13,6,0,0,0),'America/Goose_Bay':new Date(2011,2,13,2,1,0,0),'America/Miquelon':new Date(2011,2,13,5,0,0,0),'America/Godthab':new Date(2011,2,27,1,0,0,0)}
olson.ambiguity_list={'America/Denver':['America/Denver','America/Mazatlan'],'America/Chicago':['America/Chicago','America/Mexico_City'],'America/Asuncion':['Atlantic/Stanley','America/Asuncion','America/Santiago','America/Campo_Grande'],'America/Montevideo':['America/Montevideo','America/Sao_Paolo'],'Asia/Beirut':['Asia/Gaza','Asia/Beirut','Europe/Minsk','Europe/Istanbul','Asia/Damascus','Asia/Jerusalem','Africa/Cairo'],'Asia/Yerevan':['Asia/Yerevan','Asia/Baku'],'Pacific/Auckland':['Pacific/Auckland','Pacific/Fiji'],'America/Los_Angeles':['America/Los_Angeles','America/Santa_Isabel'],'America/New_York':['America/Havana','America/New_York'],'America/Halifax':['America/Goose_Bay','America/Halifax'],'America/Godthab':['America/Miquelon','America/Godthab']}
function TimeZone(offset,olson_tz,uses_dst){this.utc_offset=offset;this.olson_tz=olson_tz;this.uses_dst=uses_dst;}
TimeZone.prototype.display=function(){this.ambiguity_check();var response_text='<b>UTC-offset</b>: '+this.utc_offset+'<br/>';response_text+='<b>Olson database name</b>: '+this.olson_tz+'<br/>';response_text+='<b>Daylight Savings</b>: '+(this.uses_dst?'yes':'no')+'<br/>';return response_text;}
TimeZone.prototype.ambiguity_check=function(){var local_ambiguity_list=olson.ambiguity_list[this.olson_tz];if(typeof(local_ambiguity_list)=='undefined'){return;}
var length=local_ambiguity_list.length;for(var i=0;i<length;i++){var tz=local_ambiguity_list[i]
if(date_is_dst(olson.dst_start_dates[tz])){this.olson_tz=tz;return;}}}
function date_is_dst(date){var base_offset=((date.getMonth()>5?get_june_offset():get_january_offset()))
var date_offset=get_date_offset(date);return(base_offset-date_offset)!=0;}
function get_date_offset(date){return-date.getTimezoneOffset();}
function get_timezone_info(){var january_offset=get_january_offset();var june_offset=get_june_offset();var diff=january_offset-june_offset;if(diff<0){return{'utc_offset':january_offset,'dst':1,'hemisphere':HEMISPHERE_NORTH}}
else if(diff>0){return{'utc_offset':june_offset,'dst':1,'hemisphere':HEMISPHERE_SOUTH}}
return{'utc_offset':january_offset,'dst':0,'hemisphere':HEMISPHERE_UNKNOWN}}
function get_january_offset(){return get_date_offset(new Date(2011,0,1,0,0,0,0));}
function get_june_offset(){return get_date_offset(new Date(2011,5,1,0,0,0,0));}
function determine_timezone(){var timezone_key_info=get_timezone_info();var hemisphere_suffix=''
if(timezone_key_info.hemisphere==HEMISPHERE_SOUTH){hemisphere_suffix=',s';}
var tz_key=timezone_key_info.utc_offset+','+timezone_key_info.dst+hemisphere_suffix
return{'timezone':olson.timezones[tz_key],'key':tz_key}}
var LAnalytics={'init':function(base_url,key){LAnalytics.NODE=null;LAnalytics.CALLBACK_FUNC='LAnalytics.statResult';LAnalytics.isSecure=location.protocol=='https:'?true:false;LAnalytics.API_REQUEST_URL=(LAnalytics.isSecure?'https://':'http://')+base_url+'/api/analytics.json?';var windowWidth=self.innerWidth?self.innerWidth:(document.documentElement&&document.documentElement.clientWidth?document.documentElement.clientWidth:(document.body?document.body.clientWidth:0))
var windowHeight=self.innerHeight?self.innerHeight:(document.documentElement&&document.documentElement.clientHeight?document.documentElement.clientHeight:(document.body?document.body.clientWidth:0))
var timezone=determine_timezone().timezone;LAnalytics.config={'path':location.pathname,'browser':BrowserDetect.browser,'browser_version':BrowserDetect.version,'platform':BrowserDetect.OS,'screen_resolution':window.screen.width+'x'+window.screen.height,'window_dimensions':windowWidth+'x'+windowHeight,'enabled_cookie':areCookiesEnabled()?'1':'','flash':LAnalytics.haveFlashTrigger(),'have_java':navigator.javaEnabled(),'referrer':document.referrer,'time_zone':timezone.utc_offset,'key':key,'callback':LAnalytics.CALLBACK_FUNC};LAnalytics.stat(LAnalytics.config);},'haveFlashTrigger':function(){var flashVer=swfobject.getFlashPlayerVersion();if(flashVer&&flashVer.minor&&flashVer.major&&flashVer.release){return flashVer.major+'.'+flashVer.minor+'.'+flashVer.release;}
return'';},'buildReq':function(config){var pairs=[];for(var key in config){pairs.push(encodeURI(key)+'='+encodeURIComponent(config[key]));}
return pairs.join("&");},'stat':function(config){var headID=document.getElementsByTagName("head")[0];var scriptNode=document.createElement('script');if(LAnalytics.NODE){var oldNode=LAnalytics.NODE;oldNode.parentNode.removeChild(oldNode);}
scriptNode.type='text/javascript';scriptNode.src=LAnalytics.API_REQUEST_URL+LAnalytics.buildReq(config);headID.appendChild(scriptNode);LAnalytics.NODE=scriptNode;},'statResult':function(result){}}