let donates = document.querySelectorAll('.show-donate');

$.each(donates, function (index, element) {
    element.addEventListener('click', () => {
        $('.donate-popup').removeClass('none');
        console.log(element.value)
        $('.title').val(element.value)
    })
})

$('.close-popup').click(function () {
    $('.donate-popup').addClass('none');
})

let mode = document.querySelectorAll('#mode');

function loadMode() {
    $('.mode1').css("display", "grid");
}

loadMode()

$.each(mode, function (index, element) {
    element.addEventListener('click', () => {
        if (element.value == "mode1") {
            $('.mode1').css("display", "grid");
            $('.mode2').css("display", "none");
            $('.mode3').css("display", "none");
        }

        if (element.value == "mode2") {
            $('.mode1').css("display", "none");
            $('.mode2').css("display", "grid");
            $('.mode3').css("display", "none");
        }

        if (element.value == "mode3") {
            $('.mode1').css("display", "none");
            $('.mode2').css("display", "none");
            $('.mode3').css("display", "grid");
        }
    })
})

$('.nextGcash').click(function () {
    $('.gcash-img').css("display", "grid");
    $('.gcash').css("display", "none");

    $('.donate-popup h4').css("display", "none");
    $('.mode').css("display", "none");

    $('.donate-popup h1').css("display", "none");
})

$('.close').click(function () {
    window.location.reload();
})