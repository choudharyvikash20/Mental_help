$('.tet-carousel').owlCarousel({
          loop:true,
          margin:20,
          autoplay:true,
          autoplayTimeout: 2000,
          dots:false,
          responsive:{
              0:{
                  items:1
              },
              500:{
                  items:2
              },
              850:{
              items:3
              },
              1000:{
                  items:4
              }
          }
      })
