let urlDomain = `http://localhost:8000/`
let searchBody = $('#search-filter-body')
searchBody.css('display', 'none')



$(document).on('input', '#search-filter-value', function() { 
    // price range when changed keep values(min,max)
    value = $(this).val()
    console.log(value.length, 'uzunkuq');
    if (value.length > 0) {
        searchBody.css('display', 'block')
        getSearchData(value)
    }
    
});

function getSearchProImage(id){ // filter product images returned product image
    let image	
    $.ajax({
        url: `${urlDomain}api/v1.0/filter-api-product-images/`,
        async: false,
        global: false,
        dataType: 'json',
        
        success:function(res){
            console.log(res, 'datalar');
            for(let item of res){
                console.log(item.id)
                if (item.id == id ) {
                    console.log('salam', item)
                    image = item.image
                    console.log(image, 'sekil');
                }
            }

        },
        error: function(res){
            console.log(res, 'error');
        }

    })
    return image

}

function getSearchProMarka(title){
    try {
        let image
        console.log(title, 'meselen');
    $.ajax({
        url: `${urlDomain}api/v1.0/filter-api-product-markas/`,
        async: false,
        global: false,
        dataType: 'json',
        
        success:function(res){
            for(let item of res){
                // console.log(item, 'adlar');
                if (item.title == title ) {
                    image = item.image
                }
            }
        },
        error: function(res){
            console.log(res, 'error');
        }

    })
    return image
    }catch(err){
        console.log(err);
    }

}


async function getSearchData(value){
    productBody = ''
    try {
        const title = value;
        let slug = ''
        const datas = await $.ajax({
            dataType: 'json',
            async: true,
            global: false,
            url: `${urlDomain}api/v1.0/search/${title}`,
        });
        // console.log("Data:", datas);
        for (let product of datas){
            slug = `"${urlDomain}product/${product.slug}/"`
            console.log(product.operator_code);
            productBody += `
            <a href="${product.operator_code != null ? '#' : slug }" class="body">
                <div class="data-img">
                    <img src="${product.operator_code != null ? getSearchProMarka(product.marka[0]) : getSearchProImage(product.images[0]) }" alt="">
                </div>
                <div class="data-title">
                    ${product.marka[0]} ${product.title}
                </div>
            </a>
            `
        }
        searchBody.html(productBody)
        productBody = ''
        slug = ''
        

    }catch(err){
        console.log(err);
    }
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