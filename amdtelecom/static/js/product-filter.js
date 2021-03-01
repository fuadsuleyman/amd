const domain = `http://localhost:8000/`
console.log('salam');
// keep this page category id
const categoryProduct = $('.category-pro')[0]
let theCategory = categoryProduct.getAttribute('for-filter')

// the seuences for min and max price 
// default empty
let min_max = ''
let min_max_arr = []
let min = ''
let max = ''
// price range when changed keep values(min,max)
$(document).on('input', '#range', function() {
    $('#slider_value').html( $(this).val() );
    min_max = $(this).val()
    min_max_arr = min_max.split(';')

    min = min_max_arr[0]
    max = min_max_arr[1]

    getData()
    // var ans = 0.50;

    // if($(this).val() == 0.50){
    // alert("ans");
    // }

});

function getProImage(id){
    let image	
    let mainImage, secondImage
    let filterProductImage = {}
    $.ajax({
        url: `${domain}api/v1.0/filter-api-product-images/`,
        // data: _filterObj,
        async: false,
        global: false,
        dataType: 'json',
        
        success:function(res){
            console.log(res);
            for(let item of res){
                // console.log(j);
                // console.log(j.id);
                if (item.id == id ) {
                    image = item.image
                    // console.log(item.is_main, 'main');
                    // console.log(item.is_second_main, 'second');
                    // if(item.is_main){
                    //     mainImage = item.image
                    //     return mainImage
                    //     console.log(mainImage, 'main image');
                    // }
                    // if(item.is_second_main){
                    //     secondImage = item.image
                    //     return secondImage
                    //     console.log(secondImage, 'second image');
                    // }
                    
                    // console.log(item.is_main, 'salam');
                
                }
            }
            // console.log(secondImage, 'second');
            // console.log(mainImage, 'main');
            // if (mainImage != undefined){
            //     filterProductImage['mainImage'] = mainImage
            //     return filterProductImage.mainImage
            // }
            // else if (secondImage != undefined) {
            //     filterProductImage['secondImage'] = secondImage
            //     return filterProductImage.secondImage
            // }
            // console.log(filterProductImage.mainImage);
            // console.log(filterProductImage.secondImage);
        },
        error: function(res){
            console.log(res, 'error');
        }

    })
    return image

}



function getData() {
    $(".ajaxLoader").hide();

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

            console.log(_filterObj);

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
        success:function(response){
            console.log(response, 'product data');
            let DOM = $('.prod-items')
            let products = ''
            if (response.length > 0){  

                for(let product of response){
                    console.log(product, 'datalar');
                    if (product.color_code != null){
                        if (product.images.length > 1){
                            products += `
                                    <div class="col-xl-3 col-6 col-grid-box">
                                    <div class="product-box">
                                        <div class="img-wrapper">
                                            <div class="front">
                                                    <a href="http://localhost:8000/product/${product.slug}/">
                                                    <img
                                                        src="${getProImage(product.images[1])}"
                                                        class="img-fluid blur-up lazyload bg-img" alt="${product.title}" style="height: 271px;">
                                                    </a>
                                            </div>
                                            <div class="back">
                                                <a href="http://localhost:8000/product/${product.slug}/">
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
                                                    <!-- <li class="bg-light1"></li>
                                                    <li class="bg-light2"></li> -->
                                                </ul>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            `
                        }
                        else{
                            products += `
                            <div class="col-xl-3 col-6 col-grid-box">
                            <div class="product-box">
                                <div class="img-wrapper">
                                    <div class="front">
                                            <a href="http://localhost:8000/product/${product.slug}/">
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
                                            <!-- <li class="bg-light1"></li>
                                            <li class="bg-light2"></li> -->
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                    `
                        }
                    }
                    else {
                        if (product.images.length > 1){
                            products += `
                                    <div class="col-xl-3 col-6 col-grid-box">
                                    <div class="product-box">
                                        <div class="img-wrapper">
                                            <div class="front">
                                                    <a href="http://localhost:8000/product/${product.slug}/">
                                                    <img
                                                        src="${getProImage(product.images[1])}"
                                                        class="img-fluid blur-up lazyload bg-img" alt="${product.title}" style="height: 271px;">
                                                    </a>
                                            </div>
                                            <div class="back">
                                                <a href="http://localhost:8000/product/${product.slug}/">
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
                        }
                        else{
                            products += `
                            <div class="col-xl-3 col-6 col-grid-box">
                            <div class="product-box">
                                <div class="img-wrapper">
                                    <div class="front">
                                            <a href="http://localhost:8000/product/${product.slug}/">
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
                        }
                    }
                    DOM.html(products)
                    

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

