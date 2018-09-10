var express = require('express');
var url=require('url');
var qs=require('querystring');//解析参数的库
var router = express.Router();
/* GET home page. */
router.get('/', function (req, res, next) {
    res.render('index', {title: 'Express'});
});

// 被爬虫服务器
router.get('/getCipherText', function (req, res, next) {
    var cipherText = "%3Cdiv%20class%3D%22info-item%22%3E%3Cspan%20class%3D%22label%22%3E%3Cspan%20class%3D%22required%22%3E*%3C%2Fspan%3E%E7%94%A8%E6%88%B7%E5%90%8D%EF%BC%9A%3C%2Fspan%3E%3Cinput%20name%3D%22userDTO.loginUserDTO.user_name%22%20style%3D%22display%3Anone%3B%22%20type%3D%22text%22value%3D%22gaoyahui101117%22%3E%20%20%20%20%3Cdiv%20class%3D%22con%22%3Egaoyahui101117%3C%2Fdiv%3E%20%20%20%20%3C%2Fdiv%3E%20%20%20%20%3Cdiv%20class%3D%22info-item%22%3E%3Cspan%20class%3D%22label%22%3E%3Cspan%20class%3D%22required%22%3E*%3C%2Fspan%3E%E5%A7%93%E5%90%8D%EF%BC%9A%3C%2Fspan%3E%3Cdiv%20class%3D%22con%22%3E%E9%AB%98%E4%BA%9A%E8%BE%89%3C%2Fdiv%3E%20%20%20%20%3C%2Fdiv%3E%20%20%20%20%3Cdiv%20class%3D%22info-item%22%3E%3Cspan%20class%3D%22label%22%3E%3Cspan%20class%3D%22required%22%3E*%3C%2Fspan%3E%E6%80%A7%E5%88%AB%EF%BC%9A%3C%2Fspan%3E%3Cdiv%20class%3D%22con%22%3E%3Cspan%20class%3D%22mr15%22%3E%3Cinput%20type%3D%22radio%22%20class%3D%22radio%22name%3D%22userDTO.sex_code%22%20value%3D%22M%22checked%3D%22checked%22%3E%3Clabel%3E%E7%94%B7%3C%2Flabel%3E%3C%2Fspan%3E%3Cspan%3E%3Cinput%20type%3D%22radio%22%20name%3D%22userDTO.sex_code%22%20value%3D%22F%22%20class%3D%22radio%22%3E%3Clabel%3E%E5%A5%B3%3C%2Flabel%3E%3C%2Fspan%3E%3C%2Fdiv%3E%3C%2Fdiv%3E%3Cdiv%20class%3D%22info-item%22%3E%3Cspan%20class%3D%22label%22%3E%E5%9B%BD%E5%AE%B6%2F%E5%9C%B0%E5%8C%BA%EF%BC%9A%3C%2Fspan%3E%3Cdiv%20class%3D%22con%22%3E%3Cspan%3E%3Cspan%3E%E4%B8%AD%E5%9B%BDCHINA%3C%2Fspan%3E%3C%2Fspan%3E%3Cinput%20type%3D%22hidden%22%20name%3D%22userDTO.country_code%22%20value%3D%22CN%22%3E%20%20%20%20%3C%2Fdiv%3E%20%20%20%20%3C%2Fdiv%3E%20%20%20%20%3Cdiv%20class%3D%22info-item%22%3E%3Cspan%20class%3D%22label%22%3E%3Cspan%20class%3D%22required%22%3E*%3C%2Fspan%3E%E8%AF%81%E4%BB%B6%E7%B1%BB%E5%9E%8B%EF%BC%9A%3C%2Fspan%3E%3Cdiv%20class%3D%22con%22%3E%E4%BA%8C%E4%BB%A3%E8%BA%AB%E4%BB%BD%E8%AF%81%3C%2Fdiv%3E%20%20%20%20%3C%2Fdiv%3E%20%20%20%20%3Cdiv%20class%3D%22info-item%22%3E%3Cspan%20class%3D%22label%22%3E%3Cspan%20class%3D%22required%22%3E*%3C%2Fspan%3E%E8%AF%81%E4%BB%B6%E5%8F%B7%E7%A0%81%EF%BC%9A%3C%2Fspan%3E%3Cdiv%20class%3D%22con%22%3E412724199301066432%3C%2Fdiv%3E%20%20%20%20%3C%2Fdiv%3E%20%20%20%20%3Cdiv%20class%3D%22info-item%22%3E%3Cspan%20class%3D%22label%22%3E%E5%87%BA%E7%94%9F%E6%97%A5%E6%9C%9F%EF%BC%9A%3C%2Fspan%3E%3Cdiv%20class%3D%22con%22%3E%3Cinput%20type%3D%22text%22%20readonly%3D%22readonly%22%20value%3D%221993-01-06%22%20id%3D%22born_date%22name%3D%22userDTO.born_date%22%20class%3D%22inptxt%20w200%20color333%22%3E%20%20%20%20%3C%2Fdiv%3E%20%20%20%20%3C%2Fdiv%3E%20%20%20%20%3Cdiv%20class%3D%22info-item%22%3E%3Cspan%20class%3D%22label%22%3E%E6%A0%B8%E9%AA%8C%E7%8A%B6%E6%80%81%EF%BC%9A%3C%2Fspan%3E%3Cdiv%3E%3Cdiv%20class%3D%22con%22%20style%3D%22color%3A%230077FF%3B%22%20title%3D%22%22%3E%E5%B7%B2%E9%80%9A%E8%BF%87%3C%2Fdiv%3E%20%20%20%20%3C%2Fdiv%3E%20%20%20%20%3C!--%20%3Cdiv%20%20style%3D%22color%3A%23FF7F00%22%20th%3Atext%3D%22%24%7Bnotice1%7D%22%3E%E6%B5%8B%E8%AF%95%3C%2Fdiv%3E%20--%3E%20%20%20%20%3C%2Fdiv%3E%20%20%20%20%3Cdiv%20class%3D%22info-item%22%3E%3Cspan%20class%3D%22label%22%3E%3Cspan%20class%3D%22required%22%3E*%3C%2Fspan%3E%E7%99%BB%E5%BD%95%E5%AF%86%E7%A0%81%EF%BC%9A%3C%2Fspan%3E%3Cdiv%20class%3D%22con%22%3E%3Cinput%20type%3D%22password%22%20value%3D%22%22%20name%3D%22userDTO.password%22%20maxlength%3D%2225%22class%3D%22inptxt%20w200%20color333%22%3E%20%20%20%20%3C%2Fdiv%3E%20%20%20%20%3Cdiv%20class%3D%22tips%20one-line%22%3E%E6%AD%A3%E7%A1%AE%E8%BE%93%E5%85%A5%E5%AF%86%E7%A0%81%E6%89%8D%E8%83%BD%E4%BF%AE%E6%94%B9%E4%B8%AA%E4%BA%BA%E8%B5%84%E6%96%99%3C%2Fdiv%3E%20%20%20%20%3C%2Fdiv%3E";

    res.send({cipherText: cipherText});
});

// 爬虫服务器模拟爬虫时调用服务器进行解密
router.get('/decCipherText', function (req, res, next) {
    var cipherText = req.query.cipherText
    console.log("--->"+cipherText);
    var plainText = decodeURIComponent(cipherText);
    console.log("--->"+plainText);
    res.send({plainText: plainText});
});

module.exports = router;
