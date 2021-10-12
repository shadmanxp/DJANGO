 $(document).ready(function () {
   $('#zoom_image').ezPlus({
        zoomType: 'inner',
		cursor: 'crosshair',
		scrollZoom: true
    });
//     $("#zoom_image").ezPlus({
//      gallery: 'zoom_image_gallery',
//      cursor: 'pointer',
//      galleryActiveClass: "active",
//      imageCrossfade: true,
//      loadingIcon: "images/spinner.gif"
//    });
//    $("#zoom_image").bind("click", function (e) {
//      var ez = $('#zoom_03').data('ezPlus');
//      ez.closeAll();
//      $.fancybox(ez.getGalleryList());
//      return false;
//    });
 });

