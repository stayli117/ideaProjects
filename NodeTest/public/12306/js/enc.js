// document.querySelector('#decodeBtn').addEventListener('click', decode);

function decode() {
    $.get('/getCipherText', function (resp) {
        var cipherText = resp.cipherText;
        var plainText = decodeURIComponent(cipherText);
        document.querySelector('#basic_info_base').innerHTML = plainText;
    });
}

decode()

