function main(){
 // var $skillset = $('.skillset');
 // alert($skillset)
  $('.skillset').hide();
  $('.skillset').fadeIn(1000);
  $('.projects').hide();
  $('.projects-button').on('click', function() {
    //$(this).next().toggle();
    $(this).next().slideToggle(400);
    $(this).text('Projects Viewed').toggleClass('active');
  // execute the code here when .example-class is clicked.
});
  

}
  $(document).ready(main);