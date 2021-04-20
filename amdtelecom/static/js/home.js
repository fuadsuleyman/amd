console.log('home.js -->');
// function changeDisplaySearchBtn() {

    let searchInput = document.querySelector('.mobile-search--body')
    let inputJqWidth = $('.mobile-search--body')
    let inputVal = $('#search-filter-value')
    let responseArea = document.getElementById('search-filter-body');
    let responseJqArea = $('#search-filter-body')
    let searchBtnIcon = document.getElementById('search-btn-icon')

    let witdInput = getComputedStyle(searchInput)
    let widthStyle = witdInput.width
    let width = parseInt(widthStyle.split('p')[0])


    $(window).resize(function(e) { // 991px den yuxari oldugu zaman input hissesi acilir
        /* Do shit */
        console.log(e.target.innerWidth);
        if (e.target.innerWidth > 991) {
            // responseJqArea.css('display', 'block')
            if (inputVal.value.length != 0) {
                responseJqArea.css('display', 'block')
            }
            else {
                responseJqArea.css('display', 'none')
            }
        }
        else {
            responseJqArea.css('display', 'none')
            inputVal.val('')
        }
    });

    document.querySelector("body").addEventListener("click", function(e){
        
        console.log(e.target.getAttribute("class"));
        if (e.target.getAttribute("class") == 'data-title' || e.target.getAttribute("class") == 'image-attr' || e.target.getAttribute('class') == 'mobile-search--body--input'){
            responseJqArea.css('display', 'block')
        }
        else {
            responseJqArea.css('display', 'none')
        }
    })

function changeDisplay(widthSearch) { // for resize search body
    if (widthSearch == 36) {
        inputJqWidth.addClass('w-200')
        responseArea.classList.remove('d-none')
        responseArea.classList.remove('d-block')

    }
    else {
        inputJqWidth.removeClass('w-200')
        responseArea.classList.add('d-none')
        responseArea.classList.remove('d-block')
        inputVal.val('')
    }
}
// changeDisplay(width)
// }

searchBtnIcon.addEventListener('click', (e)=>{
    console.log('salam');
    // e.preventDefault()
    let widthStyle = witdInput.width
    let width = parseInt(widthStyle.split('p')[0])

    changeDisplay(width)
})



// changeDisplaySearchBtn()