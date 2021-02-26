$(document).ready(() => {
    function test() {
			
		
        var category = $('#categoryId').data('category')
        console.log($(this))
        var _filterObj={};
        $(".filter-item-checkbox").each(function(index,ele){
            var _filterVal=$(this).val();
            var _filterKey=$(this).data('filter');
            _filterObj[_filterKey]=Array.from(document.querySelectorAll('input[data-filter='+_filterKey+']:checked')).map(function(el){
                return el.value;
            });
        });

})