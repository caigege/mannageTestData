//定义全局变量函数
var localStorage = window.localStorage;
//定义全局变量u
//设置缓存
function set(key, value) {
    var v = value;
    //是对象转成JSON，不是直接作为值存入内存
    if (typeof v == 'object') {
        v = JSON.stringify(v);
        v = 'obj-' + v;
    } else {
        v = 'str-' + v;
    }
    var localStorage = window.localStorage;
    if (localStorage) {
        localStorage.setItem(key, v);
    }
};

//获取缓存
function get(key) {
    var localStorage = window.localStorage;
    if (localStorage)
        var v = localStorage.getItem(key);
    if (!v) {
        return;
    }
    if (v.indexOf('obj-') === 0) {
        v = v.slice(4);
        return JSON.parse(v);
    } else if (v.indexOf('str-') === 0) {
        return v.slice(4);
    }
};