let urlDomain = `http://localhost:8000/`
let searchBody = $('#search-filter-body')
searchBody.css('display', 'none')
let searchValue = document.querySelector('#search-filter-value')


$(document).on('input', '#search-filter-value', function() { 
    // price range when changed keep values(min,max)
    value = $(this).val()
    console.log(value.length, 'uzunkuq');
    getSearchData(value)

    if (value.length > 0) {
        searchBody.css('display', 'block')
    }
    else{
        searchBody.css('display', 'none')
        searchBody.html('')
    }
    
});

// searchValue.addEventListener('focusout', () => {
//     searchDataBody = $('#search-filter-body > *').on('focus', (event) => {
//         console.log(event.target[0]);
//         searchBody.css('display', 'block')
//     })
//     console.log(searchDataBody, 'mollar');
//     searchBody.css('display', 'none')
//     // searchBody.html('')
// });

// searchValue.addEventListener('focusin', () => {
//     searchBody.css('display', 'block')

// });


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
        // console.log(datas, 'promarka');
        console.log(jsonDatas.length, 'uzuluq');
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


async function getSearchData(value){

    try {
        
        let productBody = ''
        const title = value;
        let slug = ''

        const datas = await $.ajax({
            dataType: 'json',
            async: true,
            global: false,
            url: `${urlDomain}api/v1.0/search/${title}`,
        });

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

        searchBody.html(productBody)
        productBody = ''
        slug = ''
        

    }catch(err){
        console.log(err);
    }
}

// function setStorage(key, value) { 
//     let newData = JSON.stringify(value);
//     localStorage.setItem(key, newData);
// }

// function getStorage(key) { //Gelen datani yoxlayiram localstorage de yoxdusa olani gosterirem ve return edirem
//     if (localStorage.getItem(key) === null) {
//         localStorage.setItem(key, JSON.stringify([]));
//     }
//     return localStorage.getItem(key);
// }