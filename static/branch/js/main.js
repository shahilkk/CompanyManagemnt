if ($('.counter').length > 0) {
    $('.counter').counterUp({
        delay: 20,
        time: 2000
    });
}

if ($('.datetimepicker').length > 0) {
    $('.datetimepicker').datetimepicker({
        format: 'DD-MM-YYYY',
        icons: {
            up: "fas fa-angle-up",
            down: "fas fa-angle-down",
            next: 'fas fa-angle-right',
            previous: 'fas fa-angle-left'
        }
    });
}

//  $('body').append('<div class="sidebar-overlay"></div>');
// $(document).on('click', '#mobile_btn', function () {
// 	$wrapper.toggleClass('slide-nav');
// 	$('.sidebar-overlay').toggleClass('opened');
// 	$('html').toggleClass('menu-opened');
// 	return false;
// });



$(document).on('click', '#toggle_btn', function () {
    if ($('body').hasClass('mini-sidebar')) {
        $('body').removeClass('mini-sidebar');
        $('.subdrop + ul').slideDown();
    } else {
        $('body').addClass('mini-sidebar');
        $('.subdrop + ul').slideUp();
    }
    setTimeout(function () {
        mA.redraw();
        mL.redraw();
    }, 300);
    return false;
});
// ---------------------

"use strict";

// Variables declarations

var $wrapper = $('.main-wrapper');
var $pageWrapper = $('.page-wrapper');
var $slimScrolls = $('.slimscroll');

// Sidebar
var Sidemenu = function () {
    this.$menuItem = $('#sidebar-menu a');
};

function init() {
    var $this = Sidemenu;
    $('#sidebar-menu a').on('click', function (e) {
        if ($(this).parent().hasClass('submenu')) {
            e.preventDefault();
        }
        if (!$(this).hasClass('subdrop')) {
            $('ul', $(this).parents('ul:first')).slideUp(350);
            $('a', $(this).parents('ul:first')).removeClass('subdrop');
            $(this).next('ul').slideDown(350);
            $(this).addClass('subdrop');
        } else if ($(this).hasClass('subdrop')) {
            $(this).removeClass('subdrop');
            $(this).next('ul').slideUp(350);
        }
    });
    $('#sidebar-menu ul li.submenu a.active').parents('li:last').children('a:first').addClass('active').trigger('click');
}

// Sidebar Initiate
init();

// Mobile menu sidebar overlay
$('body').append('<div class="sidebar-overlay"></div>');
$(document).on('click', '#mobile_btn', function () {
    $wrapper.toggleClass('slide-nav');
    $('.sidebar-overlay').toggleClass('opened');
    $('html').toggleClass('menu-opened');
    return false;
});

// Sidebar overlay
$(".sidebar-overlay").on("click", function () {
    $wrapper.removeClass('slide-nav');
    $(".sidebar-overlay").removeClass("opened");
    $('html').removeClass('menu-opened');
});

// Page Content Height
if ($('.page-wrapper').length > 0) {
    var height = $(window).height();
    $(".page-wrapper").css("min-height", height);
}

// Page Content Height Resize
$(window).resize(function () {
    if ($('.page-wrapper').length > 0) {
        var height = $(window).height();
        $(".page-wrapper").css("min-height", height);
    }
});

// Select 2
if ($('.select').length > 0) {
    $('.select').select2({
        minimumResultsForSearch: -1,
        width: '100%'
    });
}
// ------------------




//    toggle

// end toggle

// filters
$(document).on('click', '#filter_search', function () {
    $('#filter_inputs').slideToggle("slow");
});

// endfilter



// datatable
// if ($('.datatable').length > 0) {
//     $('.datatable').DataTable({
//         language: {
//             search: '<i class="fas fa-search"></i>',
//             searchPlaceholder: "Search"
//         }
//     });
// }
// end datatable





// end  + in add invoice




// selectbox
$('.app-listing .selectBox').on("click", function () {
    $(this).parent().find('#checkBoxes').fadeToggle();
    $(this).parent().parent().siblings().find('#checkBoxes').fadeOut();
});

$('.invoices-main-form .selectBox').on("click", function () {
    $(this).parent().find('#checkBoxes-one').fadeToggle();
    $(this).parent().parent().siblings().find('#checkBoxes-one').fadeOut();
});
// end selectbox




$(".add-table-items").on('click', '.remove-btn', function () {
    $(this).closest('.add-row').remove();
    return false;

});

