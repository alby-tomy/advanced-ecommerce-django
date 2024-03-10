// to get current year
function getYear() {
    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();
    document.querySelector("#displayYear").innerHTML = currentYear;
}

getYear();


// client section owl carousel
$(".client_owl-carousel").owlCarousel({
    loop: true,
    margin: 0,
    dots: false,
    nav: true,
    navText: [],
    autoplay: true,
    autoplayHoverPause: true,
    navText: [
        '<i class="fa fa-angle-left" aria-hidden="true"></i>',
        '<i class="fa fa-angle-right" aria-hidden="true"></i>'
    ],
    responsive: {
        0: {
            items: 1
        },
        768: {
            items: 2
        },
        1000: {
            items: 2
        }
    }
});



/** google_map js **/
function myMap() {
    var mapProp = {
        center: new google.maps.LatLng(40.712775, -74.005973),
        zoom: 18,
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
}


function handleImageMagnification() {
    const images = document.querySelectorAll('.product-image');
    images.forEach((image) => {
        image.addEventListener('mousemove', (e) => {
            const { left, top } = image.getBoundingClientRect();
            const x = e.clientX - left;
            const y = e.clientY - top;
            const offsetX = 100; // Half the width of the magnify box
            const offsetY = 100; // Half the height of the magnify box
            const translateX = x - offsetX;
            const translateY = y - offsetY;
            const magnify = image.nextElementSibling;
            magnify.style.backgroundImage = `url('${image.src}')`;
            magnify.style.backgroundSize = `${image.width * 2}px ${image.height * 2}px`;
            magnify.style.backgroundPosition = `-${translateX}px -${translateY}px`;
        });
    });s
}
handleImageMagnification();