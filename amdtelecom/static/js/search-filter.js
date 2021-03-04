let urlDomain = `http://localhost:8000/`
let searchBody = $('#search-filter-body')
let DOM = $('#all-search-page-body')
let searchValue = document.querySelector('#search-filter-value')

searchBody.css('display', 'none')
searchLimited = ''
searchAllProducts = ''

searchValue.addEventListener('keyup', (e) => {

    let searchValueAll = searchValue.value
    searchAllProductsUrl = 'product'
    console.log('salam');
    if(e.keyCode == 13) {
        // e.preventDefault();
        window.open('newpage')
        getSearchData(searchValueAll, searchAllProducts)
        
    }
    
})


$(document).on('input', '#search-filter-value', function() { 
    // price range when changed keep values(min,max)
    searchLimited = 'searchLimited'
    value = $(this).val()
    console.log(value.length, 'uzunkuq');
    getSearchData(value, searchLimited)

    if (value.length > 0) {
        searchBody.css('display', 'block')
    }
    else{
        searchBody.css('display', 'none')
        searchBody.html('')
    }
    
});


function getSearchProImage(id){ // filter product images returned product image

    try {
        let image	
        let jsonDatas
        const datas = $.ajax({
            url: `${urlDomain}api/v1.0/filter-api-product-images/`,
            async: false,
            global: false,
            dataType: 'json',
        });
        jsonDatas = datas.responseJSON
        for(let item of jsonDatas){
            if (item.id == id ) {
                console.log('salam', item)
                image = item.image
                console.log(image, 'sekil');
            }
        }
        return image
    }catch(err){
        console.log(err);
    }

}

function getSearchProMarka(title){
    try {

        let image
        let jsonDatas

        const datas = $.ajax({
            dataType: 'json',
            async: false,
            global: false,
            url: `${urlDomain}api/v1.0/filter-api-product-markas/`,
            
        });
        jsonDatas = datas.responseJSON
        for(let item of jsonDatas){
            if (item.title == title ) {
                image = item.image
            }
        }

        jsonDatas = ''
        return image

    }catch(err){
        console.log(err);
    }

}


async function getSearchData(value, condition){

    try {
        
        let productBody = ''
        const title = value;
        let slug = ''
        
        
        let products = ''

        const datas = await $.ajax({
            dataType: 'json',
            async: true,
            global: false,
            url: `${urlDomain}api/v1.0/search/${title}`,
        });

        DOM.html('')
        
        if (condition == 'searchLimited') {
            console.log(datas, 'searchLimited');
            for (let product of datas){

                slug = `${urlDomain}product/${product.slug}/`
                console.log(product.operator_code);
                productBody += `
                <a href="${product.operator_code != null ? '#' : slug }" class="body">
                    <div class="data-img">
                        <img src="${product.operator_code != null ? getSearchProMarka(product.marka[0]) : getSearchProImage(product.images[0]) }" alt="">
                    </div>
                    <div class="data-title">
                        ${product.operator_code != null ? product.operator_code : product.marka[0]} ${product.color_title ? product.title + ' ' + product.color_title : product.title }
                    </div>
                </a>
                `
            }
        }
        else {
            for(let product of datas){
                console.log(product, 'allProduct');
                mainSeconImage = `
                <div class="front">
                    <a href="${urlDomain}product/${product.slug}/">
                    <img
                        src="${getSearchProImage(product.images[1])}"
                        class="img-fluid blur-up lazyload bg-img" alt="${product.title}" style="height: 271px;">
                    </a>
                </div>
                <div class="back">
                    <a href="${urlDomain}product/${product.slug}/">
                        <img
                            src="${getSearchProImage(product.images[0])}"
                            class="img-fluid blur-up lazyload bg-img" alt="${product.title}" style="height: 271px;">
                        </a>
                </div>
                <div class="cart-info cart-wrap">
                    <button data-toggle="modal" data-target="#addtocart" title="Add to cart"><i
                            class="ti-shopping-cart"></i></button> <a href="javascript:void(0)" title="Add to Wishlist"><i
                            class="ti-heart" aria-hidden="true"></i></a> <a href="#" data-toggle="modal" data-target="#quick-view" title="Quick View"><i
                            class="ti-search" aria-hidden="true"></i></a> <a href="compare.html" title="Compare"><i
                            class="ti-reload" aria-hidden="true"></i></a>
                </div>
                `

                secondImage = `
                <div class="front">
                    <a href="${urlDomain}product/${product.slug}/">
                    <img
                        src="${getSearchProMarka(product.images[0])}"
                        class="img-fluid blur-up lazyload bg-img" alt="${product.title}" style="height: 271px;">
                    </a>
                </div>
                `


                if(product.operator_code == None) {
                    if (product.color_code != null){ // productun rengi ucun
                        products += `
                                <div class="col-xl-3 col-6 col-grid-box">
                                <div class="product-box">
                                    <div class="img-wrapper">
                                        ${ product.images.length > 1 ? mainSeconImage : secondImage }
                                        <div class="cart-info cart-wrap">
                                            <button data-toggle="modal" data-target="#addtocart" title="Add to cart"><i
                                                    class="ti-shopping-cart"></i></button> <a href="javascript:void(0)" title="Add to Wishlist"><i
                                                    class="ti-heart" aria-hidden="true"></i></a> <a href="#" data-toggle="modal" data-target="#quick-view" title="Quick View"><i
                                                    class="ti-search" aria-hidden="true"></i></a> <a href="compare.html" title="Compare"><i
                                                    class="ti-reload" aria-hidden="true"></i></a>
                                        </div>
                                    </div>
                                    <div class="product-detail">
                                        <div>
                                            <a href="product-page(no-sidebar).html">
                                                <h6>${product.title}</h6>
                                            </a>
                                            <p>${product.description}
                                            </p>
                                            <h4>${product.price} AZN</h4>
                                            <ul class="color-variant">
                                                <li class="bg-light0" style="background-color: ${product.color_code} !important;"></li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        `
                    
                    }
                    else {
                        products += `
                                <div class="col-xl-3 col-6 col-grid-box">
                                <div class="product-box">
                                    <div class="img-wrapper">
                                    ${ product.images.length > 1 ? mainSeconImage : secondImage }
                                    </div>
                                    <div class="product-detail">
                                        <div>
                                            <a href="product-page(no-sidebar).html">
                                                <h6>${product.title}</h6>
                                            </a>
                                            <p>${product.description}
                                            </p>
                                            <h4>${product.price} AZN</h4>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        `
                    } // ${a == 1 && retun}
                }
                
                DOM.html(products)
                mainSeconImage = ''
                secondImage = ''
                products = ''
                searchValueAll = ''

            }  

        }  


        searchBody.html(productBody)
        productBody = ''
        slug = ''
        

    }catch(err){
        console.log(err);
    }
}
