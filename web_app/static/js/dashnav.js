
$(".s-sidebar__nav-link").click(function() {

         // if(!$(this).hasClass('nav-active')){
            var listItems = $(".s-sidebar__nav-link");

            for (let i = 0; i < listItems.length; i++) {
                listItems[i].classList.remove("nav-active");
            }
            this.classList.add("nav-active");
          // }
});
