function BTN_Color() {
    if (document.getElementById('Input_1').value !== '' && document.getElementById('Input_2').value !== '') {
        document.getElementById('Button_1').style.backgroundColor = '#0195f7';
        document.getElementById('Button_1').style.cursor = 'pointer';
    } else {
        document.getElementById('Button_1').style.backgroundColor = '#4cb5f9';
    }
}

// --------------------------------------------------------------------------------------

setTimeout(function () {
    $('#First').fadeOut('fast');
}, 2000);

// --------------------------------------------------------------------------------------