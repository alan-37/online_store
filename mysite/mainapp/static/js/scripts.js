$(document).ready(function(){
    var form = $('#buy_product');
    console.log(form);
    form.on('submit', function(e){
        e.preventDefault();

        var nmb = $('#number').val();

        console.log(nmb);
        var submit_button = $('#buy');
        var product_max = submit_button.data("max");
        if (product_max < nmb){
            nmb = product_max
        };
        var product_id = submit_button.data("product_id");
        var product_name = submit_button.data("name");
        var product_price = submit_button.data("price");
        console.log(product_id);
        console.log(product_name);
        console.log(product_price);
        var data = {};
        data.product_id = product_id;
        data.nmb = nmb;
        var csrftoken = $("#buy_product [name=csrfmiddlewaretoken]").val();
        data['csrfmiddlewaretoken'] = csrftoken;
        var url = form.attr('action');
        console.log(data);
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function(data){
                console.log('OK');
                console.log(data.product_total_nmb)
                if (data.product_total_nmb){
                    $('#basket_total_nmb').text(data.product_total_nmb);
                    console.log(data.products);
                    $('.basket-item ul').html("");

                    $.each(data.products, function(k, v){
                        $('.basket-item ul').append(' <li style="display: block;"> '+v.name+' '+v.nmb+ 'шт.     '+v.total_price+' р </li>');
                    })
                    }
                }

            ,
            error: function(){
                console.log('ERROR')
            }

        });


    });

    $('.basket-cont').mouseover(function()
    {
        $('.basket-item').removeClass('hidden');
    })
        $('.basket-cont').mouseout(function()
    {
        $('.basket-item').addClass('hidden');
    })
    $(document).on('click', '.delete-item', function(e)
    {
        e.preventDefault();
        $(this).closest('li').remove();
    })
    function CalculatingPrice(){
        var total_price_in_basket = 0;
        $('.product-amount-price').each(function(){
            total_price_in_basket +=parseInt($(this).text());
        });
        $('#total_price_in_basket').text(total_price_in_basket);

    };

    $(document).on('change', '.product-basket-nmb', function(){
        var current_nmb = $(this).val();
        var current_tr = $(this).closest('tr');
        var current_price = parseInt(current_tr.find('.product-price-item').text());
        var total_amount = current_nmb * current_price;
        current_tr.find('.product-amount-price').text(total_amount);
        CalculatingPrice()
    });

    CalculatingPrice()
});

