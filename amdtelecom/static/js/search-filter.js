let urlDomain = `http://localhost:8000/`
let searchBody = $('#search-filter-body')
searchBody.css('display', 'none')
let searchValue = document.querySelector('#search-filter-value')

searchValue.addEventListener('keyup', (e) => {
    let value = this.value.trim()
    console.log(value, 'qara');
    if(value.length > 0) {
        if(e.keyCode == 13) {
            // e.preventDefault();
            // let value = $(this).val()
            window.open(`${urlDomain}search/?q=${value}`)
            // getSearchData(value)
        }
    }
    else {
        return false
    }
})
    

$(document).on('input', '#search-filter-value', function() { 
    // price range when changed keep values(min,max)
    value = $(this).val().trim()
    // console.log(value.length, 'uzunkuq');
    

    if (value.length > 0) {
        searchBody.css('display', 'block')
        getSearchData(value)
    }
    else{
        searchBody.css('display', 'none')
        searchBody.html('')
    }
    
});

// searchValue.addEventListener('focusout', () => {
//     searchDataBody = 
//     console.log(searchDataBody, 'mollar');
//     if (searchDataBody){
//         console.log('salam');
//     }
//     // if (searchBody.length > 0){
//         searchBody.css('display', 'none')
//     // }
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
        
        
        searchBody.html('')
        const title = value;
        
        let slug = ''

        const datas = await $.ajax({
            dataType: 'json',
            async: true,
            global: false,
            url: `${urlDomain}api/v1.0/search/?q=${title}`,
        });
        // <div class="data-img">
        //     <img src="${product.operator_code != null ? getSearchProMarka(product.marka[0]) : getSearchProImage(product.images[0]) }" alt="">
        // </div>
        if (datas.length > 1){
            let productBody = ''
            searchBody.html('')

            for (let product of datas){

                slug = `${urlDomain}product/${product.slug}/`
                console.log(product.operator_code);
                productBody += `
                <a href="${slug}" class="body">

                    <div class="data-title">
                        ${product.marka[0]} ${ product.title }
                    </div>
                </a>
                `
            }
            searchBody.html(productBody)
            productBody = ''
            slug = ''
        }
        else {
            searchBody.html('')
        }


    }catch(err){
        console.log(err);
    }
}
