let linkUrl = `http://localhost:8000/`

$(document).on('input', '#search-filter-btn', function() { // price range when changed keep values(min,max)
    // $('#slider_value').html( $(this).val() );
    value = $(this).val()
    var newUrl = linkUrl
    getSearchData(newUrl)
    // $.ajax({
    //     url: `${domain}api/v1.0/filter-api-product/`,

    // })
});



function getProImage(id){ // filter product images returned product image
    let image	
    $.ajax({
        url: `${linkUrl}api/v1.0/filter-api-product-images/`,
        // async: false,
        global: false,
        dataType: 'json',
        
        success:function(res){
            console.log(res);
            for(let item of res){
                if (item.id == id ) {
                    image = item.image
                }
            }

        },
        error: function(res){
            console.log(res, 'error');
        }

    })
    return image

}

function getSearchData(urlLink){
    console.log('salam');
    $.ajax({
        dataType: 'json',
        async: false,
        global: false,
        url: `${urlLink}api/v1.0/products/`,

        success: function(data) {
        console.log(data);
        setStorage('products', data)
        },
        
        error: function(data){
            console.log(data);
        }
    });
}

function setStorage(key, value) { 
    let newData = JSON.stringify(value);
    localStorage.setItem(key, newData);
}

function getStorage(key) { //Gelen datani yoxlayiram localstorage de yoxdusa olani gosterirem ve return edirem
    if (localStorage.getItem(key) === null) {
        localStorage.setItem(key, JSON.stringify([]));
    }
    return localStorage.getItem(key);
}