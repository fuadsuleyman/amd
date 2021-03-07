const domain = `http://localhost:8000/`

// keep this page category id
const categoryProduct = $('.category-pro')[0]
let theCategory = categoryProduct.getAttribute('for-filter')

// the seuences for min and max price 
// default empty
let min_max = ''
let min_max_arr = []
let min = ''
let max = ''

$(document).on('input', '#range', function() { // price range when changed keep values(min,max)
    $('#slider_value').html( $(this).val() );
    min_max = $(this).val()
    min_max_arr = min_max.split(';')

    min = min_max_arr[0]
    max = min_max_arr[1]

    getData()

});

function getProImage(id){ // filter product images returned product image
    let image	
    $.ajax({
        url: `${domain}api/v1.0/filter-api-product-images/`,
        async: false,
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

function getProMarka(id){
    let image
    console.log(id, 'meselen');
    $.ajax({
        url: `${domain}api/v1.0/filter-api-product-markas/`,
        async: false,
        global: false,
        dataType: 'json',
        
        success:function(res){
            console.log(res, 'markalar');
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

function getData() { // filter product data return products
    // $(".ajaxLoader").hide();

    var _filterObj={};
    _filterObj['price_min'] = min
    _filterObj['price_max'] = max
    _filterObj['category'] = theCategory


    if($(".filter-item-checkbox")){
        $(".filter-item-checkbox").each(function(index,ele){
            _filterObj['price_min'] = min
            _filterObj['price_max'] = max
            var _filterVal=$(this).val();
            var _filterKey=$(this).data('filter');

            console.log(min);
            // if (min == ''){
            // }
            _filterObj[_filterKey]=Array.from(document.querySelectorAll('input[data-filter='+_filterKey+']:checked')).map(function(el){
                return el.value;
            })

            console.log(_filterObj, 'gelen datalar');

        });
    }
    // else{
    //     log
    // }
    console.log(_filterObj, 'yeni');

    $.ajax({
        url: `${domain}api/v1.0/filter-api-product/`,
        type : 'GET',
        data: _filterObj,
        dataType:'json',
        beforeSend: () => {
            $('.loadMore').html('Buraya klik edin')
        },
        success:function(response){
            console.log(response, 'product data');
            let DOM = $('.prod-items')
            let products = ''
            if (response.length > 0){  

                for(let product of response){
                    // console.log(product, 'datalar');
                    mainSeconImage = `
                    <div class="front">
                        <a href="${domain}product/${product.slug}/">
                        <img
                            src="${getProImage(product.images[1])}"
                            class="img-fluid blur-up lazyload bg-img" alt="${product.title}" style="height: 271px;">
                        </a>
                    </div>
                    <div class="back">
                        <a href="${domain}product/${product.slug}/">
                            <img
                                src="${getProImage(product.images[0])}"
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
                        <a href="${domain}product/${product.slug}/">
                        <img
                            src="${getProImage(product.images[0])}"
                            class="img-fluid blur-up lazyload bg-img" alt="${product.title}" style="height: 271px;">
                        </a>
                    </div>
                    `

                    // nomrelerin filteri ucun
                    if(product.operator_code) {

                        products += `
                            <div class="col-xl-4 col-6 col-grid-box category-pro" style="margin-top: 20px;">
                            <div class="numberCard">
                                <div class="numberCard__container">

                                    <div class="numberCard__container__head">
                                        
                                        <ul>
                                            <li>
                                                <svg class="MuiSvgIcon-root" focusable="false" viewBox="0 0 24 24" aria-hidden="true" style="cursor:pointer">
                                                    <path d="M15.55 13c.75 0 1.41-.41 1.75-1.03l3.58-6.49c.37-.66-.11-1.48-.87-1.48H5.21l-.94-2H1v2h2l3.6 7.59-1.35 2.44C4.52 15.37 5.48 17 7 17h12v-2H7l1.1-2h7.45zM6.16 6h12.15l-2.76 5H8.53L6.16 6zM7 18c-1.1 0-1.99.9-1.99 2S5.9 22 7 22s2-.9 2-2-.9-2-2-2zm10 0c-1.1 0-1.99.9-1.99 2s.89 2 1.99 2 2-.9 2-2-.9-2-2-2z"></path>
                                                </svg>
                                            </li>
                                            <li>
                                                <svg class="MuiSvgIcon-root" focusable="false" viewBox="0 0 24 24" aria-hidden="true">
                                                    <path d="M16.5 3c-1.74 0-3.41.81-4.5 2.09C10.91 3.81 9.24 3 7.5 3 4.42 3 2 5.42 2 8.5c0 3.78 3.4 6.86 8.55 11.54L12 21.35l1.45-1.32C18.6 15.36 22 12.28 22 8.5 22 5.42 19.58 3 16.5 3zm-4.4 15.55l-.1.1-.1-.1C7.14 14.24 4 11.39 4 8.5 4 6.5 5.5 5 7.5 5c1.54 0 3.04.99 3.57 2.36h1.87C13.46 5.99 14.96 5 16.5 5c2 0 3.5 1.5 3.5 3.5 0 2.89-3.14 5.74-7.9 10.05z"></path>
                                                </svg>
                                            </li>
                                        </ul>

                                    </div>

                                    <div class="numberCard__container__body">
                                        <div class="numberCard__container__body-img">
                                            <img src="${getProMarka(product.marka[0])}" alt="" style="height: 72px; width: 72px;">
                                        </div>
                                        <div class="numberCard__container__body-number">
                                            <p class="m-0 text-dark">(<!-- -->${product.operator_code}<!-- -->) <!-- -->${product.title}</p>
                                        </div>
                                    </div>

                                    <div class="numberCard__container__footer">
                                        <div class="numberCard__container__footer-price">
                                            <span class="text-dark">
                                                ${product.price}
                                                <svg id="Layer_1" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 37.41 32.09">
                                                    <defs>
                                                        <style>
                                                            .cls-1<!-- -->{<!-- -->fill:#2b2929<!-- -->}
                                                        </style>
                                                    </defs>
                                                    <title>manat</title>
                                                    <path class="cls-1" d="M312.33 418.63q-4.54-9.25-13.63-9.89l-.11-3.83-2.26.92-.14 2.9q-8.91.56-13.57 9.73-3.89 7.71-3.89 18.54h5.51c.2-16 5.47-24.67 11.88-26l-.7 23.66 4-1.37-.65-22.41c6.43.75 11.89 9.45 12 26.1h5.41q-.09-10.85-3.81-18.37z" transform="translate(-278.73 -404.91)" id="Layer_1-2"></path>
                                                </svg>
                                            </span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            
                        </div>
                        `
                    }
                    else {
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
                    

                }  
            }
            else {
                DOM.html('')
            }  

            _filterObj = {}
        },
        error: function(response){
            console.log(response, 'error');
        }

    })
    // console.log(_filterObj)


}

